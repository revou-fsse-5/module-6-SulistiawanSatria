from flask import Blueprint, request, jsonify
import secrets


login_blueprint = Blueprint('login', __name__)
from db import users



# Token sederhana untuk simulasi autentikasi
tokens = {}

@login_blueprint.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({"message": "Login gagal"}), 401
   
    if auth.username == "admin" and auth.password == "admin":
        token = secrets.token_hex(16)
        tokens[token] = auth.username
        return jsonify({"token": token})
   
    return jsonify({"message": "Login gagal"}), 401

# Fungsi helper untuk verifikasi token
def verify_token(token):
    return token in tokens
