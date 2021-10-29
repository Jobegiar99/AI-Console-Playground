from collections import defaultdict
import datetime
import random
class Sudoku:
	

	def __init__(self):
		self.rowInfo = defaultdict(lambda: set())
		self.colInfo = defaultdict(lambda: set())
		self.matrixInfo = defaultdict(lambda: set())
		self.board = []
		self.emptyCells = []
		self.inputBoard()

		startTime = datetime.datetime.now()
		self.solve(0)
		endTime = datetime.datetime.now()
		timeDiff = (endTime - startTime)
		print("Time taken to solve the board in milliseconds: ",end = "")
		print(timeDiff.total_seconds() * 1000)
		self.printBoard()
	
	def mapPositionToSubMatrix(self, row, column):
		if row < 3:
			if column < 3:
				return 0
			if column < 6:
				return 1
			if column < 9:
				return 2

		if row < 6:
			if column < 3:
				return 3
			if column < 6:
				return 4
			if column < 9:
				return 5

		if column < 3:
			return 6
		if column < 6:
			return 7
		if column < 9:
			return 8

	def inputBoard(self):
		self.board = []
		print("please type each row of the board. Use an underscore '_' to represent an empty cell")

		for iteration in range(9):
			row = input().split(' ')
			self.board.append(row)

		self.checkIfValidBoard()
			
		

	def checkIfValidBoard(self):
		self.rowInfo = defaultdict(lambda: set())
		self.colInfo = defaultdict(lambda: set())
		self.matrixInfo = defaultdict(lambda: set())
		self.emptyCells = []

		for row in range(9):
			for column in range(9):

				elem = self.board[row][column]
				matrixIndex = self.mapPositionToSubMatrix(row,column)

				if elem == "_":
					self.emptyCells.append((row,column))
					continue

				if not self.isValidInThisMap( elem, row, self.rowInfo ):
					self.inputBoard()
					return
				
				if not self.isValidInThisMap( elem, column, self.colInfo ):
					self.inputBoard()
					return

				if not self.isValidInThisMap( elem, matrixIndex, self.matrixInfo ):
					self.inputBoard()
					return
	
	def isValidInThisMap( self, elem, index, mapToCheck ):
		if elem in mapToCheck[index]:
			print("This is not a valid board, please enter a new one")
			return False
		mapToCheck[index].add( elem )
		return True	

	def printBoard(self):
		info = {}
		info['1'] =[" d88    ","  88    ","  88    ","  88    ","  88    "," d88P   "]
	
		info['2'] = ["d8888b. ","    `88 ",".aaadP' ","88'     ","88.     ","Y88888P "]

		info['3'] =  ["d8888b. ","    `88 "," aaad8' ","    `88 ","    .88 ","d88888P "]

		info['4'] = ["dP   dP ","88   88 ","88aaa88 ","     88 ","     88 ","     dP "]

		info['5'] =  ["888888P ","88'     ","88baaa. ","    `88 ","     88 ","d88888P "]

		info['6'] =  [".d8888P ","88'     ","88baaa. ","88` `88 ","8b. .d8 ","`Y888P' "]

		info['7'] = ["d88888P ","    d8' ","   d8'  ","  d8'   "," d8'    ","d8'     "]
		
		info['8'] = [".d888b. ","Y8' `8P ","d8bad8b ","88` `88 ","8b. .88 ","Y88888P "]

		info['9'] = [".d888b. ","Y8' `88 ","`8bad88 ","    `88 ","d.  .88 ","`8888P  "]

		info["_"] = ["        ","        ","        ","        ","        ","        "]

		info["-"] = ["        ","        ","        ","        ","        ","        "]

		for row in self.board:
			for index in range(len(info[row[0]])):
				rowStr = ""
				for boardElement in range(9):
					rowStr += "|" + info[row[boardElement]][index] + "|"
				print( rowStr )
			print("-----------"*8 + '-')

	def solve(self,index):
		if index >= len(self.emptyCells):
			return True
			
		row, column = self.emptyCells[index]
		matrixIndex = self.mapPositionToSubMatrix(row,column)
		for number in range(1,10):
			candidate = str(number)
			if candidate in self.rowInfo[row]:
				continue
				
			if candidate in self.colInfo[column]:
				continue

			if candidate in self.matrixInfo[ matrixIndex ]:
				continue
				
			self.rowInfo[row].add( candidate )
			self.colInfo[column].add( candidate )
			self.matrixInfo[matrixIndex ].add( candidate )

			self.board[row][column] = candidate
			foundSolution = self.solve(index + 1)
			if foundSolution:
				return True

			self.board[row][column] = "_"
			self.rowInfo[ row ].remove( candidate )
			self.colInfo[ column ].remove( candidate )
			self.matrixInfo[ matrixIndex ].remove( candidate )	

Sudoku()

