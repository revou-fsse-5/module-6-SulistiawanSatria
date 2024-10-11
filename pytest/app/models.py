from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}

class Feeding(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal_id = db.Column(db.Integer)
    enclosure_id = db.Column(db.Integer)
    food_type = db.Column(db.String(100))
    feeding_time = db.Column(db.DateTime)

    def to_dict(self):
        return {
            "id": self.id,
            "animal_id": self.animal_id,
            "enclosure_id": self.enclosure_id,
            "food_type": self.food_type,
            "feeding_time": self.feeding_time
        }
