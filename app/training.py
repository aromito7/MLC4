from c4 import Board
from c4 import Player
from c4 import Game
import json
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam


def flatten_game_board_state(board):
    flat = np.append(board.rows[1:-1, 1:-1].flatten(), board.victory)

    output = np.array([f if f < 2 else -1 for f in flat])

    return output

def expand_board_state(flattened_state):
    '''This expands a 1x43 saved game state into a board.'''

    board, victory = np.array(flattened_state[:-1]), flattened_state[-1]

def generate_training_data(games, verbose = False):
    '''This function plays a set number of games, and returns
    the results in a format suitable for tensorflow.  Each space on the
    6x7 board contains an element in [-1, 0, 1] where 1 is the current users,
    0 is an empty space, and -1 is the opponent.  This matrix is flattened
    into one dimension and the resulting game winner (or 0 for a draw) is appended
    to the end so that each game result is represented by a 1x43 array.'''
    game_boards = []
    # results = []

    p1, p2 = Player(), Player()
    game = Game(p1, p2)

    for _ in range(games):
        game.start()
        game_boards.append(flatten_game_board_state(game.board))
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

    game_results = generate_training_data(1000)

    store_training_data(game_results)

    build_model(game_results)

def build_model(game_results):
    '''This creates our tensorflow model'''
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

    # model.compile(optimizer='adam',
    #           loss=loss_fn,
    #           metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=5)

    return model

def predict(x_test, y_test):
    pass

if __name__ == '__main__':
    print(train())
