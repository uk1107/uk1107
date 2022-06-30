
N = int(input())
h = list(map(int,input().split()))

def searchmincost(N,h):
    mincost = [None] * N
    mincost[0] = 0
    mincost[1] = abs(h[1]-h[0])
    for i in range(2,N):
        mincost[i] = min(mincost[i-1] + abs(h[i]-h[i-1]), mincost[i-2] + abs(h[i]-h[i-2]))

    return(mincost[N-1])

print(searchmincost(N,h))

