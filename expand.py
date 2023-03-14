import copy
import constants

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
    
def result(location,action,board):
    # copy of a board so that we can modify it 
    newBoard = copy.deepcopy(board)
    temp = copy.deepcopy(newBoard[action[1]][action[2]]) 
    newBoard[action[1]][action[2]] = copy.deepcopy('*')
    newBoard[location[0]][location[1]]  = copy.deepcopy(temp)
    # return new board after moving * - NIL to the new location 
    return newBoard