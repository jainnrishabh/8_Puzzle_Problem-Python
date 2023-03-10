import copy

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

        # if len(self.heap) == 0:
        #     self.heap.insert(0,item)
        # else:  
        #     for count, node in enumerate(self.heap):
        #         if node[0] == item[0]:
        #             new_count = copy.deepcopy(count)
        #             while self.heap[new_count][0] == item[0]:
        #                 new_count += 1
        #                 if(new_count >= len(self.heap)):
        #                     break

        #             self.heap.insert(new_count, item)  
        #             break
        #         elif node[0] < item[0]:
        #             self.heap.insert(count, item)
        #             break  
# frontier = PriorityQueue()
# frontier.append((3, 2))
# frontier.append((3, 1))
# frontier.append((3, 0))
# frontier.append((3, 4))
# frontier.append((3, 5))

# while frontier.heap:
#     print(frontier.get())
