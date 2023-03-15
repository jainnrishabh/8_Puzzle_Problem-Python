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

@memory_profiler.profile
@cpu
def bfs(board):                                                 # function BREADTH-FIRST-SEARCH(problem) returns a solution node or failure
    frontier = queue.Queue()
    node = Node(data = board)                                   # node ← NODE(problem.INITIAL)
    frontier.put(node)                                          # frontier ← a FIFO queue, with node as an element
    # maxQueueSize = 1                                          # only for debug
    if constants.goalBoard == node.data:                        # if problem.IS-GOAL(node.STATE) 
        return node                                             # then return node
    reached = []
    reached.append(board)                                       # reached ← {problem.INITIAL}
    while not frontier.empty():                                 # while not IS-EMPTY(frontier ) do
        val = frontier.get()                                    # node ← POP(frontier )
        for child in expand(val):                               # for each child in EXPAND(problem, node) do
            s =  Node(data=child[0], depth = val.depth + 1, move= child[1] , prev=val)      # s ← child.STATE
            if goalBoard == s.data:                             # if problem.IS-GOAL(s) 
                #print('Max queue size:', maxQueueSize)         # only for debug
                return s                                        # then return child
            if s.data not in reached:                           # if s is not in reached then
                reached.append(s.data)                          # add s to reached
                frontier.put(s)                                 # add child to frontier
                # maxQueueSize+=1                               # only for debug
    #print('Max queue size:', maxQueueSize)                     # only for debug
    return failure                                              # return failure

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


printStatistics(bfs(board))