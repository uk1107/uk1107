import heapq

N,M = map(int,input().split())
edge_list = [[] * N for i in range(N)]
for i in range(M):
    arr = list(map(int,input().split()))
    arr[0] -= 1
    arr[1] -= 1
    edge_list[arr[0]].append(arr[1:3])
    edge_list[arr[1]].append(arr[::2])

def dijkstra_heap(V,e_list,S):
    inf = float('inf')
    done = [False]*V
    dist = [inf]*V
    dist[S] = 0
    node_heap = []
     
    heapq.heappush(node_heap, [dist[S], S])
    while node_heap:
        tmp = heapq.heappop(node_heap)
        cur_node = tmp[1]
        if not done[cur_node]:
            for i in e_list[cur_node]:
                if dist[i[0]] > dist[cur_node] + i[1]:
                    dist[i[0]] = dist[cur_node] + i[1]
                    heapq.heappush(node_heap,[dist[i[0]],i[0]])
                    
        done[cur_node] = True
    return dist

startcost = dijkstra_heap(N,edge_list,0)
goalcost = dijkstra_heap(N,edge_list,N-1)

K = int(input())
startarr = []
goalarr = []
for i in range(K):
    vdarr = list(map(int,input().split()))
    minsforv = startcost[vdarr[0]-1]
    mingforv = goalcost[vdarr[0]-1] 
    startarr.append(vdarr[1]+minsforv)
    goalarr.append(vdarr[1]+mingforv)

startmin = min(startarr)
goalmin = min(goalarr)
print(min(startcost[N-1],startmin+goalmin))












