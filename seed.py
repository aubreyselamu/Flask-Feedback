from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add pets
aubrey = User(username='aubrey.selamu', password="Yohanna_12", email='aubrey.selamu@gmail.com', first_name='Aubrey', last_name='Selamu-Bell')
olani= User(username='olani.selamu', password="shawn", email='olani.selamu@gmail.com', first_name='Olani', last_name='Mendes')
yohanna = User(username='yohanna.selamu', password="oreos", email='yohanna.selamu@gmail.com', first_name='Yohanna', last_name='Selamu')

# Add new objects to session, so they'll persist
db.session.add(aubrey)
db.session.add(olani)
db.session.add(yohanna)

# Commit--otherwise, this never gets saved!
db.session.commit()