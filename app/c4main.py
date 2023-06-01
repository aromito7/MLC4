import numpy
import random
#from graphics import *

class Player:
	player_types = ["AI", "NN", "PL"]
	player_type = None

	def __init__(self, player_type = "AI"):
		self.player_type = player_type

	def decide(self, board, player_number):
		if self.player_type == "AI":
			return self.ai_decide(board, player_number)
		if self.player_type == "PL":
			p = board.win.getMouse()
			x, y = int(p.x), int(p.y)
			#print(x,y, board.tile, x // board.tile)
			return int(x // board.tile) + 1

	def check_for_immediate_win(self, board, player_number):  #This only returns the first column which can immediately win the game
		max_chains = [-1,0,0,0,0,0,0,0,-1]
		for a in range(1,8):
			max_chains[a] = board.check_all_chains_with_expansion([a, board.available[a]], player_number)

		for a in range(1,8):			#First priority is winning immediately
			if max_chains[a] > 3: return a
		return -1

	def check_if_opponent_has_win(self, board, player_number):
		opp_chains = [-1,0,0,0,0,0,0,0,-1]
		for a in range(1,8):
			opp_chains[a] = board.check_all_chains_with_expansion([a, board.available[a]], 3-player_number)

		for a in range(1,8):				#Second priority is preventing opponent from winning
			if opp_chains[a] > 3: return a
		return -1

	def check_which_move_gives_opponent_win(self, board, player_number):
		moves = []
		opp_next = [-1,0,0,0,0,0,0,0,-1]
		for a in range(1,8):
			if board.available[a] < 7:
				opp_next[a] = board.check_all_chains_with_expansion([a, board.available[a] + 1], 3-player_number)
				if opp_next[a] > 3:
					moves.append(a)

		return moves

	def ai_decide(self, board, player_number):
		move = self.check_for_immediate_win(board, player_number)
		if move > 0: return move

		move = self.check_if_opponent_has_win(board, player_number)
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
			move[1] = board.check_all_chains_with_expansion([x, board.available[x]], player_number)
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



class Board:
	def __init__(self, tile = 50):
		self.available = [7,1,1,1,1,1,1,1,7]
		self.previous = [None, None]
		self.victory = 0
		self.tile = tile
		self.width = tile*7
		self.height = tile*6

		rows = [[0 for y in range(8)] for x in range(9)]
		for x in range(9):
			for y in range(8):
				if x%8 == 0 or y%7 == 0:
					rows[x][y] = -1


		self.rows = rows

	def start(self):
		win = GraphWin('Connect 4', 350, 300)
		self.win = win
		rows = self.rows

		background = Rectangle(Point(0, 0), Point(350, 300))
		background.setFill('yellow')
		background.draw(win)
		colors = ['white', 'red', 'black']
		for x in range(1, 8):
			for y in range(1, 7):
				t = self.tile
				circle = Circle(Point(-t//2 + x*t, (6.5 * t) - y*t), .4*t)
				circle.setFill(colors[rows[x][y]])
				circle.draw(win)
		win.getMouse()

	def update(self, move):
		if not hasattr(self, 'win'):
			self.start()
			return

		rows = self.rows
		win = self.win

		x = move
		y = self.available[move]-1
		colors = ['white', 'red', 'black']
		t = self.tile
		circle = Circle(Point(-t//2 + x*t, (6.5 * t) - y*t), .4*t)
		circle.setFill(colors[rows[x][y]])
		circle.draw(win)

		#win.getMouse()

	def __str__(self):
		self.update(self.previous[0])

		self.win.close()
		return("Board being displayed")

	def place(self, x, player):
		if self.available[x] > 6:
			print("Player: {} can't place in column {} due to height.".format(player, x))
			self.win.getMouse()
			x = 1/0
			return
		self.previous = [x, self.available[x]]
		self.rows[x][self.available[x]] = player
		self.available[x]+=1


		if self.is_victory():
			self.victory = player

		return self

	def is_victory(self):
		rows = self.rows

		if self.is_horizontal_victory() or self.is_vertical_victory() or self.is_diagonal_downward_victory() or self.is_diagonal_upward_victory():
			return True

		return False

	def check_all_chains_with_expansion(self, start, player):
		hori = self.check_maximum_chains(start, 1, 0, player)
		vert = self.check_maximum_chains(start, 0, 1, player)
		diup = self.check_maximum_chains(start, 1, 1, player)
		dido = self.check_maximum_chains(start, 1,-1, player)

		chains = [hori, vert, diup, dido]

		for chain in chains:
			if chain[0] + chain[1] < 4:
				chain[0] = 0

		max_chain = max(hori[0], vert[0], diup[0], dido[0])

		return max_chain

	def check_all_chains(self, start, player):
		hori = self.check_maximum_chains(start, 1, 0, player)
		vert = self.check_maximum_chains(start, 0, 1, player)
		diup = self.check_maximum_chains(start, 1, 1, player)
		dido = self.check_maximum_chains(start, 1,-1, player)

		max_chain = max(hori[0], vert[0], diup[0], dido[0])

		return max_chain

	def check_maximum_chains(self, start, dx, dy, player):
		count = 1
		expand = 0
		x = start[0]
		y =  start[1]

		if y > 6: return [0,0]

		temp = 1
		while self.rows[x-temp*dx][y-temp*dy] == player:
			temp+=1
			count+=1

		while self.rows[x-temp*dx][y-temp*dy] == 0:
			temp+=1
			expand+=1

		temp = 1
		while self.rows[x+temp*dx][y+temp*dy] == player:
			count+=1
			temp+=1

		while self.rows[x+temp*dx][y+temp*dy] == 0:
			temp+=1
			expand+=1

		return [count, expand]

	def is_horizontal_victory(self):
		count = self.check_maximum_chains(self.previous, 1, 0, self.rows[self.previous[0]][self.previous[1]])[0]
		if count > 3:
			return True
		return False

	def is_vertical_victory(self):
		count = self.check_maximum_chains(self.previous, 0, 1, self.rows[self.previous[0]][self.previous[1]])[0]
		if count > 3:
			return True
		return False

	def is_diagonal_downward_victory(self):
		count = self.check_maximum_chains(self.previous, -1, 1, self.rows[self.previous[0]][self.previous[1]])[0]
		if count > 3:
			return True
		return False

	def is_diagonal_upward_victory(self):
		count = self.check_maximum_chains(self.previous, 1, 1, self.rows[self.previous[0]][self.previous[1]])[0]
		if count > 3:
			return True
		return False

class Game:
	players = [None, None]
	def __init__(self, p0, p1):
		self.players = [p0, p1]
		self.board = Board()
		self.game_over = False
		self.current_player = 1
		self.turns = 0

	def menu(self):
		width, height = self.board.width, self.board.height
		win = GraphWin('C4 Menu', width, height)
		self.win = win
		buttons = 3

		background = Rectangle(Point(0, 0), Point(width, height))
		background.setFill('White')
		background.draw(win)

		left_button = Rectangle(Point(0, 2*height//3), Point(width//buttons, height))
		left_button.setFill('White')
		left_button.draw(win)
		left_button_text = Text(Point(width//6, (height*5)//6), 'Play Basic AI')
		left_button_text.setTextColor("Black")
		left_button_text.setSize(12)
		left_button_text.draw(win)

		right_button = Rectangle(Point(width//buttons, 2*height//3), Point(2*width//buttons, height))
		right_button.setFill('White')
		right_button.draw(win)
		right_button_text = Text(Point((width)//2, (height*5)//6), 'Neural Network')
		right_button_text.setTextColor("Black")
		right_button_text.setSize(12)
		right_button_text.draw(win)

		exit_button = Rectangle(Point(2*width//buttons, 2*height//3), Point(width, height))
		exit_button.setFill('White')
		exit_button.draw(win)
		exit_button_text = Text(Point(5*width//6, 5*height//6), 'Exit')
		exit_button_text.setTextColor("Black")
		exit_button_text.setSize(12)
		exit_button_text.draw(win)

		label = Text(Point(width//2, height//3), 'Connect Four')
		label.setTextColor("Red")
		label.setSize(36)
		label.draw(win)
		stay_on_menu = True
		while stay_on_menu:
			click = win.getMouse()
			x, y = click.x, click.y
			if y > height//2 and x < width//3:
				p1 = Player()
				p2 = Player("PL")
				game = Game(p1,p2)
				game.start()

				stay_on_menu = True
			if y > height//2 and x > 2 * width//3:
				stay_on_menu = False
				win.close()





	def start(self):
		while self.board.victory == 0:
			move = self.players[self.current_player-1].decide(self.board, self.current_player)
			self.board.place(move, self.current_player)
			self.board.update(move)
			self.current_player = 3 - self.current_player
			self.turns += 1
			#print(self.turns)
		print("Player: " + str(self.board.victory) + " wins!")
		self.board.win.getMouse()
		self.board.win.close()


def main():

	p1 = Player()
	p2 = Player("PL")

	game = Game(p1,p2)
	game.menu()

if __name__ == '__main__':
	main()
