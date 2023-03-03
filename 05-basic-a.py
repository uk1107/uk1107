
def shakersort(seq):
    left = 0
    right = len(seq)-1
    swapped = 0
    while left < right:
        for i in range(left,right):
            if seq[i+1] < seq[i]:
                seq[i],seq[i+1] = seq[i+1],seq[i]
                swapped = i
        right = swapped
        for i in range(right,left,-1):
            if seq[i-1] > seq[i]:
                seq[i],seq[i-1] = seq[i-1],seq[i]
                swapped = i
        left = swapped
    return seq

N = int(input())
arr = list(map(int,input().split()))
print(*shakersort(arr))
