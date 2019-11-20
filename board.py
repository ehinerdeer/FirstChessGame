#This is the definitions for the Board Class in our chess game

import random
import copy
import abc
import math
from pcs import *

class ChessBoard:
	def __init__(self):
		self.board = [[' .'] * 8 for _ in range(8)]
		self.size = 64
		"""
		Set Black Pieces Then White Pieces
		"""
		BlkRook1 = Rook('b', 0, 7)
		BlkKnight1 = Knight('b', 1, 7)
		BlkBishop1 = Bishop('b', 2, 7)
		BlkQueen = Queen('b', 3, 7)
		BlkKing = King('b', 4, 7)
		BlkBishop2 = Bishop('b', 5, 7)
		BlkKnight2 = Knight('b', 6, 7)
		BlkRook2 = Rook('b', 7, 7)
		BlkPawn1 = Pawn('b', 0, 6)
		BlkPawn2 = Pawn('b', 1, 6)
		BlkPawn3 = Pawn('b', 2, 6)
		BlkPawn4 = Pawn('b', 3, 6)
		BlkPawn5 = Pawn('b', 4, 6)
		BlkPawn6 = Pawn('b', 5, 6)
		BlkPawn7 = Pawn('b', 6, 6)
		BlkPawn8 = Pawn('b', 7, 6)
		WhtRook1 = Rook('w', 0, 0)
		WhtKnight1 = Knight('w', 1, 0)
		WhtBishop1 = Bishop('w', 2, 0)
		WhtQueen = Queen('w', 3, 0)
		WhtKing = King('w', 4, 0)
		WhtBishop2 = Bishop('w', 5, 0)
		WhtKnight2 = Knight('w', 6, 0)
		WhtRook2 = Rook('w', 7, 0)
		WhtPawn1 = Pawn('w', 0, 1)
		WhtPawn2 = Pawn('w', 1, 1)
		WhtPawn3 = Pawn('w', 2, 1)
		WhtPawn4 = Pawn('w', 3, 1)
		WhtPawn5 = Pawn('w', 4, 1)
		WhtPawn6 = Pawn('w', 5, 1)
		WhtPawn7 = Pawn('w', 6, 1)
		WhtPawn8 = Pawn('w', 7, 1)

		self.pieces = [
		BlkRook1, BlkKnight1, BlkBishop1, BlkQueen, BlkKing, BlkBishop2, BlkKnight2, BlkRook2,
		BlkPawn1, BlkPawn2, BlkPawn3, BlkPawn4, BlkPawn5, BlkPawn6, BlkPawn7, BlkPawn8,
		WhtRook1, WhtKnight1, WhtBishop1, WhtQueen, WhtKing, WhtBishop2, WhtKnight2, WhtRook2,
		WhtPawn1, WhtPawn2, WhtPawn3, WhtPawn4, WhtPawn5, WhtPawn6, WhtPawn7, WhtPawn8]

		for i in self.pieces:
			y = 7 - i.y
			self.board[i.x][y] = i.display

	def printBoard(self):
		"""
		Returns a string representation of the chess board.
		"""
		result = ""
		for i in range(8):
			result += str((8 - i)) + " "
			for j in range(8):
				result += str(self.board[j][i]) + " "
			result += "\n"
		result += "  a  b  c  d  e  f  g  h  \n"	
		print(result)

	def findPiece(self, x, y, color):
		for i in self.pieces:
			findY = 7 - y
			if i.x == x and i.y == y and i.color == color:
				return i
		return None
