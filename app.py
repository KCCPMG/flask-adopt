from flask import Flask, render_template, redirect, request
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "terces"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# TESTING
app.config['WTF_CSRF_ENABLED'] = False

debug = DebugToolbarExtension(app)

connect_db(app)
db.drop_all()
db.create_all()


from seed import *

@app.route("/", methods=["GET"])
def get_home():

  pets = Pet.query.filter().all()
  return render_template('home.html', pets=pets)



@app.route("/add", methods=["GET", "POST"])
def add_pet():

  form = AddPetForm()
  
  if form.validate_on_submit():
    pet = Pet(name=form['name'].data, species=form['species'].data, photo_url=form['photo_url'].data, age=form['age'].data, notes=form['notes'].data)
    pet.available = form.available.data

    db.session.add(pet)
    db.session.commit()
    return redirect("/")
  
  else:
    return render_template('add.html', form=form)



@app.route("/<int:pet_id_number>", methods = ["GET", "POST"])
def handle_pet(pet_id_number):

  pet = Pet.query.get_or_404(pet_id_number)
  form = AddPetForm(obj=pet)

  if form.validate_on_submit():
    pet.name = form.name.data
    pet.species = form.species.data
    pet.photo_url = form.photo_url.data
    pet.age = form.age.data
    pet.notes = form.notes.data
    pet.available = form.available.data

    db.session.commit()

    return redirect(f"/{pet_id_number}")

  else:
    return render_template("pet_detail_and_edit.html", pet=pet, form=form)