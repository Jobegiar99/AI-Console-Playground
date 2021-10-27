from os import system
from time import sleep
from typing import *

class DungeonPoint:

	def __init__(self,row,column,h, g):
		self.row = row
		self.column = column
		self.h = h 
		self.g = g
		self.f = h + g
		self.previous = None

	def checkIfGoal(self):
		return (self.row, self.column) == self.targetPosition

	def printSearch(self, level):
		if self:
			level[self.row][self.column] = '.'
			if self.previous:
				self.previous.printSearch(level)
			else:
				self.printSearchInConsoleHelper(level)
	
	def printSearchInConsoleHelper( self, level ):
		system("clear")
		print("  " + "__" * len(level[0]) * 2)
		for levelRow in level:
			print("|" + " ".join(['#' if x == True else ' ' if x == False else x for x in levelRow]) + " |")
		print("͞ ͞" * len(level[0]) * 2)
		sleep(0.05)


	def getMoves(self, openList, closedList, maze, goal):
		"""
	
		Obtains the possible moves that the algorithm could perform next
		and the heuristic of each one.
	
		"""
		row, column = self.row, self.column
		self.getMoveHelper(openList,closedList,row - 1, column, maze,goal)
		self.getMoveHelper(openList,closedList,row + 1, column, maze,goal)
		self.getMoveHelper(openList,closedList,row, column - 1, maze,goal)
		self.getMoveHelper(openList,closedList,row , column + 1, maze,goal)
	

	def getMoveHelper(
		self,  
		openList: List[List[int]],
		closedList: List[List[int]],
		targetRow:int, 
		targetColumn:int,
		maze: List[List[bool]],
		goal: Tuple[int,int]
	) -> None:
		"""
		
		Checks if the target move is a valid one, if it is, it obtains the heuristic and
		appends it into the possible moves list
		
		"""
		move = ( targetRow, targetColumn )
		if 0 <= targetRow < len(maze) and 0 <= targetColumn < len(maze[targetRow]) and (not maze[targetRow][targetColumn] or maze[targetRow][targetColumn] == 'G'):
			heuristic = self.getMoveHeuristic( (targetRow, targetColumn), goal)

			if self.checkIfPointInList( openList, move):
				return
			
			elif not self.checkIfPointInList( closedList, move):
				nextMove = DungeonPoint(targetRow, targetColumn,heuristic, self.g + 1)
				nextMove.previous = self
				openList.append(nextMove)

	def checkIfPointInList( self, listToCheck, item):
		for element in listToCheck:
			if (element.row, element.column) == item:
				return True
		return False

	def getMoveHeuristic( self, movePosition: Tuple[int,int], goal: Tuple[int,int]) -> int:
		"""
		
			Calculates the heuristic of the given move.

		"""		
		manhattanDistance = lambda x1,y1,x2,y2: abs( x1 - x2) + abs(y1 - y2)
				
		return manhattanDistance( movePosition[0], movePosition[1], goal[0], goal[1] )