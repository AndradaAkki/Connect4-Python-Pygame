class Player:
	def __init__(self, name, piece, color):
		self.__name = name
		self.__piece = piece
		self.__color = color

	@property
	def piece(self):
		return self.__piece

	@property
	def color(self):
		return self.__color

	@property
	def name(self):
		return self.__name