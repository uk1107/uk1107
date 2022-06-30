import sys

import resource

resource.setrlimit(resource.RLIMIT_STACK, (-1, -1)) 

sys.setrecursionlimit(1000000) 


N = int(input())
R,B = map(int,input().split())
Mr = int(input())

ab = [map(int,input().split()) for i in range(Mr)]
a,b = [list(i) for i in zip(*ab)]
Mb = int(input())
cd = [map(int,input().split()) for i in range(Mb)]
c,d = [list(i) for i in zip(*cd)]
graphred  = [[]for i in range (N)]
graphblue  = [[]for i in range (N)]
for i in range(Mr):
    graphred[a[i]-1].append(b[i])
for i in range(Mb):
    graphblue[c[i]-1].append(d[i])    

class rbsearch:
    def __init__(self,N):
        self.count = 1
        self.donered = [0] * N
        self.doneblue = [0] * N
        self.N = N

    def bfsredblue(self,nodered,nodeblue,graphred,graphblue):
        if self.count >= (self.N)**3:
            print(-1)
            return

        nextnodered = []
        nextnodeblue = []
            
        for i in nodered:
            self.donered[i-1] += 1  
            nextnodered += graphred[i-1]        
        for j in nodeblue:
            self.doneblue[j-1] += 1 
            nextnodeblue += graphblue[j-1]
        if set(nextnodered) & set(nodeblue):
            print(self.count)
            return
        else: self.count += 1
        if set(nextnodered) & set(nextnodeblue):
            print(self.count)
            return
        else: 
            self.count += 1
            self.bfsredblue(nextnodered,nextnodeblue,graphred,graphblue)
            
if R == B:
    print(0)
else:
    rb = rbsearch(N)
    startred = [R]
    startblue = [B]
    rb.bfsredblue(startred,startblue,graphred,graphblue)