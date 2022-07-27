from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def connect_db(app):
  """Connect to database"""
  
  db.app = app
  db.init_app(app)


class Pet(db.Model):
  """A pet that is potentially available for adoption"""

  __tablename__ = "pets"

  def __repr__(self):
    return(f"Pet: \nid: {self.id}, \nname: {self.name} \nspecies: {self.species}, \nphoto_url: {self.photo_url}, \nage: {self.age}, \nnotes: {self.notes}, \navailable: {self.available}")

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String, nullable=False)
  species = db.Column(db.String, nullable=False)
  photo_url = db.Column(db.String, nullable=True)
  age = db.Column(db.Integer, nullable=True)
  notes = db.Column(db.String, nullable=True)
  available = db.Column(db.Boolean, nullable=False, default=True)