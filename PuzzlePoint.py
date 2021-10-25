from os import system, name
from time import sleep
from typing import *

class PuzzlePoint:

	def __init__(self,board,row,column,h, g, targetBoard = None, targetPositions = None):
		self.board = board
		self.row = row
		self.column = column
		self.h = h
		self.g = g
		self.f = h * g
		self.previous = None
		if targetBoard:
			self.targetPositions = {}
			primeNumbers = [1,3,5,7,9,11,13,17,19]
			primeIndex = 0

			for r in range(len(targetBoard)):
				for c in range(len(targetBoard[0])):
					if targetBoard[r][c] != "":
						self.targetPositions[targetBoard[r][c]] = (r,c,primeNumbers[primeIndex])
						primeIndex += 1
		else:
			self.targetPositions = targetPositions

	def printSolution( self, clear = True ):
		
		while self:
			if clear:
				system('clear')
			self.printHelper( self.board )
			
			sleep(0.4)
			self = self.previous

	def printHelper( self, board ):
		info = {}
		info[1] =[" d88    ","  88    ","  88    ","  88    ","  88    "," d88P   "]
	
		info[2] = ["d8888b. ","    `88 ",".aaadP' ","88'     ","88.     ","Y88888P "]

		info[3] =  ["d8888b. ","    `88 "," aaad8' ","    `88 ","    .88 ","d88888P "]

		info[4] = ["dP   dP ","88   88 ","88aaa88 ","     88 ","     88 ","     dP "]

		info[5] =  ["888888P ","88'     ","88baaa. ","    `88 ","     88 ","d88888P "]

		info[6] =  [".d8888P ","88'     ","88baaa. ","88` `88 ","8b. .d8 ","`Y888P' "]

		info[7] = ["d88888P ","    d8' ","   d8'  ","  d8'   "," d8'    ","d8'     "]
		
		info[8] = [".d888b. ","Y8' `8P ","d8bad8b ","88` `88 ","8b. .88 ","Y88888P "]

		info[""] = ["        ","        ","        ","        ","        ","        "]

		for row in board:
			for index in range(len(info[row[0]])):
				print("|",info[row[0]][index],"|",info[row[1]][index],"|",info[row[2]][index],"|")
			print("-----------"*3 + '-')
		

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
				move = PuzzlePoint(board_copy,targetRow, targetColumn,heuristic, self.g + 1, targetBoard = None, targetPositions = self.targetPositions)
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
		manhattanDistance = lambda x1,y1,x2,y2: abs( x1 - x2) + abs(y1 - y2)
		heuristic = 0
		badPlacedPieces = 1
		for row in range(3):
			for column in range(3):
				if board[row][column] == '':
					continue
				x2,y2,factor = self.targetPositions[board[row][column]]
				manhattanResult = manhattanDistance( row, column, x2, y2  )
				if manhattanResult > 0:
					heuristic += (manhattanResult * factor)
					badPlacedPieces += 1
				
		return (heuristic * badPlacedPieces)