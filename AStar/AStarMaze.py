from typing import *

class AStarMaze:
	def __init__(self, dungeonPoint: "DungeonPoint" , maze, goal: Tuple[int,int], visualizeSearch: bool ) ->None:
		openList = [dungeonPoint]
		closedList = []
		while len(openList) > 0 :
			
			currentPoint = openList.pop(openList.index(min(openList, key = lambda x: x.f)))
			if visualizeSearch:
				currentPoint.printSearch([[col for col in row] for row in maze])

			if ( currentPoint.row, currentPoint.column) == goal:
				currentPoint.printSearch(maze)
				input("Solution Found. Press Enter to return to main menu")
				#self.reverseMoves( currentPoint ) 
				return
			
			currentPoint.getMoves( openList, closedList, maze, goal)
			closedList.append( currentPoint )

		print( "NO SOLUTION FOUND")
		input("Press Enter to continue")

	def reverseMoves(self, AStarResult ):
		pointerA = None
		pointerB = AStarResult
		pointerC = AStarResult.previous

		while pointerB:
			pointerB.previous = pointerA
			pointerA = pointerB
			pointerB = pointerC
			if pointerC:
				pointerC = pointerC.previous
		pointerA.printSolution()