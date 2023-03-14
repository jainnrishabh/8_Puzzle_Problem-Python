import copy
import constants

class Node:
    def __init__(self, data, depth=0, move = None, prev = None):
        self.data = data   # Assign data
        self.depth = depth # Assign depth
        self.move = move   # Assign move performed 
        self.prev = prev   # Initialize prev as null
  
class LinkedList:
    def __init__(self):
        self.head = None

def isCycle(list):
    s = set()
    temp = list
    while (temp):
        if (temp in s):
            return True
        s.add(temp)
        temp = temp.prev
    return False

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def append(self, item):
        priority, state = item
        index = len(self.heap)
        for idx, (p, s) in enumerate(self.heap):
            if priority < p:
                index = idx
                break
        self.heap.insert(index, item)
            
    def get(self):
        return self.heap.pop(0)
        
    def empty(self):
	    return len(self.heap) == 0 

def expand(board):
    for i in range(len(board.data)):
            for j in range(len(board.data[i])):
                if board.data[i][j] == '*':
                    location = [i,j]; 
    finalResult = []
    for action in possible_actions(location):
        finalResult.append([result(location,action,board.data) , action])
    return finalResult

def possible_actions(location):
    actions = ["RIGHT","LEFT","UP","DOWN"]
    actionstopeform = []
    
    for x in actions:
        # for moving right 
        if x == "RIGHT":
            if location[1]+1 < len(constants.board):
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
            if location[0]+1 < len(constants.board):
                actionstopeform.append([x,location[0]+1,location[1]])

    return actionstopeform
    
def result(location,action,board):
    newBoard = copy.deepcopy(board)
    temp = copy.deepcopy(newBoard[action[1]][action[2]]) 
    newBoard[action[1]][action[2]] = copy.deepcopy('*')
    newBoard[location[0]][location[1]]  = copy.deepcopy(temp)
    return newBoard



    

