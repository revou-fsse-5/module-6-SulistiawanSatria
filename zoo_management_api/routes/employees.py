from flask import Blueprint, request, jsonify

employees_blueprint = Blueprint('employees', __name__)

# In-memory storage for employees with initial data
employees = [
    {
        'id': 1,
        'name': 'John Doe',
        'email': 'john.doe@zoo.com',
        'phone': '123-456-7890',
        'role': 'Zookeeper',
        'schedule': 'Monday to Friday, 8 AM - 4 PM'
    },
    {
        'id': 2,
        'name': 'Jane Smith',
        'email': 'jane.smith@zoo.com',
        'phone': '098-765-4321',
        'role': 'Veterinarian',
        'schedule': 'Tuesday to Saturday, 9 AM - 5 PM'
    }
]

@employees_blueprint.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees), 200

@employees_blueprint.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    employee = next((e for e in employees if e['id'] == id), None)
    if not employee:
        return jsonify({"message": "Karyawan tidak ditemukan"}), 404
    return jsonify(employee), 200

@employees_blueprint.route('/employees', methods=['POST'])
def add_employee():
    data = request.get_json()
    new_id = max(e['id'] for e in employees) + 1 if employees else 1
    new_employee = {
        'id': new_id,
        'name': data['name'],
        'email': data['email'],
        'phone': data['phone'],
        'role': data['role'],
        'schedule': data['schedule']
    }
    employees.append(new_employee)
    return jsonify({"message": "Karyawan berhasil ditambahkan", "employee": new_employee}), 201

@employees_blueprint.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    employee = next((e for e in employees if e['id'] == id), None)
    if not employee:
        return jsonify({"message": "Karyawan tidak ditemukan"}), 404
    data = request.get_json()
    employee.update(data)
    return jsonify({"message": "Data karyawan berhasil diperbarui", "employee": employee}), 200

@employees_blueprint.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    global employees
    employee = next((e for e in employees if e['id'] == id), None)
    if not employee:
        return jsonify({"message": "Karyawan tidak ditemukan"}), 404
    employees = [e for e in employees if e['id'] != id]
    return jsonify({"message": "Data karyawan berhasil dihapus"}), 200
