# zoo_management_api/auth/register.py

from flask import Blueprint, request, jsonify
from db import users



register_blueprint = Blueprint('register', __name__)

@register_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users:
        return jsonify({"message": "User already exists"}), 400

    users[username] = {
        "password": password,
        "full_name": data.get("full_name", "")
    }

    return jsonify({"message": f"User {username} successfully registered"}), 201
