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
