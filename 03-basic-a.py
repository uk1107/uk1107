import sys

class Queue:

    def __init__(self, size:int):
        self.queue = [None] * size
        self.head = 0
        self.tail = 0
       
    def enqueue(self,a: int):
        if (self.queue[self.tail] == None):
            self.queue[self.tail] = a
            self.tail  = (self.tail + 1) % len(self.queue)
        else:
            print('queue is full')
            

    def dequeue(self):
        if (self.queue[self.head] != None):
            tmp = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % len(self.queue)
            print (tmp)
        else:
            print('queue is empty')
    
Q, K  = map(int,input().split())
T = Queue(K)
for i in range(Q):
    a = list(map(int,input().split()))
    if a[0] ==  1 and T.enqueue(a[1]):
        T.enqueue(a[1])

    elif a[0] ==  2:
        T.dequeue()