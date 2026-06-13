#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity, get_jwt
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username)["password"], password):
        return username

@app.route('/')
@auth.login_required
def index():
    return "Hello, {}!".format(auth.current_user())

@auth.get_user_roles
def get_user_roles(user):
    print(f"uuuu {user}")
    return user.get_roles()

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    for k, v in users.items():
        if username == v["username"] and check_password_hash(v.get("password"), password):
            print("access granted")
            access_token = create_access_token(
                identity=username,
                additional_claims={
                    "role":v["role"]
                }
                )
            return jsonify(access_token=access_token)
    return jsonify({"msg": "Bad username or password"})

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

@app.route('/admin-only')
@jwt_required()
def admin_only():
    claims = get_jwt()
    if claims["role"] == "admin":
        return "Admin Access: Granted"
    
    return "admin only"

if __name__ == '__main__':
    app.run()