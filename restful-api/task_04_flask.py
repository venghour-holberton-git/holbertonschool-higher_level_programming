#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)
all_users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}
    return jsonify(users)

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def user(username):
    users = {"jane": {"name": username, "age": 28, "city": "Los Angeles"}}
    return jsonify(users)

@app.route("/users")
def user_no_name():
    return jsonify({"error":"Username already exists"}), 404

@app.route("/add_user", methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        data = request.get_json(silent=True)
        if data is None:
            return jsonify({"error": "Invalid JSON"}), 400
        if "username" not in data:
            return jsonify({"error":"Username is required"}), 400
        if data["username"] in all_users:
            return jsonify({"error":"Username already exists"}), 409
        all_users[data["username"]] = data
        return jsonify(
            {
                "message": "User is added",
                "user": data
            }
        ), 201

if __name__ == "__main__":
    app.run()