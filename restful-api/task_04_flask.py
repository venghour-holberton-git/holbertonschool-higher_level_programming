#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)
all_users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    users = [k for k, v in all_users.items()]
    return jsonify(users), 200

@app.route("/status")
def status():
    return "OK", 200

@app.route("/users/<username>")
def user(username):
    if not username in all_users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(all_users[username]), 200

@app.route("/users")
def user_no_name():
    return jsonify({"error":"Username already exists"}), 404

@app.route("/add_user", methods=['POST'])
def add_user():
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
            "message": "User added",
            "user": data
        }
    ), 201

if __name__ == "__main__":
    app.run()