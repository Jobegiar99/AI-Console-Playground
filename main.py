import random
from AStar import AStar
from PuzzlePoint import PuzzlePoint
from MazeGenerator import MazeGenerator
from os import system, name


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
	option = input()
	if option == '1':
		EightPuzzleSolverRandomHelper()

	if option == '2':
		return
		
	
	
	

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
	AStar(start, maxIterations)

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
	print("Type the amount of rows and then the amount of columns that you want the maze to have. I recommend the minimum number to be 10")
	print("LEVEL INFORMATION")
	print("S --> start point")
	print("G --> goal point")
	print("  --> walkable space")
	print("▣ --> obstacle")
	levelSize = input().split(" ")
	rows = int(levelSize[0])
	columns = int(levelSize[1])
	option = "no"
	while option == "no":
		maze = MazeGenerator(rows,columns)
		maze.printDungeon()
		
		print("If you like this maze type \"yes\" if not type \"no\" to generate a new dungeon")
		option = input()
	

	
	
if __name__=="__main__":
	__main__()




				
