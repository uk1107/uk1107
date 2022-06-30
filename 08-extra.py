N,K  = map(int,input().split())
def calcpat(N,K):
    dp = [[0 for i in range(N+1)] for i in range(N+1)]
    for i in range(N+1):
        for j in range(N+1):
            if i == 0:
                dp[i][j] = 0
            if j == 0 and i <= K:
                dp[i][j] = 1          
            elif i >= j and i - j <= K:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            else:
                dp[i][j] = 0
    return dp[N][N]

print(calcpat(N,K) % 998244353)

            