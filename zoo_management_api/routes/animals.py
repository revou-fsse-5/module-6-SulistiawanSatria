from flask import Blueprint, request, jsonify

animals_blueprint = Blueprint('animals', __name__)

# In-memory storage for animals with initial data
animals = [
    {
        'id': 1,
        'species': 'Lion',
        'name': 'Simba',
        'age': 5,
        'gender': 'Male',
        'special_requirements': 'Carnivore diet, large enclosure'
    },
    {
        'id': 2,
        'species': 'Elephant',
        'name': 'Dumbo',
        'age': 10,
        'gender': 'Male',
        'special_requirements': 'Daily baths, social interaction'
    }
]

@animals_blueprint.route('/animals', methods=['GET'])
def get_animals():
    
    logger.info("Entering get_animals function")
    return jsonify(animals), 200

@animals_blueprint.route('/animals/<int:id>', methods=['GET'])
def get_animal(id):
    animal = next((a for a in animals if a['id'] == id), None)
    if not animal:
        return jsonify({"message": "Hewan tidak ditemukan"}), 404
    return jsonify(animal), 200

@animals_blueprint.route('/animals', methods=['POST'])
def add_animal():
    data = request.get_json()
    new_id = max(a['id'] for a in animals) + 1 if animals else 1
    new_animal = {
        'id': new_id,
        'species': data['species'],
        'name': data['name'],
        'age': data['age'],
        'gender': data['gender'],
        'special_requirements': data['special_requirements']
    }
    animals.append(new_animal)
    return jsonify({"message": "Hewan berhasil ditambahkan", "animal": new_animal}), 201

@animals_blueprint.route('/animals/<int:id>', methods=['PUT'])
def update_animal(id):
    animal = next((a for a in animals if a['id'] == id), None)
    if not animal:
        return jsonify({"message": "Hewan tidak ditemukan"}), 404
    data = request.get_json()
    animal.update(data)
    return jsonify({"message": "Hewan berhasil diperbarui", "animal": animal}), 200

@animals_blueprint.route('/animals/<int:id>', methods=['DELETE'])
def delete_animal(id):
    global animals
    animal = next((a for a in animals if a['id'] == id), None)
    if not animal:
        return jsonify({"message": "Hewan tidak ditemukan"}), 404
    animals = [a for a in animals if a['id'] != id]
    return jsonify({"message": "Hewan berhasil dihapus"}), 200
