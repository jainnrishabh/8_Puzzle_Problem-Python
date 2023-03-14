import copy
import constants
from pprof import cpu
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

       
class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.size = 0

    def append(self, item):
        priority, state = item
        index = len(self.heap)
        for idx, (p, s) in enumerate(self.heap):
            if priority < p:
                index = idx
                break
        self.heap.insert(index, item)
        self.size += 1
            
    def get(self):
        return self.heap.pop(0)
    
    def getSize(self):
        return self.size
        
    def empty(self):
	    return len(self.heap) == 0 

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


@cpu 
def misplaced(puzzle):
    num_misplaced = 0
    for i in range(len(puzzle.data)):
        for j in range(len(puzzle.data)):
            if puzzle.data[i][j] != constants.goalBoard[i][j] and puzzle.data[i][j] != '*':
                num_misplaced += 1
    return num_misplaced


@cpu
def linear_conflict(board, goal):
    n = len(board)
    linear_conflicts = 0
    
    # Find the linear conflicts in rows
    for i in range(n):
        row = board[i]
        goal_row = goal[i]
        for j in range(n):
            if row[j] != '*' and row[j] in goal_row:
                for k in range(j+1, n):
                    if row[k] != '*' and row[k] in goal_row and goal_row.index(row[j]) > goal_row.index(row[k]):
                        linear_conflicts += 2
                        
    # Find the linear conflicts in columns
    for j in range(n):
        column = [board[i][j] for i in range(n)]
        goal_column = [goal[i][j] for i in range(n)]
        for i in range(n):
            if column[i] != '*' and column[i] in goal_column:
                for k in range(i+1, n):
                    if column[k] != '*' and column[k] in goal_column and goal_column.index(column[i]) > goal_column.index(column[k]):
                        linear_conflicts += 2
                        
    return linear_conflicts

@cpu
def manhattan(state):
    state = state.data
    goal_state = constants.goalBoard
    distance = 0
    
    # Create a dictionary that maps each value to its position in the goal state
    goal_dict = {}
    for i in range(len(goal_state)):
        for j in range(len(goal_state[0])):
            if goal_state[i][j] != '*':
                goal_dict[goal_state[i][j]] = (i, j)
    
    # Calculate Manhattan distance
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] != '*' and state[i][j] != goal_state[i][j]:
                value = state[i][j]
                row, col = goal_dict[value]
                distance += abs(row - i) + abs(col - j)
    
    return distance

@cpu
def f(board):
        """ Heuristic Function to calculate hueristic value f(x) = h(x) + g(x) """
        manhattan_distance = manhattan(board)
        # Add linear conflict distance
        manhattan_distance += linear_conflict(board.data, constants.goalBoard)
        return manhattan_distance + board.depth


@cpu
def a_star(initialProblem, f):         
    initialNode = Node(data = initialProblem)               # node←NODE(STATE=problem.INITIAL)
    frontier = PriorityQueue()   
    frontier.append((f(initialNode), initialNode))          # frontier←a priority queue ordered by f , with node as an element

    reached = {str(initialProblem): initialNode}            # reached←a lookup table, with one entry with key problem.INITIAL and value node

    while not frontier.empty():                             # while not IS-EMPTY(frontier) do
        node = frontier.get()                               # node←POP(frontier)
        
        if constants.goalBoard == node[1].data:             # if problem.IS-GOAL(node.STATE) 
            #print('Max queue size:', frontier.getSize())   # only for debug
            return node[1]                                  # then return node
        
        for child in expand(node[1]):                       # for each child in EXPAND(problem, node) do
            # s←child.STATE
            s =  Node( data = child[0], depth = node[1].depth + 1, move = child[1], prev = node[1] )

            # if s is not in reached or child.PATH-COST < reached[s].PATH-COST then
            if str(s.data) not in reached or s.depth < reached[str(s.data)].depth:
                reached[str(s.data)] = s                    # reached[s]←child
                frontier.append((f(s) ,s))                  # add child to frontier

    return constants.failure                                # return failure


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



printStatistics(a_star(constants.board, f))