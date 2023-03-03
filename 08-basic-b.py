N,K = map(int,input().split())
A = list(map(int,input().split()))

def calcsum(arr):
    sumarr = [0] * len(arr)
    for i in range(len(arr)):
        if i == 0:
            sumarr[0] = arr[0]
        else:
            sumarr[i] = sumarr[i-1]+arr[i]
    return sumarr

def amewake(limhuman,limcandy,limitnum):
    dp = [[0 for i in range(limcandy+1)]for i in range(limhuman+1)]
    sumdp = []
    for i in range(limhuman+1):
        if i >= 1:
            sumdp.append(calcsum(dp[i-1]))
        for j in range(limcandy+1):
            if i == 0:
                dp[i][j] = 0
            if j == 0:
                dp[i][j] = 1
            if i >= 1 and j >= 1:
                if j <= limitnum[i-1]:
                    dp[i][j] = sumdp[i-1][j]
                else:
                    dp[i][j] = sumdp[i-1][j]-sumdp[i-1][j-limitnum[i-1]-1]
    ans = dp[limhuman][limcandy] % (10**9+7)
    return ans

print(amewake(N,K,A))


            
