import constants
import linkedList
import expand
from priority_queue import PriorityQueue

def misplaced(puzzle):
    num_misplaced = 0
    for i in range(len(constants.board)):
        for j in range(len(constants.board)):
            if puzzle[i][j] != constants.goalBoard[i][j] and puzzle[i][j] != '*':
                num_misplaced += 1
    return num_misplaced

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


def manhattan(state):
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
    
    # Add linear conflict distance
    distance += linear_conflict(state, constants.goalBoard)
    
    return distance
    
def f(board):
        """ Heuristic Function to calculate hueristic value f(x) = h(x) + g(x) """
        return manhattan(board.data) + board.depth


def a_star(initialProblem, f):         
    initialNode = linkedList.Node(data = initialProblem)   # node←NODE(STATE=problem.INITIAL)
    frontier = PriorityQueue()   
    frontier.append((f(initialNode), initialNode))         # frontier←a priority queue ordered by f , with node as an element

    reached = {str(initialProblem): initialNode}           # reached←a lookup table, with one entry with key problem.INITIAL and value node

    while not frontier.empty():                            # while not IS-EMPTY(frontier) do
        node = frontier.get()                              # node←POP(frontier)
        
        if constants.goalBoard == node[1].data:            # if problem.IS-GOAL(node.STATE) 
            return node[1]                                 # then return node
        
        for child in expand.expand(node[1]):               # for each child in EXPAND(problem, node) do
            # s←child.STATE
            s =  linkedList.Node( data = child[0], depth = node[1].depth + 1, move = child[1], prev = node[1] )

            # if s is not in reached or child.PATH-COST < reached[s].PATH-COST then
            if str(s.data) not in reached or s.depth < reached[str(s.data)].depth:
                reached[str(s.data)] = s                   # reached[s]←child
                frontier.append((f(s) ,s))            # add child to frontier

    return constants.failure                              # return failure

def main():
    solution = a_star(constants.board, f)
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

main()

# puzzle =  [[2, 7, '*'], [5, 4, 3], [8, 1, 6]]
# print(linear_conflict(puzzle, constants.goalBoard))


# def linear_conflict_heuristic(current_state, goal_state):
#     conflicts = 0
#     goal_rows = []
#     goal_cols = []
#     for row in range(len(goal_state)):
#         rows = []
#         cols = []
#         for col in range(len(goal_state[row])):
#             rows.append(goal_state[row][col])
#             cols.append(goal_state[col][row])
#         goal_rows.append(rows)
#         goal_cols.append(cols)

#     for row in range(len(current_state)):
#         for col in range(len(current_state[row])-1):
#             for mid in range(col+1, len(current_state[row])):
#                 if current_state[row][col] != '*' \
#                     and current_state[row][mid] != '*' \
#                     and ((current_state[row][col] != goal_state[row][col]) or (current_state[row][mid] != goal_state[row][mid])) \
#                     and current_state[row][col] in goal_rows[row] \
#                     and current_state[row][mid] in goal_rows[row]:
#                     conflicts += 2
#                 if current_state[col][row] != '*' \
#                     and current_state[mid][row] != '*' \
#                     and ((current_state[col][row] != goal_state[col][row]) or (current_state[mid][row] != goal_state[mid][row])) \
#                     and current_state[col][row] in goal_cols[row] \
#                     and current_state[mid][row] in goal_cols[row]:
#                     conflicts += 2
#     return conflicts