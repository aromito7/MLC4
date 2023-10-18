from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy import ForeignKey
from datetime import datetime
import json

class Game(db.Model):
    __tablename__ = 'games'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    board = db.Column(db.String, nullable=False)


    def to_dict(self):
        return {
            'id': self.id,
            'board': json.dumps(self.board)
        }
