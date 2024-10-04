from flask import Blueprint, request, jsonify
import json

employees_blueprint = Blueprint('employees', __name__)

def read_db():
    try:
        with open('db.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"animals": [], "employees": []}

def write_db(data):
    with open('db.json', 'w') as f:
        json.dump(data, f, indent=2)

class Employee:
    def __init__(self, id, name, email, phone, role, schedule):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.role = role
        self.schedule = schedule

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'role': self.role,
            'schedule': self.schedule
        }

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
    new_employee = Employee(new_id, data['name'], data['email'], data['phone'], data['role'], data['schedule'])
    db['employees'].append(new_employee.to_dict())
    write_db(db)
    return jsonify({"message": "Karyawan berhasil ditambahkan"}), 201

@employees_blueprint.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    db = read_db()
    employee = next((e for e in db['employees'] if e['id'] == id), None)
    if not employee:
        return jsonify({"message": "Karyawan tidak ditemukan"}), 404
    data = request.get_json()
    employee.update(data)
    write_db(db)
    return jsonify({"message": "Data karyawan berhasil diperbarui"}), 200

@employees_blueprint.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    db = read_db()
    db['employees'] = [e for e in db['employees'] if e['id'] != id]
    write_db(db)
    return jsonify({"message": "Data karyawan berhasil dihapus"}), 200
