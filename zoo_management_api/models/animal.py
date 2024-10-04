from zoo_management_api.db import users

class Animal:
    def __init__(self, id, species, age, gender, special_requirements):
        self.id = id
        self.species = species
        self.age = age
        self.gender = gender
        self.special_requirements = special_requirements
        
# You can then create a list to store animal instances
animals = []


def to_dict(self):
        return {
            'id': self.id,
            'species': self.species,
            'age': self.age,
            'gender': self.gender,
            'special_requirements': self.special_requirements
        }
