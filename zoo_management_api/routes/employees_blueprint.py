from flask import Blueprint, request, jsonify
import json
import os

employees_blueprint = Blueprint('employees', __name__)

DB_FILE = 'db.json'

def read_db():
    if not os.path.exists(DB_FILE):
        return {"employees": []}
    with open(DB_FILE, 'r') as f:
        return json.load(f)

def write_db(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@employees_blueprint.route('/employees', methods=['GET'])
def get_employees():
    db = read_db()
    return jsonify(db['employees']), 200

@employees_blueprint.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    db = read_db()
    employee = next((e for e in db['employees'] if e['id'] == id), None)
    if not employee:
        return jsonify({"message": "Karyawan tidak ditemukan"}), 404
    return jsonify(employee), 200

@employees_blueprint.route('/employees', methods=['POST'])
def add_employee():
    db = read_db()
    data = request.get_json()
    new_id = max([e['id'] for e in db['employees']] + [0]) + 1
    new_employee = {
        'id': new_id,
        'name': data['name'],
        'email': data['email'],
        'phone': data['phone'],
        'role': data['role'],
        'schedule': data['schedule']
    }
    db['employees'].append(new_employee)
    write_db(db)
    return jsonify({"message": "Karyawan berhasil ditambahkan", "employee": new_employee}), 201

@employees_blueprint.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    db = read_db()
    employee = next((e for e in db['employees'] if e['id'] == id), None)
    if not employee:
        return jsonify({"message": "Karyawan tidak ditemukan"}), 404
    data = request.get_json()
    employee.update(data)
    write_db(db)
    return jsonify({"message": "Data karyawan berhasil diperbarui", "employee": employee}), 200

@employees_blueprint.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    db = read_db()
    employee = next((e for e in db['employees'] if e['id'] == id), None)
    if not employee:
        return jsonify({"message": "Karyawan tidak ditemukan"}), 404
    db['employees'] = [e for e in db['employees'] if e['id'] != id]
    write_db(db)
    return jsonify({"message": "Data karyawan berhasil dihapus"}), 200
