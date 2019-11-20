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

	def generateMoves(self):
		currX = self.x
		currY = self.y
		return [ (currX, currY - 1),
				 (currX, currY + 1),
				 (currX - 1, currY),
				 (currX + 1, currY),
				 (currX + 1, currY - 1),
				 (currX + 1, currY + 1),
				 (currX - 1, currY - 1),
				 (currX - 1, currY + 1) ]

class Queen(Piece):
	def __init__(self, color, x, y):
		super().__init__(color, x, y)
		self.symbol = 'Q'
		self.display = self.color + self.symbol

	def generateMoves(self):
		currX = self.x
		currY = self.y
		result = []
		bishMoves = Bishop().queenMoves(currX, currY)
		result = Rook().queenMoves(currX, currY)
		for i in bishMoves:
			result.append(i)
		return result

class Rook(Piece):
	def __init__(self, color, x, y):
		super().__init__(color, x, y)
		self.symbol = 'R'
		self.display = self.color + self.symbol

	def generateMoves(self):
		currX = self.x
		currY = self.y
		result = []
		#Vertical Moves Only
		for i in range(8 - currY):
			result.append((currX, currY + i + 1))
		for i in range(currY - 1):
			result.append((currX, currY - i + 1))
		#Horizontal Moves Only
		for i in range(8 - currX):
			result.append((currX + i + 1, currY))
		for i in range(currX - 1):
			result.append((currX - i + 1, currY))
		return result

	def queenMoves(currX, currY):
		result = []
		#Vertical Moves Only
		for i in range(8 - currY):
			result.append((currX, currY + i + 1))
		for i in range(currY - 1):
			result.append((currX, currY - i + 1))
		#Horizontal Moves Only
		for i in range(8 - currX):
			result.append((currX + i + 1, currY))
		for i in range(currX - 1):
			result.append((currX - i + 1, currY))
		return result

class Bishop(Piece):
	def __init__(self, color, x, y):
		super().__init__(color, x, y)
		self.symbol = 'B'
		self.display = self.color + self.symbol

	def generateMoves(self):
		currX = self.x
		currY = self.y

	def queenMoves(currX, currY):
		result = []
		

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
		self.hasMoved = False

	def generateMoves(self):
		if self.hasMoved:
			return [(currX, currY + 1)]








