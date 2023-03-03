import numpy as np
import heapq

Class Heap:
    def __init__(self, arr,t = True):
        if t:
            arr = [-a fo a in arr]
            self.sign = -1
        else: self.sign = 1
        self.ary = arr
        self.s = 0
        heapq.heapify(self.ary)
    
    def pop(self):
        return heapq.heappop(self.ary) * self.sign

    def push(self.i):
        heapq.heappush(self.ary, i * self.sign)

    def top(self):
        return self.ary[0] * self.sign
        

