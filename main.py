#https://patorjk.com/software/taag/#p=display&f=Nancyj-Underlined&t=8%20Puzzle
# font = Nancyj-Underlined

import random
from AStar.AStar8Puzzle import AStar8Puzzle
from AStar import AStarMaze
from AStar.PuzzlePoint import PuzzlePoint
from AStar.MazeGenerator import MazeGenerator
from AStar.DungeonPoint import DungeonPoint
from os import system
import random


def __main__():
	system("clear")
	welcomeMessage = """
	
	     dP   dP   dP          dP                                            dP                         
         88   88   88          88                                            88                           
         88  .8P  .8P .d8888b. 88 .d8888b. .d8888b. 88d8b.d8b. .d8888b.    d8888P .d8888b.                
         88  d8'  d8' 88ooood8 88 88'  `"" 88'  `88 88'`88'`88 88ooood8      88   88'  `88                
         88.d8P8.d8P  88.  ... 88 88.  ... 88.  .88 88  88  88 88.  ...      88   88.  .88                
         8888' Y88'   `88888P' dP `88888P' `88888P' dP  dP  dP `88888P'      dP   `88888P'                
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo   
                                                                                                          
 .d888888  dP     888888ba  dP                                                                      dP    
d8'    88  88     88    `8b 88                                                                      88    
88aaaaa88a 88    a88aaaa8P' 88 .d8888b. dP    dP .d8888b. 88d888b. .d8888b. dP    dP 88d888b. .d888b88    
88     88  88     88        88 88'  `88 88    88 88'  `88 88'  `88 88'  `88 88    88 88'  `88 88'  `88    
88     88  88     88        88 88.  .88 88.  .88 88.  .88 88       88.  .88 88.  .88 88    88 88.  .88    
88     88  dP     dP        dP `88888P8 `8888P88 `8888P88 dP       `88888P' `88888P' dP    dP `88888P8    
ooooooooooooooooooooooooooooooooooooooooo~~~~.88~o~~~~.88~oooooooooooooooooooooooooooooooooooooooooooooooo
                                         d8888P   d8888P                                                  
	"""
	print(welcomeMessage)
	option = 0

	while option != "-1":

		print("Type the number of what you would like to do. The menu is the following:")
		print(" 1 --> A* search")
		print("-1 --> exit")

		option = input()
		if option == "1":
			AStarMenu()
			
		elif option == "-1":
			break
		
		else:
			invalidOption(__main__)

	print(" Thank you using my app! I hope that you have a great day ^-^")


def invalidOption( menuToReturnTo ):
	print("please enter a valid option")
	print("press enter to continue")
	input()
	menuToReturnTo()

def AStarMenu():
	system("clear")
	welcomeMessage = """
.d888888  .d88888b    dP                        8888ba.88ba                             
d8'    88  88.    "'   88                        88  `8b  `8b                            
88aaaaa88a `Y88888b. d8888P .d8888b. 88d888b.    88   88   88 .d8888b. 88d888b. dP    dP 
88     88        `8b   88   88'  `88 88'  `88    88   88   88 88ooood8 88'  `88 88    88 
88     88  d8'   .8P   88   88.  .88 88          88   88   88 88.  ... 88    88 88.  .88 
88     88   Y88888P    dP   `88888P8 dP          dP   dP   dP `88888P' dP    dP `88888P' 
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
                                                                        																		"""
	print(welcomeMessage)
	print("Menu: type the character of what you would like to do")
	print("1 --> 8 Puzzle")
	print("2 --> Shortest path from entrance to exit on a random generated maze")
	print( "-1 --> return" )
	menuOption = input()
			
	if menuOption == '1':
		EightPuzzleSolver()
	
	elif menuOption == '2':
		ShortestPathToExitMaze()
	
	elif menuOption == "-1":
		__main__()

	else:
		invalidOption(  AStarMenu  )

def EightPuzzleSolver():
	system("clear")
	welcomeMessage = """
.d888b.     888888ba                             dP          
Y8' `8P     88    `8b                            88          
d8bad8b    a88aaaa8P' dP    dP d888888b d888888b 88 .d8888b. 
88` `88     88        88    88    .d8P'    .d8P' 88 88ooood8 
8b. .88     88        88.  .88  .Y8P     .Y8P    88 88.  ... 
Y88888P     dP        `88888P' d888888P d888888P dP `88888P' 
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo"""
	print(welcomeMessage)
	print("Menu")
	print("1 --> random initial board and random target board")
	print("2 --> input the initial and target board")
	print("-1 --> return to A* menu")
	option = input()
	if option == '1':
		EightPuzzleSolverRandomHelper()

	elif option == '2':
		EightPuzzleSolverCustomHelper()
	
	elif option == '-1':
		AStarMenu()
	else:
		invalidOption(EightPuzzleSolver)	

