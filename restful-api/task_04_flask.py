#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)
all_users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!", 200


@app.route("/data")
def data():
     return jsonify({"users": dict(all_users)}), 200


@app.route("/status")
def status():
    return "OK", 200


@app.route("/users/<username>")
def user(username):
    if username not in all_users:
        return jsonify({"error": "User not found"}), 404

    return jsonify(all_users[username]), 200


@app.route("/add_user", methods=['POST'])
def add_user():
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    if username in all_users:
        return jsonify({"error": "Username already exists"}), 409

    all_users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()