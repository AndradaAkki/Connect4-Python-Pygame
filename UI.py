from exeptions import BoardExceptions, GameOverException
from game import Game
from player import Player


class Ui:
	def __init__(self):
		self.__game= Game()
		self.__player_1 = Player("Player 1", 1, (255, 0, 0))
		self.__player_2 = Player("Player 2", 2, (0, 0, 255))

	def place_player_piece(self, piece):
		try:
			col=int(input("Enter the column index: "))
			self.__game.place_player_piece(piece,col)
		except ValueError:
			print("please enter a number")

	def print_board(self):
		print(self.__game.get_board())

	def start_game(self):

		player_turn= True

		while True:
			self.print_board()
			if player_turn:
				try:
					self.place_player_piece(self.__player_1.piece)
					player_turn= False
				except GameOverException:
					print("You won!!!! :D")
					self.print_board()
					break
				except BoardExceptions as e:
					print(e)
			else:
				try:
					self.__game.place_computer_piece(self.__player_2.piece, self.__player_1.piece)
					player_turn = True
				except GameOverException:
					print("Computer won !!!! >:)")
					self.print_board()
					break
				except BoardExceptions as e:
					print(e)


if __name__ == "__main__":
	ui=Ui()
	ui.start_game()
