from typing import *

class AStar8Puzzle:
	def __init__(self, puzzlePoint: "PuzzlePoint" , maxIterations: int = float('inf')) ->None:
		openList = [puzzlePoint]
		closedList = []
		while len(openList) > 0 and maxIterations > 0:
			
			maxIterations -= 1
			currentPoint = openList.pop(openList.index(min(openList, key = lambda x: x.f)))
			
			if currentPoint.f == 0:
				input("Press enter to check the solution")
				self.reverseMoves( currentPoint ) 
				return
			currentPoint.getMoves( openList, closedList)

			closedList.append( currentPoint )

		print( "NO SOLUTION FOUND" if maxIterations > 0 else "MAX ITERATIONS REACHED BEFORE FINDING A SOLUTION" )
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