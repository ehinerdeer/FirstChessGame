# This is the definitions for our Piece super Class and all pieces sub classes

class Piece:
	"""
	Definition of a piece that all pieces will inherit each piece has the following:
	Color, X-Coordinate, Y-Coordinate and position on the board
	"""
	def __init__(self, color, x, y):
		self.color = color
		self.x = x
		self.y = y

class King(Piece):
	def __init__(self, color, x, y):
		super().__init__(color, x, y)
		self.symbol = 'K'
		self.display = self.color + self.symbol

class Queen(Piece):
	def __init__(self, color, x, y):
		super().__init__(color, x, y)
		self.symbol = 'Q'
		self.display = self.color + self.symbol

class Rook(Piece):
	def __init__(self, color, x, y):
		super().__init__(color, x, y)
		self.symbol = 'R'
		self.display = self.color + self.symbol

class Bishop(Piece):
	def __init__(self, color, x, y):
		super().__init__(color, x, y)
		self.symbol = 'B'
		self.display = self.color + self.symbol

class Knight(Piece):
	def __init__(self, color, x, y):
		super().__init__(color, x, y)
		self.symbol = 'N'
		self.display = self.color + self.symbol

class Pawn(Piece):
	def __init__(self, color, x, y):
		super().__init__(color, x, y)
		self.symbol = 'P'
		self.display = self.color + self.symbol