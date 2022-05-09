from functions import *
import time


def A_Star(boardState, heuristic, print_flag):
    maxDep = 0
    Start_time = time.time()
    frontier = []  # Frontier list
    oFrontier = set()  # Optimizing Frontier with datatype 'set()' rather than 'list' used to improve search time
    explored = set()
    frontier.append([boardState, heuristic(boardState), 0])  # appending board state, heuristic, depth
    oFrontier.add(boardState)
    pMap = {boardState: boardState}
    while len(frontier):
        frontier.sort(key=lambda x: (x[1], x[0]))  # sorting heap ascending according to total cost
        state = frontier.pop(0)  # Pop first element from the list (to imitate queue)
        oFrontier.remove(state[0])  # Remove the same element from the optimizing frontier set
        explored.add(state[0])
        if isGoal(state[0]):  # if current state is the goal state --> break
            maxDep = max(maxDep, state[2])
            break
        children = getChildren(state[0])  # Get all children of current state
        for child in children:
            if child in oFrontier:  # if child in frontier
                temp = 0
                for i in range(len(frontier)):
                    if frontier[i][0] == child:  # get child from frontier list
                        temp = frontier[i][1]  # store the total cost of child
                        break
                if temp > heuristic(child) + state[2] + 1:  # if total cost of child is smaller than the current cost
                    pMap[frontier[i][0]] = state[0]  # update child's parent
                    frontier[i][1] = heuristic(child) + state[2] + 1  # update child's total cost
                    frontier[i][2] = state[2] + 1  # update child's current level
            elif child not in oFrontier and child not in explored:  # search for each child in frontier and explored
                maxDep = max(maxDep,
                             state[2])  # maximum depth is the max of current max depth or level of current state
                frontier.append([child, heuristic(child) + state[2] + 1,
                                 state[2] + 1])  # if not found add child to frontier and oFrontier
                oFrontier.add(child)
                pMap[child] = state[0]  # Store the child with the current state as the parent node
    end_time = time.time()  # Ending Time
    path = findPath(pMap)  # Traverse through the dictionary to find the path of the goal state
    path.reverse()
    if print_flag == '1':
        for i in range(len(path)):  # Print each state in the path
            print(f'Step Number: {i + 1}')
            printBoard(path[i])
    print(f'Cost of Path = {len(path) - 1}')  # cost of path equal number of state changes in path to goal state
    print(f'Number of Nodes Expanded = {len(explored)}')
    print(f'Depth of Search = {maxDep}')  # depth of search equal cost since the tree is checked level by level
    print(f'A* Running time = {end_time - Start_time} sec')  # Execution time = Ending time - Starting Time
    print('Starting Board State: ')
    printBoard(boardState)


# Breadth-First-Search Algorithm
def BFS(boardState, print_flag):
    maxDep = 0
    time1 = time.time()  # Starting time
    frontier = []  # Frontier list
    oFrontier = set()  # Optimizing Frontier with datatype 'set()' rather than 'list' used to improve search time
    explored = set()
    frontier.append([boardState, 0])
    oFrontier.add(boardState)
    pMap = {boardState: boardState}  # Dictionary used to link each node with its parent in the form (child: parent)
    while len(frontier):
        state = frontier.pop(0)  # Pop first element from the list (to imitate queue)
        oFrontier.remove(state[0])  # Remove the same element from the optimizing frontier set
        explored.add(state[0])
        if isGoal(state[0]):  # if current state is the goal state --> break
            maxDep = max(maxDep, state[1])
            break
        children = getChildren(state[0])  # Get all children of current state
        for child in children:
            if child not in oFrontier and child not in explored:  # search for each child in frontier and explored
                maxDep = max(maxDep,
                             state[1])  # maximum depth is the max of current max depth or level of current state
                frontier.append([child, state[1] + 1])  # if not found add child to frontier and oFrontier
                oFrontier.add(child)
                pMap[child] = state[0]  # Store the child with the current state as the parent node
    time2 = time.time()  # Ending Time
    path = findPath(pMap)  # Traverse through the dictionary to find the path of the goal state
    path.reverse()
    if print_flag == '1':
        for i in range(len(path)):  # Print each state in the path
            print(f'Step Number: {i + 1}')
            printBoard(path[i])
    print(f'Cost of Path = {len(path) - 1}')  # cost of path equal number of state changes in path to goal state
    print(f'Number of Nodes Expanded = {len(explored)}')
    print(f'Depth of Search = {maxDep}')  # depth of search equal cost since the tree is checked level by level
    print(f'BFS Running time = {time2 - time1} sec')  # Execution time = Ending time - Starting Time
    print('Starting Board State: ')
    printBoard(boardState)


# Depth-First-Search Algorithm
def DFS(boardState, print_flag):
    maximumDepth = 0
    time1 = time.time()  # Starting time
    frontier = []  # Frontier list
    oFrontier = set()  # Optimizing Frontier with datatype 'set()' rather than 'list' used to improve search time
    explored = set()
    frontier.append([boardState, 0])
    oFrontier.add(boardState)
    pMap = {boardState: boardState}  # Dictionary used to link each node with its parent in the form (child: parent)
    while len(frontier):
        state = frontier.pop()  # Pop last element from the list (to imitate stack)
        oFrontier.remove(state[0])  # Remove the same element from the optimizing frontier set
        explored.add(state[0])
        if isGoal(state[0]):  # if current state is the goal state --> break
            maximumDepth = max(maximumDepth, state[1])
            break
        children = getChildren(state[0])  # Get all children of current state
        for child in children:
            if child not in oFrontier and child not in explored:  # search for each child in frontier and explored
                maximumDepth = max(maximumDepth,
                                   state[1])  # maximum depth is the max of current max depth or level of current state
                frontier.append([child, state[1] + 1])  # if not found add child to frontier and oFrontier
                oFrontier.add(child)
                pMap[child] = state[0]
    time2 = time.time()  # Ending Time
    path = findPath(pMap)  # Traverse through the dictionary to find the path of the goal state
    path.reverse()
    if print_flag == '1':
        for i in range(len(path)):  # Print each state in the path
            print(f'Step Number: {i + 1}')
            printBoard(path[i])
    print(f'Cost of Path = {len(path) - 1}')  # cost of path equal number of state changes in path to goal state
    print(f'Number of Nodes Expanded = {len(explored)}')
    print(f'Depth of Search = {maximumDepth}')
    print(f'DFS Running time = {time2 - time1} sec')  # Execution time = Ending time - Starting Time
    print('Starting Board State: ')
    printBoard(boardState)
