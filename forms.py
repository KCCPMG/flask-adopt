from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
  """Form for adding pets"""

  name = StringField("Pet Name", validators = [InputRequired(message="Please enter a name!")])
  species = SelectField("Species", choices=["", "cat", "dog", "porcupine"])
  photo_url = StringField("Photo URL", validators = [Optional(), URL(message="Please enter a valid URL")])
  age = IntegerField("Age", validators = [Optional(), NumberRange(min=0, max=30)])
  notes = StringField("Notes")
  available = BooleanField("Available", validators=[Optional()])