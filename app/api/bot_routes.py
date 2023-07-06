from flask import Blueprint, jsonify, session, request
from app.models import User, db
from flask_login import current_user, login_user, logout_user, login_required
from app.c4 import Board
import numpy as np

bot_routes = Blueprint('bot', __name__)



@bot_routes.route('/ai/decide', methods=['POST'])
def authenticate():
    """
    Authenticates a user.
    """
    a = np.arange(6)
    a2 = a[np.newaxis, :]
    board = Board()
    print(request.get_json())
    return {'message' : 'successful request',
            'numpy': a2.shape}
