import sys
N = int(input())
M = 998244353
a = [0] * (10**4+1)
s = [0] * (10**4+1)
def power(x,n,t):
    if n == 0: return 1
    tmp = power(x*x%t,n//2,t)
    if n%2: tmp = tmp*x%t
    return tmp
for i in range(10**4+1):
    
    a[i] = power(i+1,N,M-1)
for i in range(1,(10**4)):  
    s[1] = a[0]
    s[i+1] = s[i] +a[i]
    
    


Q = int(input())
for i in range(Q):
    K,l,r = map(int,input().split())
    if K > M:
            K = K%M
    f = s[r]-s[l-1]
    if f%M == 0: print(0)
    else: print(power(K,f,M))

        