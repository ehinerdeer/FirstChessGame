# This is the definitions for our Piece super Class and all pieces sub classes

import random
import copy
import abc
import math

class Piece:
	"""
	Definition of a piece that all pieces will inheri. Each piece has the following:
	Color, X-Coordinate, Y-Coordinate and a valid function to check if where they are 
	moving to is a valid move and remains in the bounds of the board. 
	"""
	def __init__(self, color, x, y):
		self.color = color
		self.x = x
		self.y = y

	def valid(self, row, col):
		"""
		Returns true if the given row and col represent a valid location on
		the chess board.
		"""
		return row >= 0 and col >= 0 and row < 8 and col < 8

	def spaceOpen(self, x, y, pieces):
		if self.valid(x, y):
			for i in pieces:
				findY = 7 - y
				if i.x == x and i.y == findY:
					return False
			return True


class King(Piece):
	def __init__(self, color, x, y):
		super().__init__(color, x, y)
		self.symbol = 'K'
		self.display = self.color + self.symbol
		self.value = 5

	def generateMoves(self, pieces):
		"""
		Kings can only move one square up dwn left or right
		This checks if moves stay in the board bounds and returns
		all valid potential moves that stay on the board
		"""
		currX = self.x
		currY = self.y
		result = []
		if self.spaceOpen(currX, currY - 1, pieces):
			result.append((currX, currY - 1))
		if self.spaceOpen(currX, currY + 1, pieces):
			result.append((currX, currY + 1))
		if self.spaceOpen(currX - 1, currY, pieces):
			result.append((currX - 1, currY))
		if self.spaceOpen(currX + 1, currY, pieces):
			result.append((currX + 1, currY))
		if self.spaceOpen(currX + 1, currY, pieces):
			result.append((currX + 1, currY - 1))
		if self.spaceOpen(currX + 1, currY + 1, pieces):
			result.append((currX + 1, currY + 1))
		if self.spaceOpen(currX - 1, currY - 1, pieces):
			result.append((currX - 1, currY - 1))
		if self.spaceOpen(currX - 1, currY + 1, pieces):
			result.append((currX - 1, currY + 1))
		return result

class Queen(Piece):
	def __init__(self, color, x, y):
		super().__init__(color, x, y)
		self.symbol = 'Q'
		self.display = self.color + self.symbol
		self.value = 9

	def generateMoves(self):
		"""
		Queens move in combo of Rooks and Bishops
		This returns all the potential moves that stay on the board for
		a Queen that are valid
		"""
		currX = self.x
		currY = self.y
		result = []
		bishMoves = Bishop(self.color, self.x, self.y).queenMoves(currX, currY)
		result = Rook(self.color, self.x, self.y).queenMoves(currX, currY)
		for i in bishMoves:
			result.append(i)
		return result

class Rook(Piece):
	def __init__(self, color, x, y):
		super().__init__(color, x, y)
		self.symbol = 'R'
		self.display = self.color + self.symbol
		self.value = 5

	def generateMoves(self):
		"""
		Rooks can only move up down left right
		This returns all potential moves that stay on the board for
		a Rook marked valid
		"""
		currX = self.x
		currY = self.y
		result = []
		#Vertical Moves Only
		for i in range(8 - currY):
			newY = currY + i + 1
			if self.valid(currX, newY):
				result.append((currX, newY))
		for i in range(currY):
			newY = currY - i - 1
			if self.valid(currX, newY):
				result.append((currX, newY))
		#Horizontal Moves Only
		for i in range(8 - currX):
			newX = currX + i + 1
			if self.valid(newX, currY):
				result.append((newX, currY))
		for i in range(currX):
			newX = currX - i - 1
			if self.valid(newX, currY):
				result.append((newX, currY))
		return result

	def queenMoves(self, currX, currY):
		"""
		This is generate moves but sends Rooks moves to the 
		Queen class to help simplify move construction
		"""
		result = []
		#Vertical Moves Only
		for i in range(8 - currY):
			newY = currY + i + 1
			if self.valid(currX, newY):
				result.append((currX, newY))
		for i in range(currY):
			newY = currY - i - 1
			if self.valid(currX, newY):
				result.append((currX, newY))
		#Horizontal Moves Only
		for i in range(8 - currX):
			newX = currX + i + 1
			if self.valid(newX, currY):
				result.append((newX, currY))
		for i in range(currX):
			newX = currX - i - 1
			if self.valid(newX, currY):
				result.append((newX, currY))
		return result

