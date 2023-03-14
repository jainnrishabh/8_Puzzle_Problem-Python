class Node:
    def __init__(self, data, depth=0, move = None, prev = None):
        self.data = data    # Assign data
        self.depth = depth  # Assign depth
        self.move = move    # Assign action performed 
        self.prev = prev    # Intially assign prev as null
  
class LinkedList:
    def __init__(self):
        self.head = None    # Assign head to null initially