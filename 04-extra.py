import sys

N,M = map(int,input().split())
suml = [None] * N
l = list(map(int,input().split()))
for i in range(N):
    if i == 0:
        suml[i] = l[i]
    else:
        suml[i] = l[i] + suml[i-1]

arr = [10**9+1] * (10**5+1)
arr[0] = 0

def place(w):
    left = -1
    right = len(arr)      
    while (right-left) != 1:
        mid = (left + right)//2
        if arr[mid] >= w: 
            right = mid
        else:
            left = mid        
    s = suml[right-1]
    arr[right] = w
    return 2*s

weight =  list(map(int,input().split()))
ans = 0
for i in range(M):
    ans += place(weight[i])
print(ans)



        
    





        


    
    
   