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
