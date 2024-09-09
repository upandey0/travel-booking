# Travel Booking App

This is a Django-based web application that allows users to search, book, and manage travel options.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

To run the Travel Booking App locally, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/upandey0/travel-booking/
   ```

2. Change to the project directory:
   ```
   
   ```

3. Create a virtual environment and activate it:
   ```
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Set up the database:
   ```
   python manage.py migrate
   ```

6. Create a superuser account:
   ```
   python manage.py createsuperuser
   ```

7. Start the development server:
   ```
   python manage.py runserver
   ```

8. Open your web browser and visit `http://localhost:8000` to access the Travel Booking App.

## Usage

- **Register**: Users can create an account to access the booking system.
- **Login**: Registered users can log in to the application.
- **Search Travel Options**: Users can search for available travel options (flights, trains, buses) based on various filters.
- **Book Tickets**: Users can book tickets for their selected travel options.
- **Manage Bookings**: Users can view their upcoming and past bookings, and cancel confirmed bookings.
- **Admin Panel**: The admin user can manage users, travel options, and bookings through the Django admin interface.

## Features

- User authentication (registration, login, logout)
- Search and filter travel options by type, source, destination, and date
- Booking and payment system
- Booking management (view, cancel)
- Admin panel for managing users, travel options, and bookings

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch to your forked repository.
5. Submit a pull request to the original repository.

## License

This project is licensed under the [MIT License](LICENSE).