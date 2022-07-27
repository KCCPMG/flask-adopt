from tabnanny import check
from models import Pet, db

db.drop_all()
db.create_all()


scruffy = Pet(name="Scruffy", species="dog", photo_url="http://lh3.googleusercontent.com/-yVi5X-zk778/VjJKfhTg1dI/AAAAAAAADi4/acQRf3cbDvw/s1600/Screenshot_2015-10-29-11-22-42.jpg", age=9, notes="""Scruffy is technically available, but he's very busy.""", available=False)
bongo = Pet(name="Bongo", species="bear", photo_url="http://img1.wikia.nocookie.net/__cb20120423165811/disney/images/thumb/2/29/Fun-disneyscreencaps_com-646.jpg/185px-Fun-disneyscreencaps_com-646.jpg", age=3, notes="Fictitious :-(", available=False)
checkers = Pet(name="Checkers", species="cat", photo_url="https://i.pinimg.com/originals/0c/c2/ce/0cc2ce158cce3fc6b737976231eba7fd.jpg", age=0, notes="", available=True)
michelangelo = Pet(name="Michelangelo", species="Turtle", photo_url="https://www.oelmag.com/wp-content/uploads/2020/05/despite-conservation-woes-blandings-turtle-keeps-smiling-1280x640.jpg", age=547, notes="Not a ninja", available=True)
stench_machine = Pet(name="Stench Machine", species="cat", photo_url="https://i.pinimg.com/originals/c9/21/89/c921892a8c263072fe48d7714ac47240.jpg", age=13, notes="", available=True)
david = Pet(name="David", species="dog", photo_url="https://res.cloudinary.com/petrescue/image/upload/v1520218184/gbvbqqvod9iekydwfkhn.jpg", age=7, notes="", available=False)
carol = Pet(name="Carol", species="dog", photo_url="https://res.cloudinary.com/petrescue/image/upload/v1570865922/scfhcqt5esoryynk5f4w.jpg", age=7, notes="", available=False)


for pet in [scruffy, bongo, checkers, michelangelo, stench_machine, david, carol]:
  db.session.add(pet)

db.session.commit()