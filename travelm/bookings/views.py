from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TravelOption, Booking
from .forms import BookingForm
from django.db.models import Q

def home(request):
    return render(request, 'bookings/home.html')

def travel_options(request):
    options = TravelOption.objects.filter(available_seats__gt=0)
    
    # Filter logic
    if request.GET:
        if 'type' in request.GET:
            options = options.filter(type=request.GET['type'])
        if 'source' in request.GET:
            options = options.filter(source__icontains=request.GET['source'])
        if 'destination' in request.GET:
            options = options.filter(destination__icontains=request.GET['destination'])
        if 'date' in request.GET:
            options = options.filter(date_time__date=request.GET['date'])
        
    return render(request, 'bookings/travel_options.html', {'options': options})

@login_required
def book_ticket(request, travel_id):
    travel_option = get_object_or_404(TravelOption, pk=travel_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.travel_option = travel_option
            booking.total_price = travel_option.price * booking.number_of_seats
            
            if booking.number_of_seats <= travel_option.available_seats:
                booking.save()
                travel_option.available_seats -= booking.number_of_seats
                travel_option.save()
                return redirect('my_bookings')
            else:
                form.add_error('number_of_seats', 'Not enough seats available.')
    else:
        form = BookingForm()
    return render(request, 'bookings/book_ticket.html', {'form': form, 'travel_option': travel_option})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    if booking.status == 'CONFIRMED':
        booking.status = 'CANCELLED'
        booking.save()
        travel_option = booking.travel_option
        travel_option.available_seats += booking.number_of_seats
        travel_option.save()
    return redirect('my_bookings')