from flask import Blueprint, request
from flask_login import login_required
from app.models import db, User
from sqlalchemy import desc, asc
#from app.utils import (upload_file_to_s3, allowed_file, get_unique_filename)

user_routes = Blueprint('users', __name__)

'''
    User_Dictionary = {
        'id': self.id,
        'username': self.username,
        'password': self.password,
        'active': self.active,        # Determine if users profile should be hidden.
        'theme': self.theme,          # User can store which theme they use
        'createdAt': self.createdAt,
        'updatedAt': self.updatedAt
    }
'''

@user_routes.route('/<int:id>', methods=['GET'])
@login_required
def user(id):
    """
    Route to get user by id. GET /api/users/userId
    Route returns user dictionary data.
    """
    user = User.query.get(id)
    return user.to_dict()

@user_routes.route('/<int:id>/theme', methods=['POST'])
@login_required
def update_user_theme(id):
    """
    Route to update user theme in database. POST /api/users/userId/theme
    Expects object: {theme: 'string'}
    Route returns new user dictionary data.
    """
    data = request.get_json()
    theme = data['theme']

    user = User.query.get(id)
    user.theme = theme

    db.session.commit()
    ret = User.query.get(id)

    return ret.to_dict()

@user_routes.route('/<int:id>/picture', methods=['POST'])
@login_required
def update_user_picture(id):
    """
    Route to upload user profile picture. POST /api/users/userId/picture
    Expects: {profile_picture: 'url'}
    Route returns new user dictionary data.
    """
    profile_picture = request.get_json()['profile_picture']

    if not profile_picture:
        return {'errors': ['Failed to get profile picture']}, 400

    user = User.query.get(id)
    user.profile_picture = profile_picture
    db.session.commit()
    ret = User.query.get(id)
    return ret.to_dict()

@user_routes.route('/upload', methods=['POST'])
@login_required
def upload_image():
    """
    Route to upload an image to the S3 Bucket. POST /api/users/upload
    User route is used for login required to upload a file.
    Returns a dictionary: {url: 'S3BucketUrl'}
    """
    if "image" in request.files:
        image = request.files["image"]

    if not allowed_file(image.filename):
        return {"errors": "file type not permitted"}, 400

    image.filename = get_unique_filename(image.filename)

    upload = upload_file_to_s3(image)

    if "url" not in upload:
        return upload, 400

    imageURL = upload["url"]
    return {"url": imageURL}

@user_routes.route('/<int:id>/profile', methods=['DELETE'])
@login_required
def delete_profile(id):
    '''
    Route to delete a users profile. It will set user.active to false or true.
    It will not delete the user.
    You may use user.active to hide the profile and keep their data in the data base.
    Route returns new user dictionary data.
    '''
    user = User.query.get(id)

    if not user:
        return {'errors', ['Unable to find user']}, 400

    user.active = not user.active
    db.session.commit()
    ret = User.query.get(id)
    return ret.to_dict()
