import constants
import linkedList
import expand
from priority_queue import PriorityQueue

def misplaced(puzzle):
    num_misplaced = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != constants.goalBoard[i][j] and puzzle[i][j] != '*':
                num_misplaced += 1
    return num_misplaced


def manhattan(state):
    result = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if (constants.goalBoard[i][j] == '*'):
                continue
            for l in range(len(state)):
                for m in range(len(state[i])):
                    if (constants.goalBoard[i] [j] == state[l][m]):
                        result += (abs (m - j) + abs (l - i))
                        break
    return result


def a_star(initialProblem, f):         
    initialNode = linkedList.Node(data = initialProblem)  # node←NODE(STATE=problem.INITIAL)
    frontier = PriorityQueue()   
    frontier.append((f(initialProblem), initialNode))      # frontier←a priority queue ordered by f , with node as an element

    reached = {str(initialProblem): initialNode}           # reached←a lookup table, with one entry with key problem.INITIAL and value node

    while not frontier.empty():                           # while not IS-EMPTY(frontier) do
        node = frontier.get()                             # node←POP(frontier)
        
        if constants.goalBoard == node[1].data:           # if problem.IS-GOAL(node.STATE) 
            return node[1]                                # then return node
        
        for child in expand.expand(node[1]):              # for each child in EXPAND(problem, node) do
            # s←child.STATE
            s =  linkedList.Node( data = child[0], depth = node[1].depth + 1, move = child[1], prev = node[1] )

            # if s is not in reached or child.PATH-COST < reached[s].PATH-COST then
            if str(s.data) not in reached or s.depth < reached[str(s.data)].depth:
                reached[str(s.data)] = s                  # reached[s]←child
                frontier.append((f(s.data),s))            # add child to frontier

    return constants.failure                              # return failure


solution = a_star(constants.board, misplaced)
print(solution)

stateSequence = []
actionSequence = []

while solution != None:
    stateSequence.insert(0, solution.data)
    actionSequence.insert(0, solution.move)
    solution = solution.prev

print('Action sequence:')
print(*actionSequence, sep='\n')

print('\nState sequence:')
print(*stateSequence, sep='\n')

# print('\nPath cost:', pathCost)