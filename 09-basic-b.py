import sys
import resource
from collections import deque

sys.setrecursionlimit(1000000)
resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))

H,W = map(int, input().split())
sy,sx = map(int, input().split())
sy -= 1
sx -= 1
gy,gx = map(int, input().split())
gy -= 1
gx -= 1
meiro = []
for i in range(H):
    a = [i for i in input()]
    meiro.append(a)

waiting  = deque()
count = 0
waiting.append((sy,sx,count))
done  = [[0] * W for i in range(H)]

while True:
    y,x,count = waiting.popleft()
    if y == gy and x == gx:
        print(count)
        break
    
    if done[y][x] != 1:
        done[y][x] = 1

        for newy,newx in [[y+1,x],[y-1,x],[y,x+1],[y,x-1]]:
            if 0 <= newy <= H-1 and 0 <= newx <= W-1:
                if done[newy][newx] == 0 and meiro[newy][newx] == '.':
                    waiting.append((newy,newx,count+1))



       












