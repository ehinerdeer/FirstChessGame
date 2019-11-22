# This is the definitions for our Piece super Class and all pieces sub classes

import random
import copy
import abc
import math

class Piece:
	"""
	Definition of a piece that all pieces will inherit each piece has the following:
	Color, X-Coordinate, Y-Coordinate and position on the board
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

class King(Piece):
	def __init__(self, color, x, y):
		super().__init__(color, x, y)
		self.symbol = 'K'
		self.display = self.color + self.symbol
		self.value = 5

	def generateMoves(self):
		currX = self.x
		currY = self.y
		result = []
		if self.valid(currX, currY - 1):
			result.append((currX, currY - 1))
		if self.valid(currX, currY + 1):
			result.append((currX, currY + 1))
		if self.valid(currX - 1, currY):
			result.append((currX - 1, currY))
		if self.valid(currX + 1, currY):
			result.append((currX + 1, currY))
		if self.valid(currX + 1, currY):
			result.append((currX + 1, currY - 1))
		if self.valid(currX + 1, currY + 1):
			result.append((currX + 1, currY + 1))
		if self.valid(currX - 1, currY - 1):
			result.append((currX - 1, currY - 1))
		if self.valid(currX - 1, currY + 1):
			result.append((currX - 1, currY + 1))
		return result

class Queen(Piece):
	def __init__(self, color, x, y):
		super().__init__(color, x, y)
		self.symbol = 'Q'
		self.display = self.color + self.symbol
		self.value = 9

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
		self.value = 5

	def generateMoves(self):
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

	def queenMoves(currX, currY):
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
		currX = self.x
		currY = self.y

	def queenMoves(currX, currY):
		result = []
		

class Knight(Piece):
	def __init__(self, color, x, y):
		super().__init__(color, x, y)
		self.symbol = 'N'
		self.display = self.color + self.symbol
		self.value = 3

	def generateMoves(self):
		currX = self.x
		currY = self.y
		result = []
		if self.valid(currX + 2, currY + 1)
			result.append(currX + 2, currY + 1)
		if self.valid(currX + 2, currY - 1)
			result.append(currX + 2, currY - 1)
		

class Pawn(Piece):
	def __init__(self, color, x, y):
		super().__init__(color, x, y)
		self.symbol = 'P'
		self.display = self.color + self.symbol
		self.hasMoved = False
		self.value = 1

	def generateMoves(self):
		if self.hasMoved:
			return [(currX, currY + 1)]








