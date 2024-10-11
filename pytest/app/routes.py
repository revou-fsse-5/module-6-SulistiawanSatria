from flask import Flask, jsonify, request
from supabase import create_client, Client
import os

# Inisialisasi Flask dan Supabase
app = Flask(__name__)

# Inisialisasi Supabase Client
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Create User (Membuat pengguna baru)
@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')

        if not name or not email:
            return jsonify({"error": "Name and email are required"}), 400

        response = supabase.table('users').insert({
            "name": name,
            "email": email
        }).execute()

        return jsonify({"message": "User created successfully", "data": response.data}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get All Users (Mengambil semua pengguna)
@app.route('/get_users', methods=['GET'])
def get_users():
    try:
        response = supabase.table('users').select("*").execute()

        if len(response.data) == 0:
            return jsonify({"message": "No users found"}), 404

        return jsonify(response.data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Update User (Memperbarui data pengguna)
@app.route('/update_user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')

        if not name and not email:
            return jsonify({"error": "Nothing to update"}), 400

        update_data = {}
        if name:
            update_data['name'] = name
        if email:
            update_data['email'] = email

        response = supabase.table('users').update(update_data).eq('id', user_id).execute()

        if len(response.data) == 0:
            return jsonify({"message": "User not found"}), 404

        return jsonify({"message": "User updated successfully", "data": response.data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Delete User (Menghapus pengguna)
@app.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        response = supabase.table('users').delete().eq('id', user_id).execute()

        if len(response.data) == 0:
            return jsonify({"message": "User not found"}), 404

        return jsonify({"message": "User deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Menjalankan Flask app
if __name__ == '__main__':
    app.run(debug=True)
