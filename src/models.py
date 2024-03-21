from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    favorites = db.relationship("Favorite", back_populates="user")

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }


class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    diameter = db.Column(db.Integer)
    climate = db.Column(db.String(50))
    population = db.Column(db.Integer)
    terrain = db.Column(db.String(100))


    favorites = db.relationship("Favorite", backref="planet_favorite")



    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "diameter": self.diameter,
            "climate": self.climate,
            "population": self.population,
            "terrain": self.terrain
        }


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(20))
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    hair_color =db.Column(db.String(50))
    skin_color = db.Column(db.String(50))
    eye_color = db.Column(db.String(50))


    favorites = db.relationship("Favorite", backref="people_favorite")


    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "height": self.height,
            "weight": self.weight,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color
        }


class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    character_id = db.Column(db.Integer, db.ForeignKey('people.id'))

    user = db.relationship("User", back_populates="favorites")  
    planet = db.relationship("Planets")  
    character = db.relationship("People")  

    def __repr__(self):
        return '<Favorite %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet": self.planet,
            "character": self.character
           
        }