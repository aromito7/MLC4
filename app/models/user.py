from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

default_image = 'https://www.computerhope.com/jargon/g/guest-user.png'

# follows = db.Table(
#     "follows",
#     db.Model.metadata,
#     db.Column('follower', db.Integer, db.ForeignKey(
#         add_prefix_for_prod('users.id')), primary_key=True),
#     db.Column('followed', db.Integer, db.ForeignKey(
#         add_prefix_for_prod('users.id')), primary_key=True)
# )

# likes = db.Table(
#     'likes',
#     db.Model.metadata,
#     db.Column('user_id', db.Integer, db.ForeignKey(
#         add_prefix_for_prod('users.id')), primary_key=True),
#     db.Column('post_id', db.Integer, db.ForeignKey(
#         add_prefix_for_prod('posts.id')), primary_key=True)
# )

# if environment == 'production':
#     connections.schema = SCHEMA
#     follows.schema = SCHEMA
#     likes.schema = SCHEMA

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    profile_picture = db.Column(db.Text, default=default_image)
    active = db.Column(db.Boolean, default=True)
    theme = db.Column(db.String(255), default='light')
    createdAt = db.Column(db.DateTime, default=datetime.now())
    updatedAt = db.Column(db.DateTime, default=datetime.now())

    # posts = db.relationship("Post", back_populates="user")
    # images = db.relationship("UserImage")
    
    # followers = db.relationship(
    #     "User",
    #     secondary="follows",
    #     primaryjoin=follows.c.followed == id,
    #     secondaryjoin=follows.c.follower == id,
    #     backref="following"
    # )
    
    # liked_posts = db.relationship(
    #     "Post",
    #     secondary="likes",
    #     back_populates="user_likes"
    # )


    @property
    def password(self):
        """
        Returns the users hashed password
        """
        return self.hashed_password

    @password.setter
    def password(self, password):
        """
        Sets the users password to the hashed version of the password.
        """
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        """
        Checks the input password to the users hashed password in the database.
        Returns true or false
        """
        return check_password_hash(self.password, password)

    def to_dict(self):
        """
        Returns the user instance data in a dictionary
        """
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'profile_picture': self.profile_picture,
            'active': self.active,
            'theme': self.theme,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt
        }
