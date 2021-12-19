from models import User, Feedback, db
from app import app


#*******************************************************************************************
#User Model
# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()
Feedback.query.delete()

# Add sample Users and Feedback
aubrey = User.register(username='aubrey.selamu', password="Yohanna_12", email='aubrey.selamu@gmail.com', first_name='Aubrey', last_name='Selamu-Bell')
olani= User.register(username='olani.selamu', password="shawn", email='olani.selamu@gmail.com', first_name='Olani', last_name='Mendes')
yohanna = User.register(username='yohanna.selamu', password="oreos", email='yohanna.selamu@gmail.com', first_name='Yohanna', last_name='Selamu')

aubrey_feedback = Feedback(title='My First Review', content='I hope this works!', username='aubrey.selamu')
aubrey_feedback2 = Feedback(title='My Second Review', content='It is working!', username='aubrey.selamu')
olani_feedback = Feedback(title='My First Feedback', content='I am a software engineer!', username='olani.selamu')
yohanno_feedback = Feedback(title='Im going to be great!', content='Great app!', username='yohanna.selamu')

db.session.add_all([aubrey,olani,yohanna,aubrey_feedback, aubrey_feedback2, olani_feedback,yohanno_feedback])
db.session.commit()


