
N,W = map(int, input().split())
item = []
limitsum = 0
for i in range(N):
    a = list(map(int, input().split()))
    item.append(a)
    limitsum += a[1]

def napsac(N,W,item,limitsum):
    dp = [[0 for i in range(limitsum+1)] for i in range(N+1)]
    for n in range(N+1):
        for sumv in range(limitsum+1):
            compare = []
            if n == 0:
                dp[n][sumv] = 0
            else:
                compare = []
                pre1 = item[n-1][1]
                pre0 = item[n-1][0]             
                if sumv == pre1 :
                    compare.append(pre0)
                if dp[n-1][sumv] != 0 :
                    compare.append(dp[n-1][sumv])
                if sumv-pre1 >= 0:
                    if dp[n][pre1] != 0 and dp[n-1][sumv-pre1]!= 0:
                        compare.append(pre0+dp[n-1][sumv-pre1])

                if compare != []:
                    dp[n][sumv] = min(compare)
                

    k = limitsum
    maxsum = 0
    while True:
        arr = []     
        for i in range(N+1):
            if dp[i][k] != 0 and dp[i][k] <= W:
                arr.append(dp[i][k])
        if arr != []:
            maxsum = k
            break
        k -= 1
        if k  == 0:
            break
    return maxsum
     
print(napsac(N,W,item,limitsum))

            


