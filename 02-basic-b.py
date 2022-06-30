import sys

M = 2*(10**6)

is_prime = [True] * (M+1)
is_prime[0] = False
is_prime[1] = False
for i in range(2,int(M**0.5)+1):
    if not is_prime[i]:
        continue
    for j in range(i*2,M+1,i):
        is_prime[j] = False
    
a = [0] * M
for i in range(M):
    if i%2 == 0: continue
    if is_prime[i] and is_prime[int((i+1)/2)]:
        a[i] = 1
s = [0] * (M+1)
for i in range(M):
    s[i+1] = s[i] + a[i]


Q = int(input())
for i in range(Q):
    l,r = map(int,input().split())
    print(s[r+1]- s[l])






    