def EightPuzzleSolverRandomHelper():
	initialBoard = [[0,0,0],[0,0,0],[0,0,0]]
	targetBoard = [[0,0,0],[0,0,0],[0,0,0]]
	initialOptions = [1,2,3,4,5,6,7,8,""]
	targetOptions = [1,2,3,4,5,6,7,8,""]
	for row in range(3):
		for column in range(3):
			initialElement = initialOptions.pop(random.randint(0,len(initialOptions) - 1))
			targetElement = targetOptions.pop(random.randint(0,len(targetOptions) - 1))
				
			initialBoard[row][column] = initialElement
			targetBoard[row][column] = targetElement
			if initialElement == "":
				emptyRow = row
				emptyColumn = column

	start = PuzzlePoint(initialBoard,emptyRow, emptyColumn ,float('inf'),1, targetBoard)
	end = PuzzlePoint(targetBoard, emptyRow,emptyColumn,float('inf'),1,targetBoard)
	print("INITIAL BOARD")
	start.printSolution( clear = False)
	print("\n\nTARGET BOARD")
	end.printSolution( clear = False)
	maxIterations = int(input("Type the maximum amount of iterations to attemp before stopping the search.\n I recommend 1000 as the minimum amount of iterations\n"))
	print("Please wait, it may take some time")
	AStar8Puzzle(start, maxIterations)
	EightPuzzleSolver()


def EightPuzzleSolverCustomHelper():
	print("You will decide what the initial state and goal state are. Remember that this each board is a 3 x 3 matrix.")
	option = 'no'
	while option == 'no':
		print("Type the initial  state. Mark the empty cell with an underscore character ( _ )")
		initialState,emptyRow, emptyCol =EightPuzzleInputHelper()
		print("Type the goal  state. Mark the empty cell with an underscore character ( _ )")
		goalState, _ , _ = EightPuzzleInputHelper()
		start = PuzzlePoint( initialState, emptyRow, emptyCol,  float('inf'), 1, goalState)
		end = PuzzlePoint( goalState, emptyRow, emptyCol,  float('inf'), 1, goalState)
		print("INITIAL BOARD")
		start.printSolution( clear = False)
		print("\n\nTARGET BOARD")
		end.printSolution( clear = False)
		print("Do you want to proceed, or would you like to retype the initial and end state?")
		print(" yes --> continue")
		print(" no --> type the initial and goal state again")
		option = input()
	maxIterations = int(input("Type the maximum amount of iterations to attemp before stopping the search.\n I recommend 1000 as the minimum amount of iterations\n"))
	print("Please wait, it may take some time")
	AStar8Puzzle(start, maxIterations)
	EightPuzzleSolver()

	

def EightPuzzleInputHelper():
	print("Type the first row")
	rowA = input().split(' ')
	print("Type the second row")
	rowB = input().split(' ')
	print("Type the third row")
	rowC = input().split(' ')
	board = []

	EightPuzzleInputHelperHelper(board,rowA)
	EightPuzzleInputHelperHelper(board,rowB)
	EightPuzzleInputHelperHelper(board,rowC)
	for row in range(3):
		for col in range(3):
			if board[row][col] == "":
				return board, row, col
	return board, None,None

def EightPuzzleInputHelperHelper(board, row):
	board.append([int(elem) if elem != "_" else "" for elem in row] )


