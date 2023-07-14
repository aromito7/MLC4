import unittest
import c4 as c4main
import nn
import numpy as np

class TestWinConditions(unittest.TestCase):
	#rows = [[0 for col in range(7)] for row in range(6)]

	def create_test_board_0(self):
		grid = np.array(
			[
			[0, 0, 0, 0, 0, 0, 0],
			[0, 0, 2, 0, 0, 0, 0],
			[0, 0, 1, 1, 0, 0, 0],
			[0, 0, 2, 2, 1, 0, 0],
			[0, 0, 1, 1, 2, 2, 0],
			[0, 0, 1, 2, 2, 2, 1]
			])
		available = [0, 6, 6, 1, 2, 3, 4, 5, 0]
		board = c4main.Board(grid, available)
		#board.place(3, 1).place(4,2).place(5,2).place(6,2).place(7,1).place(3,1).place(4,1).place(5,2).place(6,2).place(3,2).place(4,2).place(5,1).place(3,1).place(4,1).place(3,2)
		return board

	def create_test_board_1(self):
		grid = np.array(
			[
			[0, 0, 0, 0, 0, 0, 0],
			[0, 2, 1, 2, 0, 0, 0],
			[0, 2, 2, 1, 0, 0, 0],
			[0, 2, 2, 1, 1, 1, 0],
			[0, 1, 1, 1, 2, 2, 0],
			[1, 1, 1, 2, 2, 2, 0]
			])
		available = [0, 5, 1, 1, 1, 3, 3, 6, 0]
		board = c4main.Board(grid, available)
		#board.place(1,1).place(2,1).place(3,1).place(4,2).place(5,2).place(6,2).place(2,1).place(3,1).place(4,1).place(5,2).place(6,2).place(2,2).place(3,2).place(4,1).place(5,1).place(6,1).place(2,2).place(3,2).place(4,1).place(2,2).place(3,1).place(4,2)
		return board

	def create_test_board_2(self):
		grid = np.array(
			[
			[0, 0, 0, 0, 0, 0, 0],
			[0, 2, 1, 0, 0, 0, 0],
			[0, 2, 2, 0, 0, 0, 0],
			[0, 2, 2, 1, 1, 0, 0],
			[0, 1, 1, 2, 2, 1, 0],
			[1, 1, 1, 2, 2, 2, 0]
			])
		available = [0, 5, 1, 1, 3, 3, 4, 6, 0]
		board = c4main.Board(grid, available)
		#board.place(1,1).place(2,1).place(3,1).place(4,2).place(5,2).place(6,2).place(2,1).place(3,1).place(4,2).place(5,2).place(2,2).place(3,2).place(4,1).place(5,1).place(6,1).place(2,2).place(3,2).place(2,2).place(3,1)
		return board

	def create_test_game_0(self):
		player = c4main.Player("AI")
		grid = np.array(
			[
			[0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 2, 0, 0],
			[0, 0, 0, 0, 2, 0, 0],
			[0, 1, 1, 1, 2, 0, 0]
			])
		available = [0, 6, 5, 5, 5, 3, 6, 6, 0]
		board = c4main.Board(grid, available)
		#board.place(2,1).place(3,1).place(4,1).place(5,2).place(5,2).place(5,2)
		return board, player

	def create_test_game_1(self):
		player = c4main.Player("AI")
		grid = np.array(
			[
			[0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 2, 0, 0],
			[0, 1, 1, 0, 2, 0, 0]
			])
		available = [0, 6, 5, 5, 6, 4, 6, 6, 0]
		board = c4main.Board(grid, available)
		#board.place(2,1).place(3,1).place(5,2).place(5,2)
		return board, player

	def create_test_chain_1(self):
		player = c4main.Player("AI")
		grid = np.array(
			[
			[0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0],
			[0, 1, 1, 0, 1, 1, 0],
			[1, 1, 1, 1, 1, 1, 1],
			[2, 2, 2, 2, 2, 2, 2],
			[2, 2, 2, 2, 2, 2, 2]
			])
		available = [0, 3, 2, 2, 3, 2, 2, 3, 0]
		board = c4main.Board(grid, available)
		return board, player

	def create_test_chain_2(self):
		player = c4main.Player("AI")
		grid = np.array(
			[
			[0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0],
			[0, 2, 0, 0, 0, 2, 0],
			[2, 2, 2, 2, 2, 2, 2],
			[1, 1, 1, 1, 1, 1, 1],
			[1, 1, 1, 1, 1, 1, 1]
			])
		available = [0, 3, 2, 3, 3, 3, 2, 3, 0]
		board = c4main.Board(grid, available)
		return board, player

	def create_test_chain_3(self):
		player = c4main.Player("AI")
		grid = np.array(
			[
			[0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0],
			[0, 2, 2, 0, 0, 0, 0],
			[2, 2, 2, 2, 2, 2, 2],
			[2, 2, 2, 2, 2, 2, 2],
			[1, 1, 1, 1, 1, 1, 1]
			])
		available = [0, 3, 2, 2, 3, 3, 3, 3, 0]
		board = c4main.Board(grid, available)
		return board, player

	def create_test_chain_4(self):
		player = c4main.Player("AI")
		grid = np.array(
			[
			[0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 2, 2, 2, 0],
			[2, 2, 2, 2, 2, 2, 2],
			[2, 2, 2, 2, 2, 2, 2],
			[2, 2, 2, 2, 2, 2, 2]
			])
		available = [0, 3, 3, 3, 2, 2, 2, 3, 0]
		board = c4main.Board(grid, available)
		return board, player

	def create_test_game_2(self):
		player = c4main.Player("AI")
		grid = np.array(
			[
			[0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 1, 0],
			[0, 2, 2, 2, 1, 2, 2],
			[0, 1, 1, 1, 2, 2, 2]
			])
		available = [0, 6, 4, 4, 4, 4, 3, 4, 0]
		board = c4main.Board(grid, available)
		#board.place(2,1).place(2,2).place(3,1).place(3,2).place(4,1).place(4,2).place(5,2).place(5,1).place(6,2).place(6,2).place(6,1).place(7,2).place(7,2)
		return board, player

	def create_test_game_3(self):
		player = c4main.Player("AI")
		grid = np.array(
			[
			[0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 1],
			[0, 0, 0, 0, 0, 0, 1],
			[1, 0, 0, 1, 2, 2, 2]
			])
		available = [0, 5, 6, 6, 5, 5, 5, 3, 0]
		board = c4main.Board(grid, available)
		return board, player

	def create_test_game_immediate_win_vs_prevent_win(self):
		player = c4main.Player("AI")
		grid = np.array(
			[
			[0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0],
			[1, 0, 0, 0, 0, 0, 0],
			[1, 0, 0, 0, 0, 0, 0],
			[1, 0, 0, 2, 0, 2, 2]
			])
		available = [0, 3, 6, 6, 6, 5, 5, 5, 0]
		board = c4main.Board(grid, available)
		return board, player


	def test_place0(self):
		board = self.create_test_board_0()
		board.place(1, 2)
		self.assertEqual(board.rows[6][1], 2)

	def test_place1(self):
		board = self.create_test_board_0()

		board.place(2, 1)
		self.assertEqual(board.rows[6][2], 1)

	def test_place2(self):
		board = self.create_test_board_0()

		board.place(3, 2)
		#board.check_all_chains([3,6],2)
		self.assertEqual(board.rows[1][3], 2)

	def test_horizontal_victory0(self):
		board = self.create_test_board_1()
		board.place(7, 2)
		#board.is_horizontal_victory() and board.is_victory()
		self.assertTrue(board.is_horizontal_victory())

	def test_horizontal_victory1(self):
		board = self.create_test_board_1()
		board.place(1, 1)

		result = board.is_horizontal_victory()
		self.assertTrue(result)

	def test_vertical_victory0(self):
		board = self.create_test_board_1()
		board.place(2, 2)

		result = board.is_vertical_victory()
		self.assertTrue(result)

	def test_diagonal_downward_victory0(self):
		board = self.create_test_board_1()
		board.place(2, 1)
		result = board.is_diagonal_downward_victory()
		self.assertTrue(result)

	def test_diagonal_upward_victory0(self):
		board = self.create_test_board_1()
		board.place(5, 1)
		result = board.is_diagonal_upward_victory()
		self.assertTrue(result)

	def test_not_victory0(self):
		board = self.create_test_board_1()
		board.place(4, 2)
		result = board.is_victory()
		self.assertFalse(result)

	def test_all_chains0(self):
		board = self.create_test_board_2()
		result = board.check_all_chains([1,2], 1)
		self.assertEqual(result, 2)

	def test_all_chains1(self):
		board = self.create_test_board_2()
		result = board.check_all_chains([3, 4], 2)
		self.assertEqual(result, 3)

	def test_all_chains2(self):
		board = self.create_test_board_2()
		result = board.check_all_chains([6, 7], 1)
		self.assertEqual(result, 3)

	def test_all_chains3(self):
		board = self.create_test_board_2()
		result = board.check_all_chains([4, 6], 1)
		self.assertEqual(result, 3)

	def test_all_chains4(self):
		board = self.create_test_board_2()
		result = board.check_all_chains([4, 6], 2)
		self.assertEqual(result, 3)

	def test_ai_check_win_0(self):
		board, player = self.create_test_game_2()

		move = player.check_for_immediate_win(board, 1)
		self.assertEqual(move, 1)

	def test_ai_check_win_1(self):
		board, player = self.create_test_game_2()

		move = player.check_for_immediate_win(board, 2)
		self.assertEqual(move, -1)

	def test_ai_check_opp_win_0(self):
		board, player = self.create_test_game_2()

		move = player.check_for_immediate_win(board, 2)
		self.assertEqual(move, -1)

	def test_ai_check_opp_win_1(self):
		board, player = self.create_test_game_2()

		move = player.check_for_immediate_win(board, 1)
		self.assertEqual(move, 1)

	def test_ai_check_which_move_gives_opp_win_0(self):
		board, player = self.create_test_game_2()
		board.place(5,2)
		move = player.check_which_move_gives_opponent_win(board, 1)
		self.assertEqual(move, [1,4])

	def test_ai_check_which_move_gives_opp_win_1(self):
		board, player = self.create_test_game_2()

		move = player.check_which_move_gives_opponent_win(board, 2)
		self.assertEqual(move, [7])


	def test_ai_choice_0(self):
		board, player = self.create_test_game_0()

		move = player.decide(board, 1)
		self.assertEqual(move, 1) #player.decide(board, 1) == 1)

	def test_ai_choice_1(self):
		board, player = self.create_test_game_0()

		move = player.decide(board, 2)
		self.assertEqual(move, 5) #player.decide(board, 1) == 1)

	def test_ai_choice_2(self):
		board, player = self.create_test_game_1()

		move = player.decide(board, 2)
		self.assertEqual(move, 5) #player.decide(board, 1) == 1)

	def test_ai_choice_3(self):
		board, player = self.create_test_game_1()

		move = player.decide(board, 2)
		self.assertEqual(move, 5) #player.decide(board, 1) == 1)

	def test_ai_choice_4(self):
		board, player = self.create_test_game_3()

		move = player.decide(board, 2)
		print(move)
		self.assertTrue(3 < move < 7)

	def test_chains_1(self):
		board, player = self.create_test_chain_1()
		player = 2

		self.assertEqual(1, board.check_horizontal_chains([3, 1], 2)[0])
		self.assertEqual(1, board.check_horizontal_chains([3, 4], 2)[0])
		self.assertEqual(1, board.check_horizontal_chains([3, 7], 2)[0])

		self.assertEqual(1, board.check_vertical_chains([3, 1], 2)[0])
		self.assertEqual(1, board.check_vertical_chains([3, 4], 2)[0])
		self.assertEqual(1, board.check_vertical_chains([3, 7], 2)[0])

		self.assertEqual(1, board.check_diagonal_up_chains([3, 1], 2)[0])
		self.assertEqual(1, board.check_diagonal_up_chains([3, 4], 2)[0])
		self.assertEqual(1, board.check_diagonal_up_chains([3, 7], 2)[0])

		self.assertEqual(1, board.check_diagonal_down_chains([3, 1], 2)[0])
		self.assertEqual(1, board.check_diagonal_down_chains([3, 4], 2)[0])
		self.assertEqual(1, board.check_diagonal_down_chains([3, 7], 2)[0])

	def test_chains_2(self):
		board, player = self.create_test_chain_2()
		player = 2

		self.assertEqual(2, board.check_horizontal_chains([3, 1], 2)[0])
		self.assertEqual(2, board.check_horizontal_chains([3, 3], 2)[0])
		self.assertEqual(2, board.check_horizontal_chains([3, 5], 2)[0])
		self.assertEqual(2, board.check_horizontal_chains([3, 7], 2)[0])

		self.assertEqual(2, board.check_vertical_chains([3, 1], 2)[0])
		self.assertEqual(2, board.check_vertical_chains([3, 3], 2)[0])
		self.assertEqual(2, board.check_vertical_chains([3, 5], 2)[0])
		self.assertEqual(2, board.check_vertical_chains([3, 7], 2)[0])

		self.assertEqual(2, board.check_diagonal_up_chains([3, 3], 2)[0])
		self.assertEqual(2, board.check_diagonal_up_chains([3, 4], 2)[0])
		self.assertEqual(2, board.check_diagonal_up_chains([3, 5], 2)[0])
		self.assertEqual(2, board.check_diagonal_up_chains([3, 7], 2)[0])

		self.assertEqual(2, board.check_diagonal_down_chains([3, 1], 2)[0])
		self.assertEqual(2, board.check_diagonal_down_chains([3, 3], 2)[0])
		self.assertEqual(2, board.check_diagonal_down_chains([3, 4], 2)[0])
		self.assertEqual(2, board.check_diagonal_down_chains([3, 5], 2)[0])

	def test_chains_3(self):
		board, player = self.create_test_chain_3()
		player = 2

		self.assertEqual(3, board.check_horizontal_chains([3, 1], 2)[0])
		self.assertEqual(3, board.check_horizontal_chains([3, 4], 2)[0])


		self.assertEqual(3, board.check_vertical_chains([3, 1], 2)[0])
		self.assertEqual(3, board.check_vertical_chains([3, 4], 2)[0])


		self.assertEqual(3, board.check_diagonal_up_chains([3, 4], 2)[0])
		self.assertEqual(3, board.check_diagonal_up_chains([3, 7], 2)[0])

		self.assertEqual(3, board.check_diagonal_down_chains([3, 1], 2)[0])
		self.assertEqual(3, board.check_diagonal_down_chains([3, 4], 2)[0])

	def test_chains_4(self):
		board, player = self.create_test_chain_4()
		player = 2

		self.assertEqual(4, board.check_horizontal_chains([3, 3], 2)[0])
		self.assertEqual(4, board.check_horizontal_chains([3, 7], 2)[0])


		self.assertEqual(4, board.check_vertical_chains([3, 3], 2)[0])
		self.assertEqual(4, board.check_vertical_chains([3, 7], 2)[0])

		self.assertEqual(4, board.check_diagonal_up_chains([3, 7], 2)[0])

		self.assertEqual(4, board.check_diagonal_down_chains([3, 1], 2)[0])
		self.assertEqual(4, board.check_diagonal_down_chains([3, 3], 2)[0])

	# def test_ai_choice_4(self):
	# 	board, player = c4main.Player("AI")
	# 	game = c4main.Game(player, None)
	# 	board = game.board
	# 	board.place(2,1).place(3,1).place(5,2).place(4,2).place(2,2).place(3,2)
	# 	move = game.players[0].decide(board, 1)
	# 	self.assertEqual(move, 4) #player.decide(board, 1) == 1)

	# def test_ai_choice_5(self):
	# 	board, player = c4main.Game(c4main.Player("AI"), None)

	# 	move = player.decide(board,1)
	# 	self.assertTrue(move > 0 and move < 8)

	# def test_ai_choice_6(self):  #This tests the AI's ability to not move somewhere that gives the opponent the win
	# 	board, player = c4main.Game(c4main.Player("AI"), c4main.Player("AI"))

	# 	board.place(1,2).place(2,1).place(3,1).place(1,1).place(2,1).place(3,2).place(3,2).place(2,2).place(1,1).place(1,1).place(1,2).place(2,2).place(6,2).place(6,2).place(7,1)

	# 	move = player.decide(board, 1)
	# 	self.assertEqual(move, 7)

	# def test_ai_choice_7(self):  #This tests that the AI will give their opponent the win only if they have no other moves
	# 	game = c4main.Game(c4main.Player("AI"), c4main.Player("AI"))
	# 	board = game.board
	# 	board.place(1,2).place(2,1).place(3,1).place(1,1).place(2,1).place(3,2).place(3,2).place(2,2).place(1,1).place(1,1).place(1,2).place(2,2).place(6,2).place(6,2).place(7,1).place(1,2).place(2,1).place(2,2).place(3,1).place(3,1).place(3,1).place(5,2).place(5,1).place(5,1).place(5,2).place(5,2).place(5,1).place(6,1).place(6,1).place(6,2).place(6,2).place(7,1).place(7,2).place(7,2).place(7,2).place(7,1)
	# 	move = game.players[0].decide(board, 1)
	# 	self.assertEqual(move, 4)

	# def test_ai_choise_8(self):  #Tests whether a move will be made when there atleast two moves that all lose the game.
	# 	game = c4main.Game(c4main.Player("AI"), c4main.Player("AI"))
	# 	board = game.board
	# 	board.place(1,2).place(1,2).place(1,1).place(1,1).place(1,2).place(1,2)
	# 	board.place(3,1).place(3,2).place(3,1).place(3,2).place(3,2).place(3,1)
	# 	board.place(4,2).place(4,2).place(4,1).place(4,2).place(4,2).place(4,1)
	# 	board.place(5,1).place(5,2).place(5,1).place(5,2).place(5,2).place(5,1)
	# 	board.place(7,2).place(7,2).place(7,1).place(7,1).place(7,2).place(7,2)
	# 	move = game.players[0].decide(board, 1)
	# 	self.assertTrue(move in [2, 6])

	# def test_ai_play_game_0(self):
	# 	game = c4main.Game(c4main.Player("AI"), c4main.Player("AI"))
	# 	#game.start()

	# 	self.assertTrue(True)

if __name__ == '__main__':
	unittest.main()
