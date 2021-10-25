from typing import *

class AStar:
	def __init__(self, point: "DataTypeForPoint" , maxIterations: int = float('inf')) ->None:
		"""
		
			AStar traverse. Works on any kind of Point given by the user.
			The given parameters are:
				point: the given graph, matrix, etc. to traverse and to find a solution to

					The following functions must be defined on the given point class:
						- getMoves( openList, closedList, currentPoint )
							This function must obtain the succesors for each visited node.

						- printSolution()
							Prints the solution once found if there is any.
			
				maxIterations: the maximum iterations that AStar will do before stopping if
					the solution is not found within the range of 0 and maxIterations

		"""
		openList = [point]
		closedList = []
		iteration = 0
		while len(openList) > 0 and maxIterations > 0:
			
			iteration += 1
			maxIterations -= 1
			currentPoint = openList.pop(openList.index(min(openList, key = lambda x: x.f)))
			
			if currentPoint.f == 0:
				input("Press enter to check the solution")
				self.reverseMoves( currentPoint ) 
				return
		
			currentPoint.getMoves( openList, closedList)

			closedList.append( currentPoint )

		print( "NO SOLUTION FOUND" if maxIterations > 0 else "MAX ITERATIONS REACHED BEFORE FINDING A SOLUTION" )

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