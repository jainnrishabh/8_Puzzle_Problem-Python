import copy

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
    actions = ['R','L','U','D']
    actionstopeform = []
    
    for x in actions:
        # for moving right 
        if x == 'R':
            if location[1]+1 < 3:
                actionstopeform.append([x,location[0],location[1]+1])
        # for moving left
        elif x == 'L':
            if location[1]-1 >= 0:
                actionstopeform.append([x,location[0],location[1]-1])
        # for moving up 
        elif x == 'U':
            if location[0]-1 >= 0:
                actionstopeform.append([x,location[0]-1,location[1]])
        # for moving down
        elif x == 'D':
            if location[0]+1 < 3:
                actionstopeform.append([x,location[0]+1,location[1]])

    return actionstopeform
    
def result(location,action,board):
    newBoard = copy.deepcopy(board)
    temp = copy.deepcopy(newBoard[action[1]][action[2]]) 
    newBoard[action[1]][action[2]] = copy.deepcopy('*')
    newBoard[location[0]][location[1]]  = copy.deepcopy(temp)
    return newBoard
