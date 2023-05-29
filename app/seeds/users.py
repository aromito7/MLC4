from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text
# from faker import Faker
# fake = Faker()

default_profile_picture = 'https://www.computerhope.com/jargon/g/guest-user.png'

# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo',
        email='demo@aa.io',
        password='password',
        profile_picture = default_profile_picture
    )

    db.session.add(demo)

    for i in range(20):
        newUser = User(
            username=fake.user_name(),
            email=fake.email(),
            password='password',
            profile_picture= default_profile_picture
        )

        db.session.add(newUser)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
