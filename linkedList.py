class Node:
    # Function to initialise the node object
    def __init__(self, data, depth=0, move = None, prev = None):
        self.data = data   # Assign data
        self.depth = depth # Assign depth
        self.move = move
        self.prev = prev   # Initialize prev as null
  
# Linked List class contains a Node object
class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None


def isCycle(list):
    s = set()
    temp = list
    while (temp):

        # If we already have
        # this node in hashmap it
        # means there is a cycle
        # (Because we are encountering
        # the node second time).
        if (temp in s):
            return True

        # If we are seeing the node for
        # the first time, insert it in hash
        s.add(temp)

        temp = temp.prev

    return False