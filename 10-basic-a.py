import heapq

N,M,S = map(int,input().split())
edges_list = [[] for i in range(N)]
for i in range(M):
    arr = list(map(int,input().split()))
    edges_list[arr[0]].append(arr[1:3])

def dijkstra_heap(N,S,edges_list):
    inf = float('inf')
    done = [False] * N
    dist = [inf] * N
    dist[S] = 0
    node_heap = []
    heapq.heappush(node_heap, [dist[S], S])

    while node_heap:
        tmp = heapq.heappop(node_heap)
        cur_node = tmp[1]
        if not done[cur_node]:
            for j in edges_list[cur_node]:
                if dist[j[0]] > dist[cur_node] + j[1]:
                    dist[j[0]] = dist[cur_node] + j[1]
                    heapq.heappush(node_heap, [dist[j[0]], j[0]])
        done[cur_node] = True
    
    for i in range(N):
        if dist[i] != inf:
            print(dist[i])

        else:print("INF")

dijkstra_heap(N,S,edges_list)
