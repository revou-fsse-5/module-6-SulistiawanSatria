from flask import Blueprint, request, jsonify

employees_blueprint = Blueprint('employees', __name__)

# In-memory storage for employees
employees = []

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
    return jsonify([employee.to_dict() for employee in employees]), 200

@employees_blueprint.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    employee = next((e for e in employees if e.id == id), None)
    if not employee:
        return jsonify({"message": "Karyawan tidak ditemukan"}), 404
    return jsonify(employee.to_dict()), 200

@employees_blueprint.route('/employees', methods=['POST'])
def add_employee():
    data = request.get_json()
    new_id = len(employees) + 1
    new_employee = Employee(new_id, data['name'], data['email'], data['phone'], data['role'], data['schedule'])
    employees.append(new_employee)
    return jsonify({"message": "Karyawan berhasil ditambahkan"}), 201

@employees_blueprint.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    employee = next((e for e in employees if e.id == id), None)
    if not employee:
        return jsonify({"message": "Karyawan tidak ditemukan"}), 404
    data = request.get_json()
    for key, value in data.items():
        setattr(employee, key, value)
    return jsonify({"message": "Data karyawan berhasil diperbarui"}), 200

@employees_blueprint.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    global employees
    employee = next((e for e in employees if e.id == id), None)
    if not employee:
        return jsonify({"message": "Karyawan tidak ditemukan"}), 404
    employees = [e for e in employees if e.id != id]
    return jsonify({"message": "Data karyawan berhasil dihapus"}), 200
