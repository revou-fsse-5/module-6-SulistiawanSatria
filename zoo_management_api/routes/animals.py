from flask import Blueprint, request, jsonify
import json

animals_blueprint = Blueprint('animals', __name__)

def read_db():
    try:
        with open('db.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"animals": [], "employees": []}

def write_db(data):
    with open('db.json', 'w') as f:
        json.dump(data, f, indent=2)

class Animal:
    def __init__(self, id, species, age, gender, special_requirements):
        self.id = id
        self.species = species
        self.age = age
        self.gender = gender
        self.special_requirements = special_requirements

    def to_dict(self):
        return {
            'id': self.id,
            'species': self.species,
            'age': self.age,
            'gender': self.gender,
            'special_requirements': self.special_requirements
        }

@animals_blueprint.route('/animals', methods=['GET'])
def get_animals():
    db = read_db()
    return jsonify(db['animals']), 200

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
    new_animal = Animal(new_id, data['species'], data['age'], data['gender'], data['special_requirements'])
    db['animals'].append(new_animal.to_dict())
    write_db(db)
    return jsonify({"message": "Hewan berhasil ditambahkan"}), 201

@animals_blueprint.route('/animals/<int:id>', methods=['PUT'])
def update_animal(id):
    db = read_db()
    animal = next((a for a in db['animals'] if a['id'] == id), None)
    if not animal:
        return jsonify({"message": "Hewan tidak ditemukan"}), 404
    data = request.get_json()
    animal.update(data)
    write_db(db)
    return jsonify({"message": "Hewan berhasil diperbarui"}), 200

@animals_blueprint.route('/animals/<int:id>', methods=['DELETE'])
def delete_animal(id):
    db = read_db()
    db['animals'] = [a for a in db['animals'] if a['id'] != id]
    write_db(db)
    return jsonify({"message": "Hewan berhasil dihapus"}), 200
