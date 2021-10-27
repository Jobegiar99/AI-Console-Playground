import random

class MazeGenerator:
	def __init__(self, rows, columns, wanderer = None, seeker = None, showStart = True, showEnd = True): 
		self.rows = rows
		self.columns = columns
		self.level = [[True for x in range(columns )] for y in range(rows )]
		self.seekerVisited = []
		self.generalVisited = []
		self.wanderer = ( rows - 1, random.randint(0,columns - 1)) if wanderer == None else wanderer
		self.seeker = ( 0, random.randint(0 , columns - 1)) if seeker == None else seeker
		self.Manhattan = lambda pointA, pointB: abs( pointA[0] - pointB[0]) + abs( pointA[1] - pointB[1])
		
		self.generateSkeleton( self.wanderer, self.seeker)
		if showStart:
			self.level[self.wanderer[0]][self.wanderer[1]] = 'S'
		
		if showEnd:
			self.level[self.seeker[0]][self.seeker[1]] = 'G'

	def generateSkeleton(self,  wanderer, seeker):
		
		while seeker not in self.generalVisited:
			self.level[ seeker[0] ][ seeker[1] ] = False
			self.level[ wanderer[0] ][ wanderer[1] ] = False
			self.seekerVisited.append( seeker )
			self.generalVisited.append( wanderer )

			seeker = self.getSeekerNextMove( seeker, wanderer )
			wanderer = self.getWandererNextMove( wanderer )



	def getSeekerNextMove(self, seeker, wanderer ):
		moves = self.getMoves( seeker, [self.seekerVisited] + [self.generalVisited])
		validMoves = []
		originalDistance = self.Manhattan( seeker, wanderer)
		validMoves = list(filter(lambda point: self.Manhattan(point,wanderer) < originalDistance, moves))

		if len( validMoves ) == 0:
			if seeker in self.generalVisited:
				self.generalVisited += self.seekerVisited

			self.seekerVisited = []

			nextMove = random.randint(0, self.rows - 1), random.randint(0, self.columns - 1)

		else:
			
			nextMove = validMoves[random.randint(0, len(validMoves) - 1)]

		return nextMove

	def getWandererNextMove( self, wanderer ):
		moves = self.getMoves( wanderer, self.generalVisited )
		nextMove = None
		if len( moves ) == 0:
			nextMove = self.generalVisited[ random.randint(0, len(self.generalVisited) - 1)]
		else:
			nextMove = moves[random.randint(0, len(moves) - 1)]

		return nextMove

	def getMoves( self, pointer, visited):
		row, column = pointer
		options = [(row-1, column), (row+1, column), (row, column-1), (row, column+1)]
		return list( filter( lambda point: 0 <= point[0] < self.rows and 
										   0 <= point[1] < self.columns and 
							 			   point not in visited and 
										   self.level[point[0]][point[1]],
							 options )
					)

	def printDungeon( self ):
		print("  " + "__" * self.columns)
		for row in self.level:
			print("|" + " ".join(['#' if x == True else ' ' if x == False else x if x in ['G','S'] else '.' for x in row]) + " |")
		print("͞ ͞" * self.columns * 2)
