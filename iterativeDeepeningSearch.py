import queue 
import linkedList
import expand
import constants

board = constants.board
goalBoard = constants.goalBoard
failure =  constants.failure
cut_off =  constants.cut_off

def hasCycle(list):
    s = set()
    temp = list
    while (temp):
        if (temp in s):
            return True
        s.add(temp)
        temp = temp.prev
    return False

def idfs(board,depth):
    for step in range(depth):
        result = depthFirstSearch(board, step)
        if(result != cut_off): 
            return result

def depthFirstSearch(board, step):
    result = failure
    frontier = queue.LifoQueue()
    node = linkedList.Node(data=board)
    frontier.put(node)

    while not frontier.empty():
        val = frontier.get()
        if goalBoard == val.data:
            return val
        if  val.depth > step:
            result = cut_off
        elif not hasCycle(val):
            for child in expand.expand(val):
                temp =  linkedList.Node(data=child[0], depth =val.depth + 1 ,move= child[1] , prev=val)
                frontier.put(temp)
    return result

pathCost = 0
solution = idfs(board,50)
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