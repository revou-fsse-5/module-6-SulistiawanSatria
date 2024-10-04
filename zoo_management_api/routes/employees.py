from flask import Blueprint, request, jsonify
import logging

employees_blueprint = Blueprint('employees', __name__)
logger = logging.getLogger(__name__)

# In-memory storage for employees
employees = [
        {
        'id': 1,
        'name': 'John Doe',
        'email': 'john.doe@zoo.com',
        'phone': '123-456-7890',
        'role': 'Zookeeper',
        'schedule': 'Monday to Friday, 8 AM - 4 PM'
    }
    
        {
        "id": 2,
        "name": "Opong",
        "email": "opong@zoo.com",
        "phone": "123-456-7890",
        "role": "Zookeeper",
        "schedule": "Monday to Friday, 8 AM - 4 PM"
    }
        
                {
        "id": 3,
        "name": "Ujang",
        "email": "Ujang@zoo.com",
        "phone": "123-456-7890",
        "role": "Zookeeper",
        "schedule": "Monday to Friday, 8 AM - 4 PM"
    }
        
        
]


@employees_blueprint.route('/employees', methods=['GET'])
def get_employees():
    logger.info("Fetching all employees")
    return jsonify(employees), 200

@employees_blueprint.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    logger.info(f"Fetching employee with id {id}")
    employee = next((e for e in employees if e['id'] == id), None)
    if not employee:
        logger.warning(f"Employee with id {id} not found")
        return jsonify({"message": "Karyawan tidak ditemukan"}), 404
    return jsonify(employee), 200

@employees_blueprint.route('/employees', methods=['POST'])
def add_employee():
    logger.info("Adding new employee")
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
    logger.info(f"New employee added with id {new_id}")
    return jsonify({"message": "Karyawan berhasil ditambahkan", "employee": new_employee}), 201

@employees_blueprint.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    logger.info(f"Updating employee with id {id}")
    employee = next((e for e in employees if e['id'] == id), None)
    if not employee:
        logger.warning(f"Employee with id {id} not found for update")
        return jsonify({"message": "Karyawan tidak ditemukan"}), 404
    data = request.get_json()
    employee.update(data)
    logger.info(f"Employee with id {id} updated successfully")
    return jsonify({"message": "Data karyawan berhasil diperbarui", "employee": employee}), 200

@employees_blueprint.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    logger.info(f"Deleting employee with id {id}")
    global employees
    employee = next((e for e in employees if e['id'] == id), None)
    if not employee:
        logger.warning(f"Employee with id {id} not found for deletion")
        return jsonify({"message": "Karyawan tidak ditemukan"}), 404
    employees = [e for e in employees if e['id'] != id]
    logger.info(f"Employee with id {id} deleted successfully")
    return jsonify({"message": "Data karyawan berhasil dihapus"}), 200
