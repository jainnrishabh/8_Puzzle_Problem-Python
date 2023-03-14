Part 1 [481: 10 pts; 681: 9 pts]
Write a function possible-actions that takes a board as input and outputs a list of all actions possible on the given board.1

puzzle_0 = [[3,1,2],[7,'*',5],[4,6,8]]

def possible_actions(board, location):
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

print(possible_actions(puzzle_0, [1,1]))

Output : 
[['RIGHT', 1, 2], ['LEFT', 1, 0], ['UP', 0, 1], ['DOWN', 2, 1]]


--------------------------------------------------------------------------------------------------------------------------------

Part 2 [481: 10 pts; 681: 9 pts]
Write a function result that takes as input an action and a board and outputs the new board that will result after actually carrying out the input move in the input state. Be certain that you do not accidentally modify the input board variable.2

puzzle_0 = [[3,1,2],[7,'*',5],[4,6,8]]

def result(location,action,board):
    # copy of a board so that we can modify it 
    newBoard = copy.deepcopy(board)
    temp = copy.deepcopy(newBoard[action[1]][action[2]]) 
    newBoard[action[1]][action[2]] = copy.deepcopy('*')
    newBoard[location[0]][location[1]]  = copy.deepcopy(temp)
    # return new board after moving * - NIL to the new location 
    return newBoard

print(result([1,1],['RIGHT', 1, 2], puzzle_0))

Output: 
[[3, 1, 2], [7, 5, '*'], [4, 6, 8]]

--------------------------------------------------------------------------------------------------------------------------------

Part 3 [481: 5 pts; 681: 4pts]
Write a function expand that takes a board as input, and outputs a list of all states that can be reached in one Action from the given state.

The expand function makes use of possible actions and result functions to generate all possible states that can be reached

def expand(board):
    for i in range(len(board.data)):
        for j in range(len(board.data[i])):
            if board.data[i][j] == '*':
                location = [i,j]; 
                break

    actions = []
    for move in possible_actions(constants.board, location):
        actions.append([result(location, move, board.data) , move])

    return actions

print(expand(Node(data = constants.board)))

Output: 

[[[[3, 1, 2], [7, 5, '*'], [4, 6, 8]], ['RIGHT', 1, 2]], [[[3, 1, 2], ['*', 7, 5], [4, 6, 8]], ['LEFT', 1, 0]], [[[3, '*', 2], [7, 1, 5], [4, 6, 8]], ['UP', 0, 1]], [[[3, 1, 2], [7, 6, 5], [4, '*', 8]], ['DOWN', 2, 1]]]

---------------------------------------------------------------------------------------------------------------------------------

Part 4 [481: 15 pts; 681: 14 pts]
Implement an iterative deepening search which takes an initial board and a goal  board  and produces a list of actions that  form  an  optimal  path  from  the  initial  board  to  the  goal.  Test your search on *puzzle-0*. You can try running it on some of the other puzzles, but don’t feel discouraged if it takes a very long time before returning an answer.

import copy
import queue

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

def hasCycle(list):
    s = set()
    temp = list
    while (temp):
        if (temp in s):
            return True
        s.add(temp)
        temp = temp.prev
    return False

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

# Iterative deepening search
def idfs(board,depth):
    for step in range(depth):
        result = depthFirstSearch(board, step)
        if(result != cut_off): 
            return result

def depthFirstSearch(board, step):
    result = failure
    frontier = queue.LifoQueue()
    node = Node(data=board)
    frontier.put(node)

    while not frontier.empty():
        val = frontier.get()
        if goalBoard == val.data:
            return val
        if  val.depth > step:
            result = cut_off
        elif not hasCycle(val):
            for child in expand(val):
                temp =  Node(data=child[0], depth =val.depth + 1 ,move= child[1] , prev=val)
                frontier.put(temp)
    return result

printStatistics(idfs(board,50))

Output: 

Action sequence:
['LEFT', 1, 0]
['DOWN', 2, 0]
['RIGHT', 2, 1]
['UP', 1, 1]
['LEFT', 1, 0]
['UP', 0, 0]

State sequence:
[[3, 1, 2], ['*', 7, 5], [4, 6, 8]]
[[3, 1, 2], [4, 7, 5], ['*', 6, 8]]
[[3, 1, 2], [4, 7, 5], [6, '*', 8]]
[[3, 1, 2], [4, '*', 5], [6, 7, 8]]
[[3, 1, 2], ['*', 4, 5], [6, 7, 8]]
[['*', 1, 2], [3, 4, 5], [6, 7, 8]]

Path cost: 6


Part 5 [481: 15 pts; 681: 13 pts]
Implement a breadth-first search which, like the iterative deepening search, takes an initial board and a goal and gives an optimal sequence of actions from the initial state to the goal. Test your search on *puzzle-0* and *puzzle-1*.

def bfs(board):
    frontier = queue.Queue()
    node = linkedList.Node(data = board)
    frontier.put(node)
    if constants.goalBoard == node.data:
        return node
    
    reached = []
    reached.append(board)

    while not frontier.empty():
        val = frontier.get()
        for child in expand.expand(val):
            s =  linkedList.Node(data=child[0], depth = val.depth + 1, move= child[1] , prev=val)
            
            if goalBoard == s.data: 
                return s
            if s.data not in reached:
                reached.append(s.data)
                frontier.put(s)
                
    return failure

Output:

Action sequence:
['LEFT', 1, 0]
['DOWN', 2, 0]
['RIGHT', 2, 1]
['UP', 1, 1]
['LEFT', 1, 0]
['UP', 0, 0]

State sequence:
[[3, 1, 2], ['*', 7, 5], [4, 6, 8]]
[[3, 1, 2], [4, 7, 5], ['*', 6, 8]]
[[3, 1, 2], [4, 7, 5], [6, '*', 8]]
[[3, 1, 2], [4, '*', 5], [6, 7, 8]]
[[3, 1, 2], ['*', 4, 5], [6, 7, 8]]
[['*', 1, 2], [3, 4, 5], [6, 7, 8]]

Path cost: 6


Part 6 
For this part, you’ll be implementing A* search.

Part 6.1
Similar to breadth-first and iterative deepening, your A* search should take as input an initial board and a goal board. It should additionally take a heuristic function


Action sequence:
['LEFT', 1, 0]
['DOWN', 2, 0]
['RIGHT', 2, 1]
['UP', 1, 1]
['LEFT', 1, 0]
['UP', 0, 0]

State sequence:
[[3, 1, 2], ['*', 7, 5], [4, 6, 8]]
[[3, 1, 2], [4, 7, 5], ['*', 6, 8]]
[[3, 1, 2], [4, 7, 5], [6, '*', 8]]
[[3, 1, 2], [4, '*', 5], [6, 7, 8]]
[[3, 1, 2], ['*', 4, 5], [6, 7, 8]]
[['*', 1, 2], [3, 4, 5], [6, 7, 8]]

Path cost: 6


Part 6.2
Now you’ll implement the two classic n puzzle heuristic functions - number of misplaced tiles and Manhattan distance. Test your code with both of these on *puzzle-0* and *puzzle-1*. You’ll probably notice that you have to wait some time (but hopefully not as long as with (constantly 0)!) to get back an answer when using the misplaced tiles heuristic. This illustrates very clearly just how much choosing a good heuristic matters for the practicality of A* search.


Heuristic function: Misplaced tiles 
Puzzle: 0 

Action sequence:
['LEFT', 1, 0]
['DOWN', 2, 0]
['RIGHT', 2, 1]
['UP', 1, 1]
['LEFT', 1, 0]
['UP', 0, 0]

State sequence:
[[3, 1, 2], ['*', 7, 5], [4, 6, 8]]
[[3, 1, 2], [4, 7, 5], ['*', 6, 8]]
[[3, 1, 2], [4, 7, 5], [6, '*', 8]]
[[3, 1, 2], [4, '*', 5], [6, 7, 8]]
[[3, 1, 2], ['*', 4, 5], [6, 7, 8]]
[['*', 1, 2], [3, 4, 5], [6, 7, 8]]

