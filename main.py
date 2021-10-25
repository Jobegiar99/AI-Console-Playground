import random
from AStar import AStar
from PuzzlePoint import PuzzlePoint
from os import system, name


def __main__():
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
			invalidOption()

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
	print("a --> 8 Puzzle")
	print("b --> Shortest path from entrance to exit on a random generated dungeon")
	print( "-1 --> return" )
	menuOption = input()
			
	if menuOption == 'a':
		EightPuzzleSolver()
	
	elif menuOption == 'b':
		ShortestPathToExitDungeon()

	else:
		invalidOption(  AStarMenu  )

def EightPuzzleSolver():
	board = [[0,0,0],[0,0,0],[0,0,0]]
	options = [1,2,3,4,5,6,7,8,""]
	emptyRow = 0
	emptyColumn = 0
	maxIterations = int(input("Type the maximum amount of iterations to attemp before stopping the search.\n I recommend 1000 as the minimum amount of iterations\n"))
	for row in range(3):
		for column in range(3):
			element = options.pop(random.randint(0,len(options) - 1))
			board[row][column] = element
			if element == "":
				emptyRow = row
				emptyColumn = column
	for row in board:
		print("|".join([str(r) if r != '' else ' ' for r in row]))
	start = PuzzlePoint(board,emptyRow, emptyColumn ,float('inf'),1)
	print("Please wait, it may take some time")
	AStar(start, maxIterations)

def ShortestPathToExitDungeon()

if __name__=="__main__":
	__main__()




				
