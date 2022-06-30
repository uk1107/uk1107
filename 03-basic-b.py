

class Myheap:
    def __init__(self, size):
        self.inf = 0
        self.size = size + 1
        self.array = [self.inf]*self.size
        self.last = 0
    
    def add(self, value: int):
        if self.last != self.size:
            self.last += 1
            self.array[self.last] = value
            self.check_after_add(self.last)
    def remove(self):
        if (self.last != 0):
            removed = self.array[1]
            self.array[1] = self.array[self.last]
            self.array[self.last] = self.inf
            self.last -= 1
            self.check_after_remove(1)
            return removed
    def check_after_add(self, i):
        if i < 2: return
        if(self.array[i] > self.array[i//2]):
            self.array[i],self.array[i//2] = self.array[i//2],self.array[i]     
            return self.check_after_add(i//2)
    def check_after_remove(self,i):
        if (2*i > self.last) : return
        else:
            if (self.array[2*i]>self.array[2*i+1]):
                if (self.array[i] < self.array[2*i]):
                    self.array[i], self.array[2*i]  = self.array[2*i],self.array[i]     
                    return self.check_after_remove(2*i)
                else:return
            
            else:

                if (self.array[i] < self.array[2*i+1]):
                    self.array[i], self.array[2*i+1]  = self.array[2*i+1],self.array[i]     
                    return self.check_after_remove(2*i+1)
                else:return
            
Q = int(input())
t = Myheap(Q)
for i in range(Q):
    k = list(map(int,input().split()))
    
    if k[0] == 1:
        t.add(k[1])
    elif k[0] == 2:
        print(t.remove())
