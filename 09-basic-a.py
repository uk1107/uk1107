import sys
import resource

sys.setrecursionlimit(1000000)
resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))

N, M, S, T = map(int,input().split())
graph  = [[]for i in range (N)]
for i in range(M):
   a,b = map(int,input().split())
   graph[a-1].append(b-1)
   graph[b-1].append(a-1)

done = [0] * N
def dfs(edges,start,end,N):
    done[start] = 1
    for n in edges[start]:
       if done[n] == 0:
          done[n] = 1
          dfs(edges,n,end,N)
          if done[end] == 1:
              return('Yes')
    return('No')
print(dfs(graph,S,T,N))



