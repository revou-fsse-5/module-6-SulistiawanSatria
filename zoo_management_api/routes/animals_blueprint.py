from flask import Blueprint, request, jsonify
import json
import os
import logging

animals_blueprint = Blueprint('animals', __name__)
logger = logging.getLogger(__name__)

# Pastikan path ke db.json benar
DB_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'db.json')

def read_db():
    if not os.path.exists(DB_FILE):
        logger.warning(f"DB file not found: {DB_FILE}")
        return {"animals": [], "employees": []}
    with open(DB_FILE, 'r') as f:
        data = json.load(f)
        logger.info(f"Read data from DB: {data}")
        return data

def write_db(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@animals_blueprint.route('/animals', methods=['GET'])
def get_animals():
    db = read_db()
    return jsonify(db.get('animals', [])), 200

@animals_blueprint.route('/animals/<int:id>', methods=['GET'])
def get_animal(id):
    db = read_db()
    animal = next((a for a in db['animals'] if a['id'] == id), None)
    if not animal:
        return jsonify({"message": "Hewan tidak ditemukan"}), 404
    return jsonify(animal), 200

@animals_blueprint.route('/animals', methods=['POST'])
def add_animal():
    db = read_db()
    data = request.get_json()
    new_id = max([a['id'] for a in db['animals']] + [0]) + 1
    new_animal = {
        'id': new_id,
        'species': data['species'],
        'name': data['name'],
        'age': data['age'],
        'gender': data['gender'],
        'special_requirements': data['special_requirements']
    }
    db['animals'].append(new_animal)
    write_db(db)
    return jsonify({"message": "Hewan berhasil ditambahkan", "animal": new_animal}), 201

@animals_blueprint.route('/animals/<int:id>', methods=['PUT'])
def update_animal(id):
    db = read_db()
    animal = next((a for a in db['animals'] if a['id'] == id), None)
    if not animal:
        return jsonify({"message": "Hewan tidak ditemukan"}), 404
    data = request.get_json()
    animal.update(data)
    write_db(db)
    return jsonify({"message": "Hewan berhasil diperbarui", "animal": animal}), 200

@animals_blueprint.route('/animals/<int:id>', methods=['DELETE'])
def delete_animal(id):
    db = read_db()
    animal = next((a for a in db['animals'] if a['id'] == id), None)
    if not animal:
        return jsonify({"message": "Hewan tidak ditemukan"}), 404
    db['animals'] = [a for a in db['animals'] if a['id'] != id]
    write_db(db)
    return jsonify({"message": "Hewan berhasil dihapus"}), 200