Path cost: 6

--------------------------------------------------------------------------------------------------------

Heuristic function : Manhattan 
Puzzle: 0 

Action sequence:
['LEFT', 1, 0]
['DOWN', 2, 0]
['RIGHT', 2, 1]
['UP', 1, 1]
['LEFT', 1, 0]
['UP', 0, 0]

State sequence:
[[3, 1, 2], ['*', 7, 5], [4, 6, 8]]
[[3, 1, 2], [4, 7, 5], ['*', 6, 8]]
[[3, 1, 2], [4, 7, 5], [6, '*', 8]]
[[3, 1, 2], [4, '*', 5], [6, 7, 8]]
[[3, 1, 2], ['*', 4, 5], [6, 7, 8]]
[['*', 1, 2], [3, 4, 5], [6, 7, 8]]

Path cost: 6

--------------------------------------------------------------------------------------------------------

Heuristic function : Misplaced tiles  
Puzzle: 1 

Action sequence:
['RIGHT', 1, 2]
['UP', 0, 2]
['LEFT', 0, 1]
['LEFT', 0, 0]
['DOWN', 1, 0]
['RIGHT', 1, 1]
['RIGHT', 1, 2]
['DOWN', 2, 2]
['LEFT', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['RIGHT', 1, 1]
['RIGHT', 1, 2]
['DOWN', 2, 2]
['LEFT', 2, 1]
['UP', 1, 1]
['RIGHT', 1, 2]
['UP', 0, 2]
['LEFT', 0, 1]
['LEFT', 0, 0]
['DOWN', 1, 0]
['RIGHT', 1, 1]
['UP', 0, 1]
['RIGHT', 0, 2]
['DOWN', 1, 2]
['LEFT', 1, 1]
['UP', 0, 1]
['LEFT', 0, 0]
['DOWN', 1, 0]
['RIGHT', 1, 1]
['DOWN', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['UP', 0, 0]
['RIGHT', 0, 1]
['DOWN', 1, 1]
['DOWN', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['UP', 0, 0]
['RIGHT', 0, 1]
['DOWN', 1, 1]
['LEFT', 1, 0]
['DOWN', 2, 0]
['RIGHT', 2, 1]
['UP', 1, 1]
['UP', 0, 1]
['LEFT', 0, 0]
['DOWN', 1, 0]
['RIGHT', 1, 1]
['DOWN', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['UP', 0, 0]

State sequence:
[[7, 2, 4], [5, 6, '*'], [8, 3, 1]]
[[7, 2, '*'], [5, 6, 4], [8, 3, 1]]
[[7, '*', 2], [5, 6, 4], [8, 3, 1]]
[['*', 7, 2], [5, 6, 4], [8, 3, 1]]
[[5, 7, 2], ['*', 6, 4], [8, 3, 1]]
[[5, 7, 2], [6, '*', 4], [8, 3, 1]]
[[5, 7, 2], [6, 4, '*'], [8, 3, 1]]
[[5, 7, 2], [6, 4, 1], [8, 3, '*']]
[[5, 7, 2], [6, 4, 1], [8, '*', 3]]
[[5, 7, 2], [6, 4, 1], ['*', 8, 3]]
[[5, 7, 2], ['*', 4, 1], [6, 8, 3]]
[[5, 7, 2], [4, '*', 1], [6, 8, 3]]
[[5, 7, 2], [4, 1, '*'], [6, 8, 3]]
[[5, 7, 2], [4, 1, 3], [6, 8, '*']]
[[5, 7, 2], [4, 1, 3], [6, '*', 8]]
[[5, 7, 2], [4, '*', 3], [6, 1, 8]]
[[5, 7, 2], [4, 3, '*'], [6, 1, 8]]
[[5, 7, '*'], [4, 3, 2], [6, 1, 8]]
[[5, '*', 7], [4, 3, 2], [6, 1, 8]]
[['*', 5, 7], [4, 3, 2], [6, 1, 8]]
[[4, 5, 7], ['*', 3, 2], [6, 1, 8]]
[[4, 5, 7], [3, '*', 2], [6, 1, 8]]
[[4, '*', 7], [3, 5, 2], [6, 1, 8]]
[[4, 7, '*'], [3, 5, 2], [6, 1, 8]]
[[4, 7, 2], [3, 5, '*'], [6, 1, 8]]
[[4, 7, 2], [3, '*', 5], [6, 1, 8]]
[[4, '*', 2], [3, 7, 5], [6, 1, 8]]
[['*', 4, 2], [3, 7, 5], [6, 1, 8]]
[[3, 4, 2], ['*', 7, 5], [6, 1, 8]]
[[3, 4, 2], [7, '*', 5], [6, 1, 8]]
[[3, 4, 2], [7, 1, 5], [6, '*', 8]]
[[3, 4, 2], [7, 1, 5], ['*', 6, 8]]
[[3, 4, 2], ['*', 1, 5], [7, 6, 8]]
[['*', 4, 2], [3, 1, 5], [7, 6, 8]]
[[4, '*', 2], [3, 1, 5], [7, 6, 8]]
[[4, 1, 2], [3, '*', 5], [7, 6, 8]]
[[4, 1, 2], [3, 6, 5], [7, '*', 8]]
[[4, 1, 2], [3, 6, 5], ['*', 7, 8]]
[[4, 1, 2], ['*', 6, 5], [3, 7, 8]]
[['*', 1, 2], [4, 6, 5], [3, 7, 8]]
[[1, '*', 2], [4, 6, 5], [3, 7, 8]]
[[1, 6, 2], [4, '*', 5], [3, 7, 8]]
[[1, 6, 2], ['*', 4, 5], [3, 7, 8]]
[[1, 6, 2], [3, 4, 5], ['*', 7, 8]]
[[1, 6, 2], [3, 4, 5], [7, '*', 8]]
[[1, 6, 2], [3, '*', 5], [7, 4, 8]]
[[1, '*', 2], [3, 6, 5], [7, 4, 8]]
[['*', 1, 2], [3, 6, 5], [7, 4, 8]]
[[3, 1, 2], ['*', 6, 5], [7, 4, 8]]
[[3, 1, 2], [6, '*', 5], [7, 4, 8]]
[[3, 1, 2], [6, 4, 5], [7, '*', 8]]
[[3, 1, 2], [6, 4, 5], ['*', 7, 8]]
[[3, 1, 2], ['*', 4, 5], [6, 7, 8]]
[['*', 1, 2], [3, 4, 5], [6, 7, 8]]

Path cost: 54

--------------------------------------------------------------------------------------------------------

Heuristic function : Manhattan 
Puzzle: 1

Action sequence:
['RIGHT', 1, 2]
['UP', 0, 2]
['LEFT', 0, 1]
['LEFT', 0, 0]
['DOWN', 1, 0]
['RIGHT', 1, 1]
['DOWN', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['RIGHT', 1, 1]
['RIGHT', 1, 2]
['DOWN', 2, 2]
['LEFT', 2, 1]
['UP', 1, 1]
['UP', 0, 1]
['LEFT', 0, 0]
['DOWN', 1, 0]
['RIGHT', 1, 1]
['RIGHT', 1, 2]
['UP', 0, 2]
['LEFT', 0, 1]
['DOWN', 1, 1]
['LEFT', 1, 0]
['UP', 0, 0]
['RIGHT', 0, 1]
['RIGHT', 0, 2]
['DOWN', 1, 2]
['DOWN', 2, 2]
['LEFT', 2, 1]
['UP', 1, 1]
['UP', 0, 1]
['LEFT', 0, 0]
['DOWN', 1, 0]
['DOWN', 2, 0]
['RIGHT', 2, 1]
['RIGHT', 2, 2]
['UP', 1, 2]
['LEFT', 1, 1]
['DOWN', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['UP', 0, 0]

State sequence:
[[7, 2, 4], [5, 6, '*'], [8, 3, 1]]
[[7, 2, '*'], [5, 6, 4], [8, 3, 1]]
[[7, '*', 2], [5, 6, 4], [8, 3, 1]]
[['*', 7, 2], [5, 6, 4], [8, 3, 1]]
[[5, 7, 2], ['*', 6, 4], [8, 3, 1]]
[[5, 7, 2], [6, '*', 4], [8, 3, 1]]
[[5, 7, 2], [6, 3, 4], [8, '*', 1]]
[[5, 7, 2], [6, 3, 4], ['*', 8, 1]]
[[5, 7, 2], ['*', 3, 4], [6, 8, 1]]
[[5, 7, 2], [3, '*', 4], [6, 8, 1]]
[[5, 7, 2], [3, 4, '*'], [6, 8, 1]]
[[5, 7, 2], [3, 4, 1], [6, 8, '*']]
[[5, 7, 2], [3, 4, 1], [6, '*', 8]]
[[5, 7, 2], [3, '*', 1], [6, 4, 8]]
[[5, '*', 2], [3, 7, 1], [6, 4, 8]]
[['*', 5, 2], [3, 7, 1], [6, 4, 8]]
[[3, 5, 2], ['*', 7, 1], [6, 4, 8]]
[[3, 5, 2], [7, '*', 1], [6, 4, 8]]
[[3, 5, 2], [7, 1, '*'], [6, 4, 8]]
[[3, 5, '*'], [7, 1, 2], [6, 4, 8]]
[[3, '*', 5], [7, 1, 2], [6, 4, 8]]
[[3, 1, 5], [7, '*', 2], [6, 4, 8]]
[[3, 1, 5], ['*', 7, 2], [6, 4, 8]]
[['*', 1, 5], [3, 7, 2], [6, 4, 8]]
[[1, '*', 5], [3, 7, 2], [6, 4, 8]]
[[1, 5, '*'], [3, 7, 2], [6, 4, 8]]
[[1, 5, 2], [3, 7, '*'], [6, 4, 8]]
[[1, 5, 2], [3, 7, 8], [6, 4, '*']]
[[1, 5, 2], [3, 7, 8], [6, '*', 4]]
[[1, 5, 2], [3, '*', 8], [6, 7, 4]]
[[1, '*', 2], [3, 5, 8], [6, 7, 4]]
[['*', 1, 2], [3, 5, 8], [6, 7, 4]]
[[3, 1, 2], ['*', 5, 8], [6, 7, 4]]
[[3, 1, 2], [6, 5, 8], ['*', 7, 4]]
[[3, 1, 2], [6, 5, 8], [7, '*', 4]]
[[3, 1, 2], [6, 5, 8], [7, 4, '*']]
[[3, 1, 2], [6, 5, '*'], [7, 4, 8]]
[[3, 1, 2], [6, '*', 5], [7, 4, 8]]
[[3, 1, 2], [6, 4, 5], [7, '*', 8]]
[[3, 1, 2], [6, 4, 5], ['*', 7, 8]]
[[3, 1, 2], ['*', 4, 5], [6, 7, 8]]
[['*', 1, 2], [3, 4, 5], [6, 7, 8]]

Path cost: 42

--------------------------------------------------------------------------------------------------------


Part 7 [481: 25 pts; 681: 23 pts]
In this final part, you’ll be benchmarking your searches to get an empirical sense of the differ- ences in time/space complexity between them. For this you’ll need a profiler. NB that  some profilers also include memory usage statistics, which may give a good idea about the maximum amount of memory used at any point on a given run. If the profiler for your language does not include this, you’ll have to instrument your code to keep track of the maximum number of nodes on the frontier at any one time over the entire run.   In Figures 5 and 6 I list what I get when profiling runs of my reference implementations of breadth-first and A* search. This output was generated using SBCL’s profiler. SBCL is the Common Lisp implementation that I use. Like most of Common Lisp tooling, the profiler is easily accessible using SLIME in Emacs
What we’re interested in here is ”consed” (which is a good proxy for the total amount of memory used) and the number of calls we made to expand. The former gives us an idea of the space complexity, and the latter the time complexity. Note that A* performs orders of magnitude better than breadth-first on both counts! You can also see that A* is better in terms of actual time - taking less than half a second to complete where breadth-first takes over four seconds.

Part 7.1
Profile each of iterative deepening search, breadth-first search, and A* search using Manhattan distance solving *puzzle-0*. Even on this simple puzzle solvable in only 6 moves, you should be able to get a sense of the difference in performance characteristics between these three algo- rithms.

A) Iterative deeping search - 

Profiler report : idfs_report_1.pdf

Max queue size: 401

Action sequence:
['LEFT', 1, 0]
['DOWN', 2, 0]
['RIGHT', 2, 1]
['UP', 1, 1]
['LEFT', 1, 0]
['UP', 0, 0]

State sequence:
[[3, 1, 2], ['*', 7, 5], [4, 6, 8]]
[[3, 1, 2], [4, 7, 5], ['*', 6, 8]]
[[3, 1, 2], [4, 7, 5], [6, '*', 8]]
[[3, 1, 2], [4, '*', 5], [6, 7, 8]]
[[3, 1, 2], ['*', 4, 5], [6, 7, 8]]
[['*', 1, 2], [3, 4, 5], [6, 7, 8]]

Path cost: 6


B) BFS Search:

Profiler report : bfs_report_1.pdf

Max queue size: 97

Action sequence:
['LEFT', 1, 0]
['DOWN', 2, 0]
['RIGHT', 2, 1]
['UP', 1, 1]
['LEFT', 1, 0]
['UP', 0, 0]

State sequence:
[[3, 1, 2], ['*', 7, 5], [4, 6, 8]]
[[3, 1, 2], [4, 7, 5], ['*', 6, 8]]
[[3, 1, 2], [4, 7, 5], [6, '*', 8]]
[[3, 1, 2], [4, '*', 5], [6, 7, 8]]
[[3, 1, 2], ['*', 4, 5], [6, 7, 8]]
[['*', 1, 2], [3, 4, 5], [6, 7, 8]]

Path cost: 6



c) A* search with manhattan distance heuristic : 

Profiler report : a_star_report_1.pdf

Max queue size: 16

Action sequence:
['LEFT', 1, 0]
['DOWN', 2, 0]
['RIGHT', 2, 1]
['UP', 1, 1]
['LEFT', 1, 0]
['UP', 0, 0]

State sequence:
[[3, 1, 2], ['*', 7, 5], [4, 6, 8]]
[[3, 1, 2], [4, 7, 5], ['*', 6, 8]]
[[3, 1, 2], [4, 7, 5], [6, '*', 8]]
[[3, 1, 2], [4, '*', 5], [6, 7, 8]]
[[3, 1, 2], ['*', 4, 5], [6, 7, 8]]
[['*', 1, 2], [3, 4, 5], [6, 7, 8]]

Path cost: 6


Part 7.2
Just to drive the point home about choosing a good heuristic, profile A* on *puzzle-2* once using the number of misplaced tiles, and then once using the Manhattan distance.

Profiler report : a_star_report_7.2_1.pdf

Puzzle 2: Manhattan distance

Max queue size: 172

Action sequence:
['LEFT', 2, 0]
['UP', 1, 0]
['UP', 0, 0]
['RIGHT', 0, 1]
['RIGHT', 0, 2]
['DOWN', 1, 2]
['LEFT', 1, 1]
['DOWN', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['UP', 0, 0]
['RIGHT', 0, 1]
['DOWN', 1, 1]
['DOWN', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['UP', 0, 0]
['RIGHT', 0, 1]
['DOWN', 1, 1]
['DOWN', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['UP', 0, 0]
['RIGHT', 0, 1]
['DOWN', 1, 1]
['LEFT', 1, 0]
['DOWN', 2, 0]
['RIGHT', 2, 1]
['UP', 1, 1]
['UP', 0, 1]
['LEFT', 0, 0]
['DOWN', 1, 0]
['RIGHT', 1, 1]
['DOWN', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['UP', 0, 0]

State sequence:
[[6, 7, 3], [1, 5, 2], ['*', 4, 8]]
[[6, 7, 3], ['*', 5, 2], [1, 4, 8]]
[['*', 7, 3], [6, 5, 2], [1, 4, 8]]
[[7, '*', 3], [6, 5, 2], [1, 4, 8]]
[[7, 3, '*'], [6, 5, 2], [1, 4, 8]]
[[7, 3, 2], [6, 5, '*'], [1, 4, 8]]
[[7, 3, 2], [6, '*', 5], [1, 4, 8]]
[[7, 3, 2], [6, 4, 5], [1, '*', 8]]
[[7, 3, 2], [6, 4, 5], ['*', 1, 8]]
[[7, 3, 2], ['*', 4, 5], [6, 1, 8]]
[['*', 3, 2], [7, 4, 5], [6, 1, 8]]
[[3, '*', 2], [7, 4, 5], [6, 1, 8]]
[[3, 4, 2], [7, '*', 5], [6, 1, 8]]
[[3, 4, 2], [7, 1, 5], [6, '*', 8]]
[[3, 4, 2], [7, 1, 5], ['*', 6, 8]]
[[3, 4, 2], ['*', 1, 5], [7, 6, 8]]
[['*', 4, 2], [3, 1, 5], [7, 6, 8]]
[[4, '*', 2], [3, 1, 5], [7, 6, 8]]
[[4, 1, 2], [3, '*', 5], [7, 6, 8]]
[[4, 1, 2], [3, 6, 5], [7, '*', 8]]
[[4, 1, 2], [3, 6, 5], ['*', 7, 8]]
[[4, 1, 2], ['*', 6, 5], [3, 7, 8]]
[['*', 1, 2], [4, 6, 5], [3, 7, 8]]
[[1, '*', 2], [4, 6, 5], [3, 7, 8]]
[[1, 6, 2], [4, '*', 5], [3, 7, 8]]
[[1, 6, 2], ['*', 4, 5], [3, 7, 8]]
[[1, 6, 2], [3, 4, 5], ['*', 7, 8]]
[[1, 6, 2], [3, 4, 5], [7, '*', 8]]
[[1, 6, 2], [3, '*', 5], [7, 4, 8]]
[[1, '*', 2], [3, 6, 5], [7, 4, 8]]
[['*', 1, 2], [3, 6, 5], [7, 4, 8]]
[[3, 1, 2], ['*', 6, 5], [7, 4, 8]]
[[3, 1, 2], [6, '*', 5], [7, 4, 8]]
[[3, 1, 2], [6, 4, 5], [7, '*', 8]]
[[3, 1, 2], [6, 4, 5], ['*', 7, 8]]
[[3, 1, 2], ['*', 4, 5], [6, 7, 8]]
[['*', 1, 2], [3, 4, 5], [6, 7, 8]]

Path cost: 37


Profiler report: 

Puzzle 2: Misplaced Tiles

Max queue size: 413

Action sequence:
['LEFT', 2, 0]
['UP', 1, 0]
['RIGHT', 1, 1]
['DOWN', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['UP', 0, 0]
['RIGHT', 0, 1]
['RIGHT', 0, 2]
['DOWN', 1, 2]
['LEFT', 1, 1]
['DOWN', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['UP', 0, 0]
['RIGHT', 0, 1]
['DOWN', 1, 1]
['LEFT', 1, 0]
['DOWN', 2, 0]
['RIGHT', 2, 1]
['UP', 1, 1]
['RIGHT', 1, 2]
['DOWN', 2, 2]
['LEFT', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['RIGHT', 1, 1]
['DOWN', 2, 1]
['RIGHT', 2, 2]
['UP', 1, 2]
['LEFT', 1, 1]
['LEFT', 1, 0]
['UP', 0, 0]

State sequence:
[[6, 7, 3], [1, 5, 2], ['*', 4, 8]]
[[6, 7, 3], ['*', 5, 2], [1, 4, 8]]
[[6, 7, 3], [5, '*', 2], [1, 4, 8]]
[[6, 7, 3], [5, 4, 2], [1, '*', 8]]
[[6, 7, 3], [5, 4, 2], ['*', 1, 8]]
[[6, 7, 3], ['*', 4, 2], [5, 1, 8]]
[['*', 7, 3], [6, 4, 2], [5, 1, 8]]
[[7, '*', 3], [6, 4, 2], [5, 1, 8]]
[[7, 3, '*'], [6, 4, 2], [5, 1, 8]]
[[7, 3, 2], [6, 4, '*'], [5, 1, 8]]
[[7, 3, 2], [6, '*', 4], [5, 1, 8]]
[[7, 3, 2], [6, 1, 4], [5, '*', 8]]
[[7, 3, 2], [6, 1, 4], ['*', 5, 8]]
[[7, 3, 2], ['*', 1, 4], [6, 5, 8]]
[['*', 3, 2], [7, 1, 4], [6, 5, 8]]
[[3, '*', 2], [7, 1, 4], [6, 5, 8]]
[[3, 1, 2], [7, '*', 4], [6, 5, 8]]
[[3, 1, 2], ['*', 7, 4], [6, 5, 8]]
[[3, 1, 2], [6, 7, 4], ['*', 5, 8]]
[[3, 1, 2], [6, 7, 4], [5, '*', 8]]
[[3, 1, 2], [6, '*', 4], [5, 7, 8]]
[[3, 1, 2], [6, 4, '*'], [5, 7, 8]]
[[3, 1, 2], [6, 4, 8], [5, 7, '*']]
[[3, 1, 2], [6, 4, 8], [5, '*', 7]]
[[3, 1, 2], [6, 4, 8], ['*', 5, 7]]
[[3, 1, 2], ['*', 4, 8], [6, 5, 7]]
[[3, 1, 2], [4, '*', 8], [6, 5, 7]]
[[3, 1, 2], [4, 5, 8], [6, '*', 7]]
[[3, 1, 2], [4, 5, 8], [6, 7, '*']]
[[3, 1, 2], [4, 5, '*'], [6, 7, 8]]
[[3, 1, 2], [4, '*', 5], [6, 7, 8]]
[[3, 1, 2], ['*', 4, 5], [6, 7, 8]]
[['*', 1, 2], [3, 4, 5], [6, 7, 8]]

Path cost: 33


Part 7.3
Generate profiler reports for both of A* using Manhattan distance and breadth-first search on
*puzzle-2*, *puzzle-3*, *puzzle-4*, *puzzle-5*, and *puzzle-6*.7 Then calculate aver- ages over each of the five runs for the amount of memory used and number of calls to expand for both A* and breadth-first search.


Profiler report : a_star_report_7.3_1.pdf

Puzzle 2: Manhattan distance

Max queue size: 172

Action sequence:
['LEFT', 2, 0]
['UP', 1, 0]
['UP', 0, 0]
['RIGHT', 0, 1]
['RIGHT', 0, 2]
['DOWN', 1, 2]
['LEFT', 1, 1]
['DOWN', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['UP', 0, 0]
['RIGHT', 0, 1]
['DOWN', 1, 1]
['DOWN', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['UP', 0, 0]
['RIGHT', 0, 1]
['DOWN', 1, 1]
['DOWN', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['UP', 0, 0]
['RIGHT', 0, 1]
['DOWN', 1, 1]
['LEFT', 1, 0]
['DOWN', 2, 0]
['RIGHT', 2, 1]
['UP', 1, 1]
['UP', 0, 1]
['LEFT', 0, 0]
['DOWN', 1, 0]
['RIGHT', 1, 1]
['DOWN', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['UP', 0, 0]

State sequence:
[[6, 7, 3], [1, 5, 2], ['*', 4, 8]]
[[6, 7, 3], ['*', 5, 2], [1, 4, 8]]
[['*', 7, 3], [6, 5, 2], [1, 4, 8]]
[[7, '*', 3], [6, 5, 2], [1, 4, 8]]
[[7, 3, '*'], [6, 5, 2], [1, 4, 8]]
[[7, 3, 2], [6, 5, '*'], [1, 4, 8]]
[[7, 3, 2], [6, '*', 5], [1, 4, 8]]
[[7, 3, 2], [6, 4, 5], [1, '*', 8]]
[[7, 3, 2], [6, 4, 5], ['*', 1, 8]]
[[7, 3, 2], ['*', 4, 5], [6, 1, 8]]
[['*', 3, 2], [7, 4, 5], [6, 1, 8]]
[[3, '*', 2], [7, 4, 5], [6, 1, 8]]
[[3, 4, 2], [7, '*', 5], [6, 1, 8]]
[[3, 4, 2], [7, 1, 5], [6, '*', 8]]
[[3, 4, 2], [7, 1, 5], ['*', 6, 8]]
[[3, 4, 2], ['*', 1, 5], [7, 6, 8]]
[['*', 4, 2], [3, 1, 5], [7, 6, 8]]
[[4, '*', 2], [3, 1, 5], [7, 6, 8]]
[[4, 1, 2], [3, '*', 5], [7, 6, 8]]
[[4, 1, 2], [3, 6, 5], [7, '*', 8]]
[[4, 1, 2], [3, 6, 5], ['*', 7, 8]]
[[4, 1, 2], ['*', 6, 5], [3, 7, 8]]
[['*', 1, 2], [4, 6, 5], [3, 7, 8]]
[[1, '*', 2], [4, 6, 5], [3, 7, 8]]
[[1, 6, 2], [4, '*', 5], [3, 7, 8]]
[[1, 6, 2], ['*', 4, 5], [3, 7, 8]]
[[1, 6, 2], [3, 4, 5], ['*', 7, 8]]
[[1, 6, 2], [3, 4, 5], [7, '*', 8]]
[[1, 6, 2], [3, '*', 5], [7, 4, 8]]
[[1, '*', 2], [3, 6, 5], [7, 4, 8]]
[['*', 1, 2], [3, 6, 5], [7, 4, 8]]
[[3, 1, 2], ['*', 6, 5], [7, 4, 8]]
[[3, 1, 2], [6, '*', 5], [7, 4, 8]]
[[3, 1, 2], [6, 4, 5], [7, '*', 8]]
[[3, 1, 2], [6, 4, 5], ['*', 7, 8]]
[[3, 1, 2], ['*', 4, 5], [6, 7, 8]]
[['*', 1, 2], [3, 4, 5], [6, 7, 8]]

Path cost: 37

Profiler report : a_star_report_7.3_2.pdf

Puzzle 3: Manhattan distance
Max queue size: 602
Action sequence:
['RIGHT', 0, 1]
['DOWN', 1, 1]
['RIGHT', 1, 2]
['DOWN', 2, 2]
['LEFT', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['UP', 0, 0]
['RIGHT', 0, 1]
['RIGHT', 0, 2]
['DOWN', 1, 2]
['DOWN', 2, 2]
['LEFT', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['RIGHT', 1, 1]
['UP', 0, 1]
['LEFT', 0, 0]
['DOWN', 1, 0]
['RIGHT', 1, 1]
['DOWN', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['UP', 0, 0]
['RIGHT', 0, 1]
['RIGHT', 0, 2]
['DOWN', 1, 2]
['DOWN', 2, 2]
['LEFT', 2, 1]
['UP', 1, 1]
['RIGHT', 1, 2]
['DOWN', 2, 2]
['LEFT', 2, 1]
['UP', 1, 1]
['UP', 0, 1]
['LEFT', 0, 0]
['DOWN', 1, 0]
['DOWN', 2, 0]
['RIGHT', 2, 1]
['RIGHT', 2, 2]
['UP', 1, 2]
['LEFT', 1, 1]
['DOWN', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['UP', 0, 0]

State sequence:
[[8, '*', 6], [4, 1, 3], [7, 2, 5]]
[[8, 1, 6], [4, '*', 3], [7, 2, 5]]
[[8, 1, 6], [4, 3, '*'], [7, 2, 5]]
[[8, 1, 6], [4, 3, 5], [7, 2, '*']]
[[8, 1, 6], [4, 3, 5], [7, '*', 2]]
[[8, 1, 6], [4, 3, 5], ['*', 7, 2]]
[[8, 1, 6], ['*', 3, 5], [4, 7, 2]]
[['*', 1, 6], [8, 3, 5], [4, 7, 2]]
[[1, '*', 6], [8, 3, 5], [4, 7, 2]]
[[1, 6, '*'], [8, 3, 5], [4, 7, 2]]
[[1, 6, 5], [8, 3, '*'], [4, 7, 2]]
[[1, 6, 5], [8, 3, 2], [4, 7, '*']]
[[1, 6, 5], [8, 3, 2], [4, '*', 7]]
[[1, 6, 5], [8, 3, 2], ['*', 4, 7]]
[[1, 6, 5], ['*', 3, 2], [8, 4, 7]]
[[1, 6, 5], [3, '*', 2], [8, 4, 7]]
[[1, '*', 5], [3, 6, 2], [8, 4, 7]]
[['*', 1, 5], [3, 6, 2], [8, 4, 7]]
[[3, 1, 5], ['*', 6, 2], [8, 4, 7]]
[[3, 1, 5], [6, '*', 2], [8, 4, 7]]
[[3, 1, 5], [6, 4, 2], [8, '*', 7]]
[[3, 1, 5], [6, 4, 2], ['*', 8, 7]]
[[3, 1, 5], ['*', 4, 2], [6, 8, 7]]
[['*', 1, 5], [3, 4, 2], [6, 8, 7]]
[[1, '*', 5], [3, 4, 2], [6, 8, 7]]
[[1, 5, '*'], [3, 4, 2], [6, 8, 7]]
[[1, 5, 2], [3, 4, '*'], [6, 8, 7]]
[[1, 5, 2], [3, 4, 7], [6, 8, '*']]
[[1, 5, 2], [3, 4, 7], [6, '*', 8]]
[[1, 5, 2], [3, '*', 7], [6, 4, 8]]
[[1, 5, 2], [3, 7, '*'], [6, 4, 8]]
[[1, 5, 2], [3, 7, 8], [6, 4, '*']]
[[1, 5, 2], [3, 7, 8], [6, '*', 4]]
[[1, 5, 2], [3, '*', 8], [6, 7, 4]]
[[1, '*', 2], [3, 5, 8], [6, 7, 4]]
[['*', 1, 2], [3, 5, 8], [6, 7, 4]]
[[3, 1, 2], ['*', 5, 8], [6, 7, 4]]
[[3, 1, 2], [6, 5, 8], ['*', 7, 4]]
[[3, 1, 2], [6, 5, 8], [7, '*', 4]]
[[3, 1, 2], [6, 5, 8], [7, 4, '*']]
[[3, 1, 2], [6, 5, '*'], [7, 4, 8]]
[[3, 1, 2], [6, '*', 5], [7, 4, 8]]
[[3, 1, 2], [6, 4, 5], [7, '*', 8]]
[[3, 1, 2], [6, 4, 5], ['*', 7, 8]]
[[3, 1, 2], ['*', 4, 5], [6, 7, 8]]
[['*', 1, 2], [3, 4, 5], [6, 7, 8]]

Path cost: 46


Profiler report : a_star_report_7.3_3.pdf

Puzzle 4: Manhattan distance
Max queue size: 626
Action sequence:
['LEFT', 2, 1]
['UP', 1, 1]
['LEFT', 1, 0]
['UP', 0, 0]
['RIGHT', 0, 1]
['RIGHT', 0, 2]
['DOWN', 1, 2]
['LEFT', 1, 1]
['UP', 0, 1]
['RIGHT', 0, 2]
['DOWN', 1, 2]
['LEFT', 1, 1]
['LEFT', 1, 0]
['DOWN', 2, 0]
['RIGHT', 2, 1]
['UP', 1, 1]
['RIGHT', 1, 2]
['DOWN', 2, 2]
['LEFT', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['RIGHT', 1, 1]
['DOWN', 2, 1]
['RIGHT', 2, 2]
['UP', 1, 2]
['LEFT', 1, 1]
['LEFT', 1, 0]
['UP', 0, 0]

State sequence:
[[7, 3, 4], [2, 5, 1], [6, '*', 8]]
[[7, 3, 4], [2, '*', 1], [6, 5, 8]]
[[7, 3, 4], ['*', 2, 1], [6, 5, 8]]
[['*', 3, 4], [7, 2, 1], [6, 5, 8]]
[[3, '*', 4], [7, 2, 1], [6, 5, 8]]
[[3, 4, '*'], [7, 2, 1], [6, 5, 8]]
[[3, 4, 1], [7, 2, '*'], [6, 5, 8]]
[[3, 4, 1], [7, '*', 2], [6, 5, 8]]
[[3, '*', 1], [7, 4, 2], [6, 5, 8]]
[[3, 1, '*'], [7, 4, 2], [6, 5, 8]]
[[3, 1, 2], [7, 4, '*'], [6, 5, 8]]
[[3, 1, 2], [7, '*', 4], [6, 5, 8]]
[[3, 1, 2], ['*', 7, 4], [6, 5, 8]]
[[3, 1, 2], [6, 7, 4], ['*', 5, 8]]
[[3, 1, 2], [6, 7, 4], [5, '*', 8]]
[[3, 1, 2], [6, '*', 4], [5, 7, 8]]
[[3, 1, 2], [6, 4, '*'], [5, 7, 8]]
[[3, 1, 2], [6, 4, 8], [5, 7, '*']]
[[3, 1, 2], [6, 4, 8], [5, '*', 7]]
[[3, 1, 2], [6, 4, 8], ['*', 5, 7]]
[[3, 1, 2], ['*', 4, 8], [6, 5, 7]]
[[3, 1, 2], [4, '*', 8], [6, 5, 7]]
[[3, 1, 2], [4, 5, 8], [6, '*', 7]]
[[3, 1, 2], [4, 5, 8], [6, 7, '*']]
[[3, 1, 2], [4, 5, '*'], [6, 7, 8]]
[[3, 1, 2], [4, '*', 5], [6, 7, 8]]
[[3, 1, 2], ['*', 4, 5], [6, 7, 8]]
[['*', 1, 2], [3, 4, 5], [6, 7, 8]]

Path cost: 28

Profiler report : a_star_report_7.3_4.pdf

Puzzle 5: Manhattan distance
Max queue size: 634
Action sequence:
['UP', 1, 1]
['UP', 0, 1]
['LEFT', 0, 0]
['DOWN', 1, 0]
['RIGHT', 1, 1]
['RIGHT', 1, 2]
['UP', 0, 2]
['LEFT', 0, 1]
['LEFT', 0, 0]
['DOWN', 1, 0]
['RIGHT', 1, 1]
['UP', 0, 1]
['RIGHT', 0, 2]
['DOWN', 1, 2]
['LEFT', 1, 1]
['LEFT', 1, 0]
['UP', 0, 0]
['RIGHT', 0, 1]
['DOWN', 1, 1]
['RIGHT', 1, 2]
['UP', 0, 2]
['LEFT', 0, 1]
['DOWN', 1, 1]
['RIGHT', 1, 2]
['DOWN', 2, 2]
['LEFT', 2, 1]
['UP', 1, 1]
['UP', 0, 1]
['RIGHT', 0, 2]
['DOWN', 1, 2]
['DOWN', 2, 2]
['LEFT', 2, 1]
['UP', 1, 1]
['RIGHT', 1, 2]
['DOWN', 2, 2]
['LEFT', 2, 1]
['UP', 1, 1]
['UP', 0, 1]
['LEFT', 0, 0]
['DOWN', 1, 0]
['DOWN', 2, 0]
['RIGHT', 2, 1]
['RIGHT', 2, 2]
['UP', 1, 2]
['LEFT', 1, 1]
['DOWN', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['UP', 0, 0]

State sequence:
[[1, 3, 8], [4, '*', 5], [6, 7, 2]]
[[1, '*', 8], [4, 3, 5], [6, 7, 2]]
[['*', 1, 8], [4, 3, 5], [6, 7, 2]]
[[4, 1, 8], ['*', 3, 5], [6, 7, 2]]
[[4, 1, 8], [3, '*', 5], [6, 7, 2]]
[[4, 1, 8], [3, 5, '*'], [6, 7, 2]]
[[4, 1, '*'], [3, 5, 8], [6, 7, 2]]
[[4, '*', 1], [3, 5, 8], [6, 7, 2]]
[['*', 4, 1], [3, 5, 8], [6, 7, 2]]
[[3, 4, 1], ['*', 5, 8], [6, 7, 2]]
[[3, 4, 1], [5, '*', 8], [6, 7, 2]]
[[3, '*', 1], [5, 4, 8], [6, 7, 2]]
[[3, 1, '*'], [5, 4, 8], [6, 7, 2]]
[[3, 1, 8], [5, 4, '*'], [6, 7, 2]]
[[3, 1, 8], [5, '*', 4], [6, 7, 2]]
[[3, 1, 8], ['*', 5, 4], [6, 7, 2]]
[['*', 1, 8], [3, 5, 4], [6, 7, 2]]
[[1, '*', 8], [3, 5, 4], [6, 7, 2]]
[[1, 5, 8], [3, '*', 4], [6, 7, 2]]
[[1, 5, 8], [3, 4, '*'], [6, 7, 2]]
[[1, 5, '*'], [3, 4, 8], [6, 7, 2]]
[[1, '*', 5], [3, 4, 8], [6, 7, 2]]
[[1, 4, 5], [3, '*', 8], [6, 7, 2]]
[[1, 4, 5], [3, 8, '*'], [6, 7, 2]]
[[1, 4, 5], [3, 8, 2], [6, 7, '*']]
[[1, 4, 5], [3, 8, 2], [6, '*', 7]]
[[1, 4, 5], [3, '*', 2], [6, 8, 7]]
[[1, '*', 5], [3, 4, 2], [6, 8, 7]]
[[1, 5, '*'], [3, 4, 2], [6, 8, 7]]
[[1, 5, 2], [3, 4, '*'], [6, 8, 7]]
[[1, 5, 2], [3, 4, 7], [6, 8, '*']]
[[1, 5, 2], [3, 4, 7], [6, '*', 8]]
[[1, 5, 2], [3, '*', 7], [6, 4, 8]]
[[1, 5, 2], [3, 7, '*'], [6, 4, 8]]
[[1, 5, 2], [3, 7, 8], [6, 4, '*']]
[[1, 5, 2], [3, 7, 8], [6, '*', 4]]
[[1, 5, 2], [3, '*', 8], [6, 7, 4]]
[[1, '*', 2], [3, 5, 8], [6, 7, 4]]
[['*', 1, 2], [3, 5, 8], [6, 7, 4]]
[[3, 1, 2], ['*', 5, 8], [6, 7, 4]]
[[3, 1, 2], [6, 5, 8], ['*', 7, 4]]
[[3, 1, 2], [6, 5, 8], [7, '*', 4]]
[[3, 1, 2], [6, 5, 8], [7, 4, '*']]
[[3, 1, 2], [6, 5, '*'], [7, 4, 8]]
[[3, 1, 2], [6, '*', 5], [7, 4, 8]]
[[3, 1, 2], [6, 4, 5], [7, '*', 8]]
[[3, 1, 2], [6, 4, 5], ['*', 7, 8]]
[[3, 1, 2], ['*', 4, 5], [6, 7, 8]]
[['*', 1, 2], [3, 4, 5], [6, 7, 8]]

Path cost: 49


Profiler report : a_star_report_7.3_5.pdf

Puzzle 6: Manhattan distance
Max queue size: 53
Action sequence:
['LEFT', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['UP', 0, 0]
['RIGHT', 0, 1]
['RIGHT', 0, 2]
['DOWN', 1, 2]
['DOWN', 2, 2]
['LEFT', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['UP', 0, 0]
['RIGHT', 0, 1]
['RIGHT', 0, 2]
['DOWN', 1, 2]
['DOWN', 2, 2]
['LEFT', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['UP', 0, 0]
['RIGHT', 0, 1]
['RIGHT', 0, 2]
['DOWN', 1, 2]
['DOWN', 2, 2]
['LEFT', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['UP', 0, 0]

State sequence:
[[8, 7, 6], [5, 4, 3], [2, '*', 1]]
[[8, 7, 6], [5, 4, 3], ['*', 2, 1]]
[[8, 7, 6], ['*', 4, 3], [5, 2, 1]]
[['*', 7, 6], [8, 4, 3], [5, 2, 1]]
[[7, '*', 6], [8, 4, 3], [5, 2, 1]]
[[7, 6, '*'], [8, 4, 3], [5, 2, 1]]
[[7, 6, 3], [8, 4, '*'], [5, 2, 1]]
[[7, 6, 3], [8, 4, 1], [5, 2, '*']]
[[7, 6, 3], [8, 4, 1], [5, '*', 2]]
[[7, 6, 3], [8, 4, 1], ['*', 5, 2]]
[[7, 6, 3], ['*', 4, 1], [8, 5, 2]]
[['*', 6, 3], [7, 4, 1], [8, 5, 2]]
[[6, '*', 3], [7, 4, 1], [8, 5, 2]]
[[6, 3, '*'], [7, 4, 1], [8, 5, 2]]
[[6, 3, 1], [7, 4, '*'], [8, 5, 2]]
[[6, 3, 1], [7, 4, 2], [8, 5, '*']]
[[6, 3, 1], [7, 4, 2], [8, '*', 5]]
[[6, 3, 1], [7, 4, 2], ['*', 8, 5]]
[[6, 3, 1], ['*', 4, 2], [7, 8, 5]]
[['*', 3, 1], [6, 4, 2], [7, 8, 5]]
[[3, '*', 1], [6, 4, 2], [7, 8, 5]]
[[3, 1, '*'], [6, 4, 2], [7, 8, 5]]
[[3, 1, 2], [6, 4, '*'], [7, 8, 5]]
[[3, 1, 2], [6, 4, 5], [7, 8, '*']]
[[3, 1, 2], [6, 4, 5], [7, '*', 8]]
[[3, 1, 2], [6, 4, 5], ['*', 7, 8]]
[[3, 1, 2], ['*', 4, 5], [6, 7, 8]]
[['*', 1, 2], [3, 4, 5], [6, 7, 8]]

Path cost: 28

Profiler report : bfs_7.3_1.pdf
Puzzle : 2
Max queue size: 68949
Action sequence:
['LEFT', 2, 0]
['UP', 1, 0]
['UP', 0, 0]
['RIGHT', 0, 1]
['RIGHT', 0, 2]
['DOWN', 1, 2]
['LEFT', 1, 1]
['LEFT', 1, 0]
['DOWN', 2, 0]
['RIGHT', 2, 1]
['UP', 1, 1]
['LEFT', 1, 0]
['UP', 0, 0]
['RIGHT', 0, 1]
['DOWN', 1, 1]
['LEFT', 1, 0]
['DOWN', 2, 0]
['RIGHT', 2, 1]
['UP', 1, 1]
['LEFT', 1, 0]
['UP', 0, 0]

State sequence:
[[6, 7, 3], [1, 5, 2], ['*', 4, 8]]
[[6, 7, 3], ['*', 5, 2], [1, 4, 8]]
[['*', 7, 3], [6, 5, 2], [1, 4, 8]]
[[7, '*', 3], [6, 5, 2], [1, 4, 8]]
[[7, 3, '*'], [6, 5, 2], [1, 4, 8]]
[[7, 3, 2], [6, 5, '*'], [1, 4, 8]]
[[7, 3, 2], [6, '*', 5], [1, 4, 8]]
[[7, 3, 2], ['*', 6, 5], [1, 4, 8]]
[[7, 3, 2], [1, 6, 5], ['*', 4, 8]]
[[7, 3, 2], [1, 6, 5], [4, '*', 8]]
[[7, 3, 2], [1, '*', 5], [4, 6, 8]]
[[7, 3, 2], ['*', 1, 5], [4, 6, 8]]
[['*', 3, 2], [7, 1, 5], [4, 6, 8]]
[[3, '*', 2], [7, 1, 5], [4, 6, 8]]
[[3, 1, 2], [7, '*', 5], [4, 6, 8]]
[[3, 1, 2], ['*', 7, 5], [4, 6, 8]]
[[3, 1, 2], [4, 7, 5], ['*', 6, 8]]
[[3, 1, 2], [4, 7, 5], [6, '*', 8]]
[[3, 1, 2], [4, '*', 5], [6, 7, 8]]
[[3, 1, 2], ['*', 4, 5], [6, 7, 8]]
[['*', 1, 2], [3, 4, 5], [6, 7, 8]]

Path cost: 21



Profiler report : bfs_7.3_2.pdf

Puzzle : 3
Max queue size: 136151
Action sequence:
['DOWN', 1, 0]
['RIGHT', 1, 1]
['DOWN', 2, 1]
['RIGHT', 2, 2]
['UP', 1, 2]
['LEFT', 1, 1]
['UP', 0, 1]
['RIGHT', 0, 2]
['DOWN', 1, 2]
['LEFT', 1, 1]
['UP', 0, 1]
['LEFT', 0, 0]
['DOWN', 1, 0]
['RIGHT', 1, 1]
['DOWN', 2, 1]
['RIGHT', 2, 2]
['UP', 1, 2]
['LEFT', 1, 1]
['DOWN', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['RIGHT', 1, 1]
['UP', 0, 1]
['LEFT', 0, 0]

State sequence:
[[4, 8, 6], ['*', 1, 3], [7, 2, 5]]
[[4, 8, 6], [1, '*', 3], [7, 2, 5]]
[[4, 8, 6], [1, 2, 3], [7, '*', 5]]
[[4, 8, 6], [1, 2, 3], [7, 5, '*']]
[[4, 8, 6], [1, 2, '*'], [7, 5, 3]]
[[4, 8, 6], [1, '*', 2], [7, 5, 3]]
[[4, '*', 6], [1, 8, 2], [7, 5, 3]]
[[4, 6, '*'], [1, 8, 2], [7, 5, 3]]
[[4, 6, 2], [1, 8, '*'], [7, 5, 3]]
[[4, 6, 2], [1, '*', 8], [7, 5, 3]]
[[4, '*', 2], [1, 6, 8], [7, 5, 3]]
[['*', 4, 2], [1, 6, 8], [7, 5, 3]]
[[1, 4, 2], ['*', 6, 8], [7, 5, 3]]
[[1, 4, 2], [6, '*', 8], [7, 5, 3]]
[[1, 4, 2], [6, 5, 8], [7, '*', 3]]
[[1, 4, 2], [6, 5, 8], [7, 3, '*']]
[[1, 4, 2], [6, 5, '*'], [7, 3, 8]]
[[1, 4, 2], [6, '*', 5], [7, 3, 8]]
[[1, 4, 2], [6, 3, 5], [7, '*', 8]]
[[1, 4, 2], [6, 3, 5], ['*', 7, 8]]
[[1, 4, 2], ['*', 3, 5], [6, 7, 8]]
[[1, 4, 2], [3, '*', 5], [6, 7, 8]]
[[1, '*', 2], [3, 4, 5], [6, 7, 8]]
[['*', 1, 2], [3, 4, 5], [6, 7, 8]]

Path cost: 24


Profiler report : bfs_7.3_3.pdf

Puzzle : 4
Max queue size: 76969
Action sequence:
['LEFT', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['UP', 0, 0]
['RIGHT', 0, 1]
['DOWN', 1, 1]
['RIGHT', 1, 2]
['UP', 0, 2]
['LEFT', 0, 1]
['DOWN', 1, 1]
['LEFT', 1, 0]
['DOWN', 2, 0]
['RIGHT', 2, 1]
['UP', 1, 1]
['LEFT', 1, 0]
['UP', 0, 0]
['RIGHT', 0, 1]
['DOWN', 1, 1]
['RIGHT', 1, 2]
['UP', 0, 2]
['LEFT', 0, 1]
['LEFT', 0, 0]

State sequence:
[[7, 3, 4], [2, 5, 1], [6, '*', 8]]
[[7, 3, 4], [2, 5, 1], ['*', 6, 8]]
[[7, 3, 4], ['*', 5, 1], [2, 6, 8]]
[['*', 3, 4], [7, 5, 1], [2, 6, 8]]
[[3, '*', 4], [7, 5, 1], [2, 6, 8]]
[[3, 5, 4], [7, '*', 1], [2, 6, 8]]
[[3, 5, 4], [7, 1, '*'], [2, 6, 8]]
[[3, 5, '*'], [7, 1, 4], [2, 6, 8]]
[[3, '*', 5], [7, 1, 4], [2, 6, 8]]
[[3, 1, 5], [7, '*', 4], [2, 6, 8]]
[[3, 1, 5], ['*', 7, 4], [2, 6, 8]]
[[3, 1, 5], [2, 7, 4], ['*', 6, 8]]
[[3, 1, 5], [2, 7, 4], [6, '*', 8]]
[[3, 1, 5], [2, '*', 4], [6, 7, 8]]
[[3, 1, 5], ['*', 2, 4], [6, 7, 8]]
[['*', 1, 5], [3, 2, 4], [6, 7, 8]]
[[1, '*', 5], [3, 2, 4], [6, 7, 8]]
[[1, 2, 5], [3, '*', 4], [6, 7, 8]]
[[1, 2, 5], [3, 4, '*'], [6, 7, 8]]
[[1, 2, '*'], [3, 4, 5], [6, 7, 8]]
[[1, '*', 2], [3, 4, 5], [6, 7, 8]]
[['*', 1, 2], [3, 4, 5], [6, 7, 8]]

Path cost: 22

Profiler report : bfs_7.3_4.pdf

Puzzle : 5
Max queue size: 105272
Action sequence:
['RIGHT', 2, 2]
['UP', 1, 2]
['LEFT', 1, 1]
['DOWN', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['UP', 0, 0]
['RIGHT', 0, 1]
['DOWN', 1, 1]
['LEFT', 1, 0]
['DOWN', 2, 0]
['RIGHT', 2, 1]
['RIGHT', 2, 2]
['UP', 1, 2]
['UP', 0, 2]
['LEFT', 0, 1]
['DOWN', 1, 1]
['DOWN', 2, 1]
['RIGHT', 2, 2]
['UP', 1, 2]
['LEFT', 1, 1]
['LEFT', 1, 0]
['UP', 0, 0]

State sequence:
[[1, 3, 8], [4, 7, 5], [6, 2, '*']]
[[1, 3, 8], [4, 7, '*'], [6, 2, 5]]
[[1, 3, 8], [4, '*', 7], [6, 2, 5]]
[[1, 3, 8], [4, 2, 7], [6, '*', 5]]
[[1, 3, 8], [4, 2, 7], ['*', 6, 5]]
[[1, 3, 8], ['*', 2, 7], [4, 6, 5]]
[['*', 3, 8], [1, 2, 7], [4, 6, 5]]
[[3, '*', 8], [1, 2, 7], [4, 6, 5]]
[[3, 2, 8], [1, '*', 7], [4, 6, 5]]
[[3, 2, 8], ['*', 1, 7], [4, 6, 5]]
[[3, 2, 8], [4, 1, 7], ['*', 6, 5]]
[[3, 2, 8], [4, 1, 7], [6, '*', 5]]
[[3, 2, 8], [4, 1, 7], [6, 5, '*']]
[[3, 2, 8], [4, 1, '*'], [6, 5, 7]]
[[3, 2, '*'], [4, 1, 8], [6, 5, 7]]
[[3, '*', 2], [4, 1, 8], [6, 5, 7]]
[[3, 1, 2], [4, '*', 8], [6, 5, 7]]
[[3, 1, 2], [4, 5, 8], [6, '*', 7]]
[[3, 1, 2], [4, 5, 8], [6, 7, '*']]
[[3, 1, 2], [4, 5, '*'], [6, 7, 8]]
[[3, 1, 2], [4, '*', 5], [6, 7, 8]]
[[3, 1, 2], ['*', 4, 5], [6, 7, 8]]
[['*', 1, 2], [3, 4, 5], [6, 7, 8]]

Path cost: 23

Profiler report : bfs_7.3_5.pdf

Puzzle : 6


Max queue size: 178223
Action sequence:
['LEFT', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['UP', 0, 0]
['RIGHT', 0, 1]
['RIGHT', 0, 2]
['DOWN', 1, 2]
['DOWN', 2, 2]
['LEFT', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['UP', 0, 0]
['RIGHT', 0, 1]
['RIGHT', 0, 2]
['DOWN', 1, 2]
['DOWN', 2, 2]
['LEFT', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['UP', 0, 0]
['RIGHT', 0, 1]
['RIGHT', 0, 2]
['DOWN', 1, 2]
['DOWN', 2, 2]
['LEFT', 2, 1]
['LEFT', 2, 0]
['UP', 1, 0]
['UP', 0, 0]

State sequence:
[[8, 7, 6], [5, 4, 3], [2, '*', 1]]
[[8, 7, 6], [5, 4, 3], ['*', 2, 1]]
[[8, 7, 6], ['*', 4, 3], [5, 2, 1]]
[['*', 7, 6], [8, 4, 3], [5, 2, 1]]
[[7, '*', 6], [8, 4, 3], [5, 2, 1]]
[[7, 6, '*'], [8, 4, 3], [5, 2, 1]]
[[7, 6, 3], [8, 4, '*'], [5, 2, 1]]
[[7, 6, 3], [8, 4, 1], [5, 2, '*']]
[[7, 6, 3], [8, 4, 1], [5, '*', 2]]
[[7, 6, 3], [8, 4, 1], ['*', 5, 2]]
[[7, 6, 3], ['*', 4, 1], [8, 5, 2]]
[['*', 6, 3], [7, 4, 1], [8, 5, 2]]
[[6, '*', 3], [7, 4, 1], [8, 5, 2]]
[[6, 3, '*'], [7, 4, 1], [8, 5, 2]]
[[6, 3, 1], [7, 4, '*'], [8, 5, 2]]
[[6, 3, 1], [7, 4, 2], [8, 5, '*']]
[[6, 3, 1], [7, 4, 2], [8, '*', 5]]
[[6, 3, 1], [7, 4, 2], ['*', 8, 5]]
[[6, 3, 1], ['*', 4, 2], [7, 8, 5]]
[['*', 3, 1], [6, 4, 2], [7, 8, 5]]
[[3, '*', 1], [6, 4, 2], [7, 8, 5]]
[[3, 1, '*'], [6, 4, 2], [7, 8, 5]]
[[3, 1, 2], [6, 4, '*'], [7, 8, 5]]
[[3, 1, 2], [6, 4, 5], [7, 8, '*']]
[[3, 1, 2], [6, 4, 5], [7, '*', 8]]
[[3, 1, 2], [6, 4, 5], ['*', 7, 8]]
[[3, 1, 2], ['*', 4, 5], [6, 7, 8]]
[['*', 1, 2], [3, 4, 5], [6, 7, 8]]

Path cost: 28



15 Puzzle!
Warning: I highly recommend you do not attempt this section before you’re sure you’ve com- pleted all the main parts of the assignment.
With that out of the way, consider the following two 15 puzzle instances:
(defvar *15-puzzle-1* #2A((13 10 11 6)
(5 7 4 8)
(1 12 14 9)
(3 15 2 nil)))

(defvar *15-puzzle-2* #2A((13 10 11 6)
(5 7 4 8)
(2 12 14 9)
(3 15 1 nil)))
One of these is solvable, the other is not! If you can figure out which one has a solution, try solving it first with your breadth-first search, and then with your A* search. You may have to look into using a better heuristic than even the Manhattan distance with A*!
What happens with breadth-first search on this puzzle?  Include  some  profiler  output,  stack traces, or other error information to back up your conclusion here.
For full credit, you should also include a listing of the optimal solution to whichever of these is solvable. Explain how you got it (e.g. ”A* search with the linear conflict + Manhattan distance heuristic”). If you used a new heuristic, you should include your implementation of it with the rest of your code.


