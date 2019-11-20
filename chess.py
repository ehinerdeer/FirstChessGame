#my attempt at beggining a chess game that can be played in the console
#author Eric Hinerdeer

import random
import copy
import abc
import math
from board import *

class PlayGame(ChessBoard):
	def __init__(self):
		super().__init__()
		self.turn = 'b'

	def play(self):
		tryagain = False
		while(1):
			if self.turn == 'w' and tryagain == False:
				self.turn = 'b'
				print()
				print('Black\'s Turn - Enter move (Example: e2e4): ')
			elif self.turn == 'b' and tryagain == False:
				self.turn = 'w'
				print()
				print('White\'s Turn - Enter move (Example: e2e4): ')
			self.printBoard()
			move = input()
			if move == 'quit':
				break;
			fr = move[0:2]
			to = move[2:4]
			fx = self.convertLetToNum(fr[0])
			ty = self.convertLetToNum(to[0])
			if fr[0] != None and to[0] != None:
				piece = self.findPiece(fx, (int(fr[1]) - 1), self.turn)
				if piece != None:
					self.move(piece, ty, (int(to[1]) - 1))
					tryagain = False
				else:
					print('x from: ' + str(fx) + ' x to: ' + str(ty) + ' y from: ' + str(int(fr[1]) - 1) + " y to: " + str(int(to[1]) - 1))
					print('Invalid Piece to move try again: ' )
					tryagain = True

	def move(self, piece, x, y):
		"""
		simple switch of position from one square to another for any piece
		NOTE: might be more complicated later on with move restrictions and mapping
		or create each piece has a spefic mapping
		"""
		self.board[piece.x][piece.y] = ' .'
		self.board[x][y] = piece.display
		piece.x = x
		piece.y = y

	def valid(self, row, col):
		"""
		Returns true if the given row and col represent a valid location on
		the chess board.
		"""
		return row >= 0 and col >= 0 and row < 8 and col < 8

	def contains(self, board, row, col, symbol):
		"""
		Returns true if the given row and col represent a valid location on
		the chess board and the piece at that location, None if not valid
		"""
		if self.valid(row,col) and board[row][col] != '.':
			return board[row][col]
		else:
			return None

	def convertLetToNum(self, letter):
		letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
		for i in range(len(letters)):
			if letter == letters[i]:
				return i
		return None

	def opponent(self, player):
		"""
		Given a player symbol, returns the opponent's symbol, 'B' for black,
		or 'W' for white.
		"""
		if player == 'B':
			return 'W'
		else:
			return 'B'

game = PlayGame()
game.play()
