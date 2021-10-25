from os import system, name
from time import sleep
from typing import *

class PuzzlePoint:

	def __init__(self,board,row,column,h, g):
		self.board = board
		self.row = row
		self.column = column
		self.h = h
		self.g = g
		self.f = h * g
		self.previous = None

	def printSolution( self ):
		while self:
			system('clear')
			self.printHelper( self.board )
			
			sleep(0.2)
			self = self.previous

	def printHelper( self, board ):
		for row in board:
			elemA = row[0] if row[0] != "" else " "
			elemB = row[1] if row[1] != "" else " "
			elemC = row[2] if row[2] != "" else " "
			print("|", elemA ,"|", elemB ,"|", elemC ) 

	def getMoves(self, openList, closedList):
		"""
	
		Obtains the possible moves that the algorithm could perform next
		and the heuristic of each one.
	
		"""
		row, column = self.row, self.column
		self.getMoveHelper(openList,closedList,row - 1, column)
		self.getMoveHelper(openList,closedList,row + 1, column)
		self.getMoveHelper(openList,closedList,row, column - 1)
		self.getMoveHelper(openList,closedList,row , column + 1)

	def getMoveHelper(
		self,  
		openList: List[List[int]],
		closedList: List[List[int]],
		targetRow:int, 
		targetColumn:int
	) -> None:
		"""
		
		Checks if the target move is a valid one, if it is, it obtains the heuristic and
		appends it into the possible moves list and the row and column of the empty cell.
		
		"""
		board, row, column = self.board, self.row, self.column

		if 0 <= targetRow < 3 and 0 <= targetColumn < 3:
			board_copy = [[col for col in row] for row in board]
			board_copy[row][column], board_copy[targetRow][targetColumn] = board_copy[targetRow][targetColumn] , board_copy[row][column]
			heuristic = self.getMoveHeuristic(board_copy,self.g)

			if self.checkIfPointInList(openList,board_copy):
				return
			
			elif not self.checkIfPointInList(closedList, board_copy):
				move = PuzzlePoint(board_copy,targetRow, targetColumn,heuristic, self.g + 1)
				move.previous = self
				openList.append(move)

	def checkIfPointInList( self, listToCheck, item):
		for element in listToCheck:
			if element.board == item:
				return True
		return False

	def getMoveHeuristic( 
		self,
		board: List[List[int]],
		g: int # the cost so far to reach the current state
	) -> int:
		"""
		
		Calculates the heuristic of the given board.

		"""
		targetPositions = {
			1: (0,0,1),
			2: (0,1,3),
			3: (0,2,5),
			4: (1,0,7),
			5: (1,2,9),
			6: (2,0,11),
			7: (2,1,13),
			8: (2,2,17)
		}
		manhattanDistance = lambda x1,y1,x2,y2: abs( x1 - x2) + abs(y1 - y2)
		heuristic = 0
		badPlacedPieces = 1
		for row in range(3):
			for column in range(3):
				if board[row][column] == '':
					continue
				x2,y2,factor = targetPositions[board[row][column]]
				manhattanResult = manhattanDistance( row, column, x2, y2  )
				if manhattanResult > 0:
					heuristic += (manhattanResult * factor)
					badPlacedPieces += 1
				
		return (heuristic * badPlacedPieces)