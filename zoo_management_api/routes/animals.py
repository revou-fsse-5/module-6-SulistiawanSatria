from flask import Blueprint, request, jsonify
from db_handler import load_db, save_db, get_next_id

animals_blueprint = Blueprint('animals', __name__)

@animals_blueprint.route('/animals', methods=['GET'])
def get_animals():
    db = load_db()
    return jsonify(db['animals']), 200

@animals_blueprint.route('/animals/<int:id>', methods=['GET'])
def get_animal(id):
    db = load_db()
    animal = next((a for a in db['animals'] if a['id'] == id), None)
    if not animal:
        return jsonify({"message": "Hewan tidak ditemukan"}), 404
    return jsonify(animal), 200

@animals_blueprint.route('/animals', methods=['POST'])
def add_animal():
    db = load_db()
    data = request.get_json()
    new_id = get_next_id(db['animals'])
    new_animal = {
        'id': new_id,
        'species': data['species'],
        'age': data['age'],
        'gender': data['gender'],
        'special_requirements': data['special_requirements']
    }
    db['animals'].append(new_animal)
    save_db(db)
    return jsonify({"message": "Hewan berhasil ditambahkan", "id": new_id}), 201

@animals_blueprint.route('/animals/<int:id>', methods=['PUT'])
def update_animal(id):
    db = load_db()
    animal = next((a for a in db['animals'] if a['id'] == id), None)
    if not animal:
        return jsonify({"message": "Hewan tidak ditemukan"}), 404
    data = request.get_json()
    animal.update(data)
    save_db(db)
    return jsonify({"message": "Hewan berhasil diperbarui"}), 200

@animals_blueprint.route('/animals/<int:id>', methods=['DELETE'])
def delete_animal(id):
    db = load_db()
    db['animals'] = [a for a in db['animals'] if a['id'] != id]
    save_db(db)
    return jsonify({"message": "Hewan berhasil dihapus"}), 200
