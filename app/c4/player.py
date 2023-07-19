import numpy
import random

class Player:
	player_types = ["AI", "NN", "PL"]
	player_type = None

	def __init__(self, player_type = "AI"):
		self.player_type = player_type

	def decide(self, board, player_number):
		'''This this determines how a player decides to move
		based on what type of player they are.'''

		if self.player_type == "AI":
			return self.ai_decide(board, player_number)
		if self.player_type == "PL":
			p = board.win.getMouse()
			x, y = int(p.x), int(p.y)
			#print(x,y, board.tile, x // board.tile)
			return int(x // board.tile) + 1

		return 0


	def check_for_immediate_win(self, board, player_number):
		'''Checks to see if a player has a move that can immediately win
		them the game.  If there are multiple it returns the first column
		number for a winning move.  Otherwise it returns -1.'''

		max_chains = [-1,0,0,0,0,0,0,0,-1]
		for a in range(1,8):
			max_chains[a] = board.check_all_chains_with_expansion([board.available[a], a], player_number)
		print("Player {} chains".format(player_number))
		print(max_chains)
		for a in range(1,8):
			if max_chains[a] > 3: return a
		return -1


	def check_which_move_gives_opponent_win(self, board, player_number):
		'''Checks to see which moves will give your opponent an opportuny
		to win by placing their piece on top of yours and returns an array
		of column numbers.'''

		moves = []
		opp_next = [-1,0,0,0,0,0,0,0,-1]
		for a in range(1,8):
			if board.available[a] < 7:
				opp_next[a] = board.check_all_chains_with_expansion([board.available[a] - 1, a], 3 - player_number)
				if opp_next[a] > 3:
					moves.append(a)

		return moves

	def ai_decide(self, board, player_number):
		'''This allows the basic AI to decide where to move based on a priority
		system.  Immediately win -> prevent opponent win -> exclude moves that give
		a win next turn -> pick a move that maximizes chain length and randomly
		select a move if there's a tie.'''

		print(board)
		print(board.available)
		move = self.check_for_immediate_win(board, player_number)

		if move > 0: return move

		move = self.check_for_immediate_win(board, 3-player_number)

		if move > 0: return move

		bad_moves = self.check_which_move_gives_opponent_win(board, player_number)
		max_height = [i for i in range(1,8) if board.available[i] > 6]
		moves = [i for i in range(1,8) if i not in max_height]
		if len(moves) == 1:
			return moves[0]

		safe_moves = [[i, 0] for i in moves if i not in bad_moves]

		if len(safe_moves) == 0:
			return random.choice(moves)

		moves = safe_moves

		greatest = 0
		greatest_moves = []
		for move in moves:
			x = move[0]
			move[1] = board.check_all_chains_with_expansion([board.available[x], x], player_number)
			if move[1] > greatest:
				greatest = move[1]
				greatest_moves = [x]
			if move[1] == greatest:
				greatest_moves.append(x)

		return random.choice(greatest_moves)

	def ai_decide2(self, board, player_number):
		max_chains = [-1,0,0,0,0,0,0,0,-1]
		opp_chains = [-1,0,0,0,0,0,0,0,-1]
		opp_next = [-1,0,0,0,0,0,0,0,-1]
		for a in range(1,8):
			max_chains[a] = board.check_all_chains_with_expansion([a, board.available[a]], player_number)
			opp_chains[a] = board.check_all_chains_with_expansion([a, board.available[a]], 3-player_number)
			if board.available[a] < 7:
				opp_next[a] = board.check_all_chains_with_expansion([a, board.available[a] + 1], 3-player_number)


		#print(max_chains)
		#print(opp_chains)

		for a in range(1,8):			#First priority is winning immediately
			if max_chains[a] > 3: return a
		for a in range(1,8):				#Second priority is preventing opponent from winning
			if opp_chains[a] > 3: return a
		for a in range(1,8):
			if opp_next[a] > 4: max_chains[a] = -1

		possible_moves = []
		for a in range(len(board.available)):		#Third priority is creating the longest chain possible
			if max_chains[a] == max(max_chains):
				possible_moves.append(a)
		return random.choice(possible_moves)
