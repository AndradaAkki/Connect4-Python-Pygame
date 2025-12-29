from texttable import Texttable

from exeptions import AlreadyFullColumnExceptions, OutOfBoundsExceptions


class Connect4Board:
	def __init__(self):
		self._board =[[' ' for _ in range(7)] for _ in range(6)]
		self.__rows=6
		self.__cols=7

	@property
	def rows(self):
		return self.__rows
	@property
	def cols(self):
		return self.__cols

	def drop_piece(self, row, col, piece):
		self._board[row][col] = piece

	def is_valid_location(self, col):
		if col > self.__cols - 1:
			raise OutOfBoundsExceptions
		if self._board[self.__rows - 1][col] != ' ':
			raise AlreadyFullColumnExceptions
		return True
	def is_valid_computer_location(self, col):
		if col > self.__cols - 1:
			return False
		if self._board[self.__rows - 1][col] != ' ':
			return False
		return True

	def remove_piece(self, row, col, piece):
		self._board[row][col] = ' '

	def get_next_open_row(self, col):
		for r in range(self.__rows):
			if self._board[r][col] == ' ':
				return r
		raise OutOfBoundsExceptions

	def won(self, player_piece):

		# horizontal win check
		for j in range(self.__cols - 3):
			for i in range(self.__rows):
				if self._board[i][j] == player_piece and self._board[i][j + 1] == player_piece and (
						  self._board[i][j + 2] == player_piece) and self._board[i][j + 3] == player_piece:
					return True

		# vertical win check
		for j in range(self.__cols):
			for i in range(self.__rows - 3):
				if self._board[i][j] == player_piece and self._board[i + 1][j] == player_piece and (
						  self._board[i + 2][j] == player_piece) and self._board[i + 3][j] == player_piece:
					return True

		# main diagonal win check
		for j in range(self.__cols - 3):
			for i in range(3, self.__rows):
				if self._board[i][j] == player_piece and self._board[i - 1][j+1] == player_piece and (
					self._board[i-2][j + 2] == player_piece) and self._board[i-3][j + 3] == player_piece:
					return True

		# anti-diagonal win check
		for j in range(self.__cols - 3):
			for i in range(self.__rows-3):
				if self._board[i][j] == player_piece and self._board[i+1][j + 1] == player_piece and (
					self._board[i+2][j + 2] == player_piece) and self._board[i+3][j + 3] == player_piece:
					return True

		return False

	def get_available_col(self):
		valid_cols = []
		for i in range(self.__cols):
			if self.is_valid_computer_location(i):
				valid_cols.append(i)
		return valid_cols

	def get_piece(self, row, col):
		return self._board[row][col]

	#the str is flipped
	def __str__(self):
		table= Texttable()
		header = [' '] + [str(i) for i in range(7)]
		table.header(header)
		for i in range(5, -1, -1):
			row = [str(i)] + self._board[i]
			table.add_row(row)

		return table.draw()
