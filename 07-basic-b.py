
def checksum(N,A,S):
    dp = [[-1 for _ in range(S+1)]for _ in range(N+1)]
    for i in range(N+1):
        for j in range(S+1):
            if i == 0:
                if j == 0: dp[i][j] = True
                else:dp[i][j] = False
            else:
                if (dp[i-1][j] or (j >= A[i-1] and dp[i-1][j-A[i-1]])):
                    dp[i][j] = True
                else: dp[i][j] = False
    
    if dp[N][S]: print("Yes")
    else: print("No")

    return

N,S = map(int, input().split())
A = list(map(int, input().split()))
checksum(N,A,S)
            



    