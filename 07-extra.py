 
def cumsum(x): 
    result = [None] * (len(x)+1)
    result[0] = 0
    for i in range(len(x)):
        result[i+1] = result[i] + x[i]
    return result

def calcmax(length,numarr,betarr): 
    dp =  [[0 for _ in range(length)]for _ in range(length)]
    dp2 =  [[0 for _ in range(length)]for _ in range(length)]
    cumarr = cumsum(numarr)
    
    for i in range(length):
        for j in range(length):
            dp[j][i] = cumarr[j+1]-cumarr[i]
            if i == 0:
                dp2[j][i] = 0
            else: 
                k = 0
                c = []
                while k < i:
                    if dp[i-1][k] != dp[j][i]:
                        c.append(dp2[i-1][k])
                    k += 1
                if not c:
                    if i == j:
                        dp[j][i] += dp[j-1][i-1]
                else:
                    dp2[j][i] += max(c) + betarr[i-1]
              
    maxnum = max(dp2[length-1])
    return maxnum

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

print(calcmax(N,A,B))

                        

            
                
                   
            



            
