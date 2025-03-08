# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

users = []
movies = []
shows = []
bookings = []

# User Registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    for user in users:
        if user['username'] == username:
            return jsonify({"message": "User already exists"}), 400

    users.append({"username": username, "password": password})
    return jsonify({"message": "User registered successfully"}), 201

# User Login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    for user in users:
        if user['username'] == username and user['password'] == password:
            return jsonify({"message": "Login successful"}), 200

    return jsonify({"message": "Invalid credentials"}), 401

# Add Movie (Theater Owner)
@app.route('/movies', methods=['POST'])
def add_movie():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')

    if not title or not description:
        return jsonify({"message": "Title and description are required"}), 400

    movie = {
        "id": len(movies) + 1,
        "title": title,
        "description": description
    }
    movies.append(movie)
    return jsonify({"message": "Movie added successfully", "movie": movie}), 201

# Get Movies
@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify(movies), 200

# Add Show (Theater Owner)
@app.route('/shows', methods=['POST'])
def add_show():
    data = request.get_json()
    movie_id = data.get('movie_id')
    time = data.get('time')
    available_seats = data.get('available_seats')

    if not movie_id or not time or available_seats is None:
        return jsonify({"message": "Movie ID, time, and available seats are required"}), 400

    if not any(movie['id'] == movie_id for movie in movies):
        return jsonify({"message": "Invalid movie ID"}), 404

    show = {
        "id": len(shows) + 1,
        "movie_id": movie_id,
        "time": time,
        "available_seats": available_seats
    }
    shows.append(show)
    return jsonify({"message": "Show added successfully", "show": show}), 201

# Get Shows
@app.route('/shows', methods=['GET'])
def get_shows():
    return jsonify(shows), 200

# Book Seat (User)
@app.route('/book', methods=['POST'])
def book_seat():
    data = request.get_json()
    username = data.get('username')
    show_id = data.get('show_id')

    if not username or not show_id:
        return jsonify({"message": "Username and show ID are required"}), 400

    show = next((s for s in shows if s['id'] == show_id), None)

    if not show:
        return jsonify({"message": "Show not found"}), 404

    if show['available_seats'] <= 0:
        return jsonify({"message": "No seats available"}), 400

    show['available_seats'] -= 1
    booking = {"username": username, "show_id": show_id}
    bookings.append(booking)

    return jsonify({"message": "Seat booked successfully", "booking": booking}), 201

# View User Bookings
@app.route('/bookings/<username>', methods=['GET'])
def get_user_bookings(username):
    user_bookings = [b for b in bookings if b['username'] == username]

    if not user_bookings:
        return jsonify({"message": "No bookings found for user"}), 404

    return jsonify(user_bookings), 200

if __name__ == '__main__':
    app.run(debug=True)
