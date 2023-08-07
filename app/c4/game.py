from .player import Player
from .board import Board

class Game:
	players = [None, None]
	def __init__(self, p0, p1):
		self.players = [p0, p1]
		self.board = Board()

	def restart(self):
		self.board.reset()
		self.game_over = False
		self.current_player = 1
		self.turns = 0
		self.messages = []

	# def menu(self):
	# 	width, height = self.board.width, self.board.height
	# 	win = GraphWin('C4 Menu', width, height)
	# 	self.win = win
	# 	buttons = 3

	# 	background = Rectangle(Point(0, 0), Point(width, height))
	# 	background.setFill('White')
	# 	background.draw(win)

	# 	left_button = Rectangle(Point(0, 2*height//3), Point(width//buttons, height))
	# 	left_button.setFill('White')
	# 	left_button.draw(win)
	# 	left_button_text = Text(Point(width//6, (height*5)//6), 'Play Basic AI')
	# 	left_button_text.setTextColor("Black")
	# 	left_button_text.setSize(12)
	# 	left_button_text.draw(win)

	# 	right_button = Rectangle(Point(width//buttons, 2*height//3), Point(2*width//buttons, height))
	# 	right_button.setFill('White')
	# 	right_button.draw(win)
	# 	right_button_text = Text(Point((width)//2, (height*5)//6), 'Neural Network')
	# 	right_button_text.setTextColor("Black")
	# 	right_button_text.setSize(12)
	# 	right_button_text.draw(win)

	# 	exit_button = Rectangle(Point(2*width//buttons, 2*height//3), Point(width, height))
	# 	exit_button.setFill('White')
	# 	exit_button.draw(win)
	# 	exit_button_text = Text(Point(5*width//6, 5*height//6), 'Exit')
	# 	exit_button_text.setTextColor("Black")
	# 	exit_button_text.setSize(12)
	# 	exit_button_text.draw(win)

	# 	label = Text(Point(width//2, height//3), 'Connect Four')
	# 	label.setTextColor("Red")
	# 	label.setSize(36)
	# 	label.draw(win)
	# 	stay_on_menu = True
	# 	while stay_on_menu:
	# 		click = win.getMouse()
	# 		x, y = click.x, click.y
	# 		if y > height//2 and x < width//3:
	# 			p1 = Player()
	# 			p2 = Player("PL")
	# 			game = Game(p1,p2)
	# 			game.start()

	# 			stay_on_menu = True
	# 		if y > height//2 and x > 2 * width//3:
	# 			stay_on_menu = False
	# 			win.close()


	def play_games(self, games, verbose = False):
		for _ in range(games):
			self.start(verbose)

	def generate_training_data(self):
		pass


	def start(self, verbose = False):
		self.restart()
		while self.board.victory == 0 and sum(self.board.available) > 0:
			move = self.players[self.current_player - 1].decide(self.board, self.current_player)
			self.board.place(move, self.current_player)
			self.board.update(move)
			self.current_player = 3 - self.current_player
			self.turns += 1
			self.board.messages = []
			#print(self.turns)

		if not verbose:
			return

		if self.board.victory:
			print(f"Player: {str(self.board.victory)} wins!")
		else:
			print("Game is a draw :-/")
		print(self.board)

		# self.board.win.getMouse()
		# self.board.win.close()
