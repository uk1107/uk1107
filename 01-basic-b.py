import sys

n, m =  map(int,input().split())
a = list(map(int,input().split()))
sum = 0
b = []

for i in range(m):
    sum += a[i]
b.append(sum)

for j in range(n-m):
    sum = sum - a[j] + a[j+m]
    b.append(sum)

c = max(b)
d = b.index(max(b))+1
print(c,d)    

