from functions import *
from algorithms import *


while (True):
    print('How would you like to initialize the puzzle ?')
    print('1) Enter a puzzle to solve')
    print('2) initialize random puzzle')
    print('3) exit program')
    initialize = input('Choice: ')
    if initialize == '1':
        randomState = input('Puzzle: ')
    elif initialize == '2':
        randomState = generateRandomState()
    elif initialize == '3':
        break
    print('Solving: ')
    printBoard(randomState)
    if not isSolvable(randomState):
        print('This state is Unsolvable! (Odd number of inversions)')
    else:
        print('Select Method:')
        print('1) BFS')
        print('2) DFS')
        print('3) A* (Manhattan Distance Heuristic)')
        print('4) A* (Euclidean Distance Heuristic)')
        choice = input('Choice: ')
        print('Do you want to print the steps ?')
        print('1) Yes')
        print('2) No')
        steps = input('answer: ')
        if choice == '1':
            BFS(randomState, steps)
        elif choice == '2':
            DFS(randomState, steps)
        elif choice == '3':
            A_Star(randomState, manhattanHeuristic, steps)
        elif choice == '4':
            A_Star(randomState, euclideanHeuristic, steps)
    print('-----------------------------------------------')
