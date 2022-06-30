N,M = map(int,input().split())
inf = float('inf')
edge = [[inf] * N for i in range(N)]
for i in range(M):
    a,b,d = (map(int,input().split()))
    edge[a][b] = d
Q = int(input())

def WarshallFloyd(V,e_matrix):
    dist = e_matrix
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] != inf and dist[k][j] != inf:
                    dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])

    return dist

result = WarshallFloyd(N,edge)
for i in range(Q):
    q1,q2 = map(int,input().split())
    if result[q1][q2] != inf:
        print(result[q1][q2])
    else:print("INF")


