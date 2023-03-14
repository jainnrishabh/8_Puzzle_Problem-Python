import cProfile
import constants
import queue 
import linkedList
import expand
from collections import deque

board = constants.board
goalBoard = constants.goalBoard
failure =  constants.failure
cut_off =  constants.cut_off


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
        
def main():
    solution = bfs(board)
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

if __name__ == '__main__':
    cProfile.run('main()')