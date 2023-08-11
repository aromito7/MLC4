from c4 import Board
from c4 import Player
from c4 import Game
import json
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam


def generate_training_data(self, games, verbose = False):
    '''This function plays a set number of games, and returns
    the results in a format suitable for tensorflow.  Each space on the
    6x7 board contains an element in [-1, 0, 1] where 1 is the current users,
    0 is an empty space, and -1 is the opponent.  This matrix is flattened
    into one dimension and the resulting game winner (or 0 for a draw) is appended
    to the end so that each game result is represented by a 1x43 array.'''
    game_boards = []
    # results = []

    for _ in range(games):
        self.start()
        game_boards.append(self.board.flatten_game_board_state())
        # results.append(self.board.victory)

    # if verbose:
    # 	for game, result in zip(game_boards, results):
    # 		print(result)
    # 		print(game)



    return game_boards #, results

def store_training_data(game_boards):
    with open('game_data.csv', 'a') as f:
        for result in game_boards:
            f.write(json.dumps(result.tolist()) + "\n")

def train():
    p1 = Player("AI")
    p2 = Player("AI")
    game = Game(p1, p2)

    game_results = game.generate_training_data(5)

    store_training_data(game_results)

    def build_model(states, actions):
        model = Sequential()
        model.add(Flatten(input_shape=(1, 42)))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(1, activation='linear'))
        return model

    x_train, y_train = [], []

    for result in game_results:
        x_train.append(result[:-1])
        y_train.append(result[-1])

    model = build_model(x_train, y_train)
    prediction = model.predict([[[1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 2, 2, 0, 1, 1, 0, 0, 2, 1, 2, 2, 2, 0, 0, 2, 1, 1, 2, 2, 2, 0, 1, 1, 1, 2, 2, 2, 1]]])

    return prediction

if __name__ == '__main__':
    print(train())
