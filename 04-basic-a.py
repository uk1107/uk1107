
arr = [None] * (10**5)

def add(i):
    c = i
    i %= 10**5
    if arr[i] == None:
        arr[i] = c
    else:
        while arr[i] != None:
            i += 1
            if i == 10**5:
                i = 0
        arr[i] = c

def search(i):
    d = i
    i %= 10**5
    if arr[i] == d:
        return "found"
    elif arr[i]  == None:
        return "not found"
    else:
        k = 0
        while k < len(arr):
            if i == 10**5:
                i = 0
                k += 1
            else:           
                if arr[i] == d:
                    return "found"
                elif arr[i] == None:
                    return "not found"
                k += 1
                i += 1 
              
  
Q = int(input())
for i in range(Q):
    a = list(map(int,input().split()))
    if a[0] == 0:
        add(a[1])
    elif a[0] == 1:
        print(search(a[1]))

    




