def ShortestPathToExitMaze():
	system("clear")
	welcomeMessage = """
 888888ba                          dP                        8888ba.88ba                             
 88    `8b                         88                        88  `8b  `8b                            
a88aaaa8P' .d8888b. 88d888b. .d888b88 .d8888b. 88d8b.d8b.    88   88   88 .d8888b. d888888b .d8888b. 
 88   `8b. 88'  `88 88'  `88 88'  `88 88'  `88 88'`88'`88    88   88   88 88'  `88    .d8P' 88ooood8 
 88     88 88.  .88 88    88 88.  .88 88.  .88 88  88  88    88   88   88 88.  .88  .Y8P    88.  ... 
 dP     dP `88888P8 dP    dP `88888P8 `88888P' dP  dP  dP    dP   dP   dP `88888P8 d888888P `88888P' 
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
	"""
	print(welcomeMessage)
	print("LEVEL INFORMATION")
	print("S --> start point")
	print("G --> goal point")
	print("  --> walkable space")
	print("x --> obstacle")
	print("Menu")
	print("1 --> Random dungeon of a fixed size")
	print("2 --> Random maze (you can decide the amount of rows and columns that it will have)")
	print("-1 --> return")
	option = input()

	if option == '1':
		randomDungeon()
	elif option == '2':
		randomMaze()
	elif option == '-1':
		AStarMenu()
	else:
		invalidOption( ShortestPathToExitMaze)


def randomDungeon():
	rows = 20
	columns = 40
	level  = [   [  '1' for col in range( columns * 2) ] for row in range(rows * 2) ]
	
	option = "no"
	while option == "no":
		system("clear")
		#Bottom Left Matrix
		seekerDownLeft = (0, random.randint(0, columns - 1))
		wandererDownLeft = ( rows - 1 , random.randint(0, columns - 1))

		#Top Left Matrix
		wandererTopLeft = (rows - 1, seekerDownLeft[1])
		seekerTopLeft = (random.randint(0, rows - 1), columns - 1)

		#Top Right Matrix
		wandererTopRight = ( seekerTopLeft[0], 0)
		seekerTopRight =  ( rows - 1, random.randint(0, columns - 1))

		#Bottom Right Matrix
		wandererDownRight = ( 0, seekerTopRight[1])
		seekerDownRight = ( rows - 1 , random.randint(0, columns - 1 ))


		upLeft = MazeGenerator(rows,columns, wanderer = wandererTopLeft, seeker = seekerTopLeft, showStart = False, showEnd = False)
		upRight = MazeGenerator(rows,columns, wanderer= wandererTopRight, seeker = seekerTopRight, showStart = False, showEnd = False)
		downLeft = MazeGenerator(rows,columns, wanderer = wandererDownLeft, seeker = seekerDownLeft, showStart = True, showEnd = False)
		downRight = MazeGenerator(rows,columns, wanderer = wandererDownRight, seeker = seekerDownRight, showStart = False, showEnd = True)

		for currentRow in range( rows ):
			for currentCol in range( columns ):
				level[currentRow][currentCol] = upLeft.level[ currentRow ][ currentCol ]
				level[ currentRow][currentCol + columns ] = upRight.level[ currentRow ][currentCol ]
				level[ currentRow + rows ][ currentCol ] = downLeft.level[ currentRow ][ currentCol ]
				level[ currentRow + rows ] [ currentCol + columns ] = downRight.level [ currentRow ][ currentCol ]

		print("  " + "__" * columns * 2)
		for levelRow in level:
			print("|" + " ".join(['x' if x == True else ' ' if x == False else x for x in levelRow]) + " |")
		print("͞ ͞" * columns * 4)

		
		
		print("If you like this dungeon type \"yes\" if not type \"no\" to generate a new dungeon")
		option = input()
	print("Do you want to visualize how A* searches the best path?")
	print(" 1 --> yes")
	print(" 2 --> no")
	option = input()
	visualizeSearch = option == '1'
	point = DungeonPoint( (rows * 2 ) - 1, wandererDownLeft[1],0,0)
	AStarMaze(point, level, ((rows * 2) - 1, seekerDownRight[1] + columns), visualizeSearch )
	ShortestPathToExitMaze()

def randomMaze():
	print("Type the amount of rows followed by the amount of columns that you want the maze to have. Separat the values with a space. I recommend the minimum number to be 10")


	levelSize = input().split(" ")
	rows = int(levelSize[0])
	columns = int(levelSize[1])
	option = "no"
	while option == "no":
		maze = MazeGenerator(rows,columns)
		maze.printDungeon()
		
		print("If you like this maze type \"yes\" if not type \"no\" to generate a new dungeon")
		option = input()
	print("Do you want to visualize how A* searches the best path?")
	print(" 1 --> yes")
	print(" 2 --> no")
	option = input()
	visualizeSearch = option == '1'
	point = DungeonPoint( maze.wanderer[0], maze.seeker[1], 0,0 )
	AStarMaze( point, maze.level, maze.seeker, visualizeSearch)

	ShortestPathToExitMaze()

	
	
if __name__=="__main__":
	__main__()




				
