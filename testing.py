import unittest

from exeptions import GameOverException, AlreadyFullColumnExceptions
from game import Game
from player import Player

class Testing(unittest.TestCase):
	def setUp(self):
		self.game=Game()
		self.board=self.game.get_board()
		self.player_1 = Player("Player 1", 1, (12, 196, 239))
		self.player_2 = Player("Computer", 2, (246, 1, 157))

	def test_add_player_piece(self):
		#Check addition of a player piece in a board
		self.game.place_player_piece(self.player_1.piece, 1)
		self.assertEqual(self.game.get_piece(0, 1), self.player_1.piece)
		print(self.board)

	def test_add_blocking_computer_piece(self):
		#check if the computer blocks a winning move
		self.game.place_player_piece(self.player_1.piece, 0)
		self.game.place_player_piece(self.player_1.piece, 2)
		self.game.place_player_piece(self.player_1.piece, 1)
		self.game.place_computer_piece(self.player_2.piece, self.player_1.piece)
		self.assertEqual(self.game.get_piece(0, 3), self.player_2.piece)
		print(self.board)

	def test_winning_computer(self):
		self.game.place_player_piece(self.player_2.piece, 0)
		self.game.place_player_piece(self.player_2.piece, 2)
		self.game.place_player_piece(self.player_2.piece, 1)

		with self.assertRaises(GameOverException) as context:#???
			self.game.place_computer_piece(self.player_2.piece, self.player_1.piece)


		self.assertEqual(str(context.exception), "Game Finished.")
	def test_player_1_wins(self):

		self.game.place_player_piece(self.player_1.piece, 0)
		self.game.place_player_piece(self.player_1.piece, 2)
		self.game.place_player_piece(self.player_1.piece, 1)


		with self.assertRaises(GameOverException) as context:
			self.game.place_player_piece(self.player_1.piece, 3)

		self.assertEqual(str(context.exception), "Game Finished.")

	def test_full_column_error(self):
		self.game.place_player_piece(self.player_1.piece, 0)
		self.game.place_player_piece(self.player_2.piece, 0)
		self.game.place_player_piece(self.player_1.piece, 0)
		self.game.place_player_piece(self.player_2.piece, 0)
		self.game.place_player_piece(self.player_1.piece, 0)
		self.game.place_player_piece(self.player_2.piece, 0)
		with self.assertRaises(AlreadyFullColumnExceptions) as context:
			self.game.place_player_piece(self.player_1.piece, 0)
		print(self.board)


if __name__ == "__main__":
	unittest.main()
