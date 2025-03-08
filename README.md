# Movie Ticket Booking System

A simple Flask-based API for managing movie tickets, including user authentication, movie and show management, and ticket booking.

## Features
- User Registration & Login
- Add and View Movies (for theater owners)
- Add and View Shows (with seat availability)
- Book Seats for a Show
- View User Booking History

## Prerequisites
- Python 3.x
- Flask

## Setup Instructions
1. Clone the repository and navigate to the project folder.
2. Install dependencies:

    ```bash
    pip install Flask
    ```

3. Run the application:

    ```bash
    python app.py
    ```

4. API will be available at: `http://localhost:5000`

## API Endpoints

### User Authentication
- **POST /register** - Register a new user
    ```json
    {
      "username": "user1",
      "password": "pass123"
    }
    ```
- **POST /login** - Login a user

### Movie Management
- **POST /movies** - Add a movie (title, description)
- **GET /movies** - Get all movies

### Show Management
- **POST /shows** - Add a show (movie_id, time, available_seats)
- **GET /shows** - Get all shows

### Booking
- **POST /book** - Book a seat
    ```json
    {
      "username": "user1",
      "show_id": 1
    }
    ```

- **GET /bookings/<username>** - View user bookings

## Example Usage
1. Register a user:
    ```bash
    curl -X POST http://localhost:5000/register -H "Content-Type: application/json" -d '{"username": "user1", "password": "pass123"}'
    ```
2. Add a movie:
    ```bash
    curl -X POST http://localhost:5000/movies -H "Content-Type: application/json" -d '{"title": "Inception", "description": "Sci-fi thriller"}'
    ```

## Notes
- Ensure Flask is installed before running the app.
- Debug mode is enabled for development purposes.

## License
MIT License

