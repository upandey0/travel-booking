from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('travel-options/', views.travel_options, name='travel_options'),
    path('book/<int:travel_id>/', views.book_ticket, name='book_ticket'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]