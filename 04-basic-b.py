
N = int(input())
Arr = list(map(int,input().split()))



def nibutan(a, v):
    left = -1
    right = len(a)
        
    while (right-left) != 1:
        mid = (left + right)//2
        if a[mid] > v: 
            right = mid
        else:
            left = mid
    if right < len(a):
        return(a[right])
    else: return( "not exist")
    

Q = int(input())
for i in range(Q):
    s = int(input())
    print(nibutan(Arr,s))

