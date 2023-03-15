# References: 
# 1. For algorithms of IDFS, DFS, BFS and A* ( Best first search ) - http://aima.cs.berkeley.edu/global-algorithms.pdf
# 2. Official textbook - http://lib.ysu.am/disciplines_bk/b7707dde83ee24b2b23999b4df5fd988.pdf
# 3. Python Code reference -  https://github.com/aimacode
# 4. Profiler reference - https://github.com/mirecl/pprof , https://pypi.org/project/memory-profiler/

import copy
import queue
import constants
from pprof import cpu
import memory_profiler 
cpu.auto_report()

board = constants.board
goalBoard = constants.goalBoard
failure =  constants.failure
cut_off =  constants.cut_off

class Node:
    def __init__(self, data, depth=0, move = None, prev = None):
        self.data = data   # Assign data
        self.depth = depth # Assign depth
        self.move = move   # Assign move performed 
        self.prev = prev   # Initialize prev as null
  
class LinkedList:
    def __init__(self):
        self.head = None

@cpu
def expand(board):
    for i in range(len(board.data)):                                # to find the location of * - NIL in current board
        for j in range(len(board.data[i])):
            if board.data[i][j] == '*':
                location = [i,j]; 
                break

    actions = []
    for move in possible_actions(constants.board, location):        # to find all possible actions
        actions.append([result(location, move, board.data) , move]) # prepare all possible boards from actions 

    return actions                                                  # After expanding return all possible boards

@cpu
def possible_actions(board, location):                              # to find all possible actions in current board
    actions = ["RIGHT","LEFT","UP","DOWN"]
    actionstopeform = []
    
    for x in actions:
        # for moving right 
        if x == "RIGHT":
            if location[1]+1 < len(board):
                actionstopeform.append([x,location[0],location[1]+1])
        # for moving left
        elif x == "LEFT":
            if location[1]-1 >= 0:
                actionstopeform.append([x,location[0],location[1]-1])
        # for moving up 
        elif x == "UP":
            if location[0]-1 >= 0:
                actionstopeform.append([x,location[0]-1,location[1]])
        # for moving down
        elif x == "DOWN":
            if location[0]+1 < len(board):
                actionstopeform.append([x,location[0]+1,location[1]])

    return actionstopeform

@cpu
def result(location,action,board):
    newBoard = copy.deepcopy(board)                             # copy of a board so that we can modify it 
    temp = copy.deepcopy(newBoard[action[1]][action[2]]) 
    newBoard[action[1]][action[2]] = copy.deepcopy('*')
    newBoard[location[0]][location[1]]  = copy.deepcopy(temp)
    return newBoard                                             # return new board after moving * - NIL to the new location 


# Reference : https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/
@cpu
def hasCycle(list):                                             # function to check if there is a cycle in a linked list
    s = set()
    temp = list
    while (temp):
        if (temp in s):
            return True
        s.add(temp)
        temp = temp.prev
    return False


# Iterative deepening search
@memory_profiler.profile
@cpu
def idfs(board,depth):                              # function ITERATIVE-DEEPENING-SEARCH(problem) returns a solution node or failure
    for step in range(depth):                       # for depth = 0 to ∞ do
        result = depthFirstSearch(board, step)      # result ← DEPTH-LIMITED-SEARCH(problem, depth)
        if(result != cut_off):                      # if result 6= cutoff 
            return result                           # then return result

# Depth first search
@cpu

def depthFirstSearch(board, step):                  # function DEPTH-LIMITED-SEARCH(problem, ℓ) returns a node or failure or cutof
    frontier = queue.LifoQueue()                    # frontier ← a LIFO queue (stack) with NODE(problem.INITIAL) as an element
    result = failure                                # result ← failure
    node = Node(data=board)
    frontier.put(node)  
    maxQueueSize =1                                 # only for debug

    while not frontier.empty():                     # while not IS-EMPTY(frontier ) do
        val = frontier.get()                        # node ← POP(frontier )
        if goalBoard == val.data:                   # if problem.IS-GOAL(node.STATE) then
            return val                              # return node
        if  val.depth > step:                       # if DEPTH(node) > ℓ then
            result = cut_off                        # result ← cutoff
        elif not hasCycle(val):                     # else if not IS-CYCLE(node) do
            for child in expand(val):               # for each child in EXPAND(problem, node) do
                temp =  Node(data=child[0], depth =val.depth + 1 ,move= child[1] , prev=val)    
                frontier.put(temp)                  # add child to frontier
                maxQueueSize+=1                     # only for debug
    
    #print('Max queue size:', maxQueueSize)         # only for debug
    return result                                   # return result

@cpu
def printStatistics(solution):
    pathCost = 0
    stateSequence = []
    actionSequence = []

    while solution.prev != None:
        stateSequence.insert(0, solution.data)
        actionSequence.insert(0, solution.move)
        solution = solution.prev
        pathCost += 1

    print('Action sequence:')
    print(*actionSequence, sep='\n')

    print('\nState sequence:')
    print(*stateSequence, sep='\n')

    print('\nPath cost:', pathCost)


printStatistics(idfs(board, 50))