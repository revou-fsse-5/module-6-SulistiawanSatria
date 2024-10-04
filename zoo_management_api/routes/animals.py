from flask import Blueprint, request, jsonify

animals_blueprint = Blueprint('animals', __name__)

# In-memory storage for animals
animals = []

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
    return jsonify([animal.to_dict() for animal in animals]), 200

@animals_blueprint.route('/animals/<int:id>', methods=['GET'])
def get_animal(id):
    animal = next((a for a in animals if a.id == id), None)
    if not animal:
        return jsonify({"message": "Hewan tidak ditemukan"}), 404
    return jsonify(animal.to_dict()), 200

@animals_blueprint.route('/animals', methods=['POST'])
def add_animal():
    data = request.get_json()
    new_id = len(animals) + 1
    new_animal = Animal(new_id, data['species'], data['age'], data['gender'], data['special_requirements'])
    animals.append(new_animal)
    return jsonify({"message": "Hewan berhasil ditambahkan"}), 201

@animals_blueprint.route('/animals/<int:id>', methods=['PUT'])
def update_animal(id):
    animal = next((a for a in animals if a.id == id), None)
    if not animal:
        return jsonify({"message": "Hewan tidak ditemukan"}), 404
    data = request.get_json()
    for key, value in data.items():
        setattr(animal, key, value)
    return jsonify({"message": "Hewan berhasil diperbarui"}), 200

@animals_blueprint.route('/animals/<int:id>', methods=['DELETE'])
def delete_animal(id):
    global animals
    animal = next((a for a in animals if a.id == id), None)
    if not animal:
        return jsonify({"message": "Hewan tidak ditemukan"}), 404
    animals = [a for a in animals if a.id != id]
    return jsonify({"message": "Hewan berhasil dihapus"}), 200
