import random

class DungeonGenerator:
	def __init__(self, rows, columns): 
		self.rows = rows
		self.columns = columns
		self.level = [[True for x in range(rows)] for y in range(columns)]
		self.seekerVisited = []
		self.generalVisisted = []
		wanderer = ( rows - 1, random.randint(0,columns - 1))
		seeker = ( 0, random.randint(0 , columns - 1))
		self.Manhattan = lambda pointA, pointB: abs( pointA[0] - pointB[0]) + abs( pointA[1] - pointB[1])
		self.generateSkeleton( wanderer, seeker)
		self.level[wanderer[0]][wanderer[1]] = 'S'
		self.level[seeker[0]][seeker[1]] = 'G'

	def generateSkeleton(self,  wanderer, seeker):
		
		while seeker not in self.generalVisisted:

			self.level[ seeker[0] ][ seeker[1] ] = False
			self.level[ wanderer[0] ][ wanderer[1] ] = False
			self.seekerVisited.append( seeker )
			self.generalVisisted.append( wanderer )

			seeker = self.getSeekerNextMove( seeker, wanderer )
			wanderer = self.getWandererNextMove( wanderer )


	def getSeekerNextMove(self, seeker, wanderer ):
		moves = self.getMoves( seeker, [self.seekerVisited] + [self.generalVisited])
		validMoves = []
		originalDistance = self.Manhattan( seeker, wanderer)
		validMoves = list(filter(lambda x: self.Manhattan(x,wanderer) < originalDistance, moves))

		if len( validMoves ) == 0:
			if seeker in self.generalVisited:
				self.generalVisited += self.seekerVisited

			self.seekerVisited = []

			nextMove = random.randint(0, self.rows - 1), random.randint(0, self.columns - 1)

		else:
			
			nextMove = validMoves[random.randint(0, len(validMoves) - 1)]

		return nextMove

	def Manhattan( pointA , pointB ):
		return 

	def getWandererNextMove( self, generalVisited, wanderer ):
		moves = self.getMoves( wanderer, generalVisited )
		nextMove = None
		if len( moves ) == 0:
			nextMove = generalVisited[ random.randint(0, len(generalVisited) - 1)]
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
					options ))

	def printMaze( self ):
		print("  " + "__" * self.columns)
		for row in self.level:
			print("|" + " ".join(['▣' if x == True else ' ' if x == False else x for x in row]) + "|")
		print("͞ ͞" * self.columns * 2)