class Bishop(Piece):
	def __init__(self, color, x, y):
		super().__init__(color, x, y)
		self.symbol = 'B'
		self.display = self.color + self.symbol
		self.value = 3

	def generateMoves(self):
		"""
		Bishops can only move diaganol on their own square
		This returns all potential moves that a Bishop can make
		from its current position
		"""
		currX = self.x
		currY = self.y
		testY = currY
		result = []
		for i in range(currX):
			testY -= 1
			if self.valid(currX - i - 1, testY):
				result.append((currX - i - 1, testY))

		testY = currY
		for i in range(8 - currX):
			testY += 1
			if self.valid(currX + i + 1, testY):
				result.append((currX + i + 1, testY))

		testY = currY
		for i in range(8 - currX):
			testY += 1
			if self.valid(currX - i - 1, testY):
				result.append((currX - i - 1, testY))

		testY = currY
		for i in range(8 - currX):
			testY -= 1
			if self.valid(currX + i + 1, testY):
				result.append((currX + i + 1, testY))

		return result

	def queenMoves(self, currX, currY):
		"""
		This is all the Bishop moves but the function is for
		sending those moves to Queens to simplify generating 
		the Queen moves. 
		"""
		testY = currY
		result = []
		for i in range(currX):
			testY -= 1
			if self.valid(currX - i - 1, testY):
				result.append((currX - i - 1, testY))

		testY = currY
		for i in range(8 - currX):
			testY += 1
			if self.valid(currX + i + 1, testY):
				result.append((currX + i + 1, testY))

		testY = currY
		for i in range(8 - currX):
			testY += 1
			if self.valid(currX - i - 1, testY):
				result.append((currX - i - 1, testY))

		testY = currY
		for i in range(8 - currX):
			testY -= 1
			if self.valid(currX + i + 1, testY):
				result.append((currX + i + 1, testY))

		return result
		

class Knight(Piece):
	def __init__(self, color, x, y):
		super().__init__(color, x, y)
		self.symbol = 'N'
		self.display = self.color + self.symbol
		self.value = 3

	def generateMoves(self):
		"""
		Knights can only move in an L shape
		This generates all valid and potential moves that
		a Knight can make from its current position.
		"""
		currX = self.x
		currY = self.y
		result = []
		if self.valid(currX + 2, currY + 1):
			result.append((currX + 2, currY + 1))
		if self.valid(currX + 2, currY - 1):
			result.append((currX + 2, currY - 1))
		if self.valid(currX - 2, currY + 1):
			result.append((currX - 2, currY + 1))
		if self.valid(currX - 2, currY - 1):
			result.append((currX - 2, currY - 1))
		if self.valid(currX - 1, currY + 2):
			result.append((currX - 1, currY + 2))
		if self.valid(currX - 1, currY - 2):
			result.append((currX - 1, currY - 2))
		if self.valid(currX + 1, currY - 2):
			result.append((currX + 1, currY - 2))
		if self.valid(currX + 1, currY + 2):
			result.append((currX + 1, currY + 2))
		return result
		

class Pawn(Piece):
	def __init__(self, color, x, y):
		super().__init__(color, x, y)
		self.symbol = 'P'
		self.display = self.color + self.symbol
		self.hasMoved = False
		self.value = 1

	def generateMoves(self):
		"""
		Pawns can move 1 or 2 squares on their first move and then 
		only 1 after that. This generate move function disregards 
		captures and en pasant for now. 
		"""
		if self.hasMoved:
			return [(currX, currY + 1)]
		if not self.hasMoved:
			return [(currX, currY + 1) , (currX, currY + 2)]








