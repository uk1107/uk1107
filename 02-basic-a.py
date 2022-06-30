import sys

n, k = map(int,input().split())
m = 1000000007

def kaijo(a,b):
    t = 1
    for i in range(1,a+1):
        t *= i
        if(t > b):
            t = t%b
    return t

def power(a,n):
    M = 1000000007
    if n == 0: return 1
    tmp = power(a*a%M, n//2)
    if n%2: tmp = tmp*a%M

    return tmp

k1 = (kaijo(k,m)*kaijo(n-k,m))%m
k2 = power(k1,m-2)
d = (kaijo(n,m)*k2)%m
print(d)
    
    


