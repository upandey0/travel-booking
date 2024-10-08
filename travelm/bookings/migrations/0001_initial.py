# Generated by Django 5.1.1 on 2024-09-09 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('number_of_seats', models.PositiveIntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('CONFIRMED', 'Confirmed'), ('CANCELLED', 'Cancelled')], default='CONFIRMED', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TravelOption',
            fields=[
                ('travel_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('FLIGHT', 'Flight'), ('TRAIN', 'Train'), ('BUS', 'Bus')], max_length=10)),
                ('source', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('date_time', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available_seats', models.PositiveIntegerField()),
            ],
        ),
    ]
