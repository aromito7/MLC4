from flask import Blueprint, jsonify, session, request
from app.models import db
from app.c4 import Board
from app.c4 import Player
import numpy as np

bot_routes = Blueprint('bot', __name__)



@bot_routes.route('/ai/decide', methods=['POST'])
def authenticate():
    """
    Authenticates a user.
    """
    json = request.get_json()
    active = np.full((9), -1)
    active[1:8] = np.array(json['active']) + np.full((7), 1)


    board = Board(json['board'], active)
    player = Player()
    move = player.decide(board, 2)
    return {'message' : 'successful request ',
            'move': move}
