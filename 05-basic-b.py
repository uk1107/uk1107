
def qsort(seq,left,right):
    
    if right > left:   
        pivot = seq[(left + right)//2]
        cur_l = left
        cur_r = right
        while True: 
            while(seq[cur_l] < pivot):
                cur_l += 1
            while(seq[cur_r] > pivot):
                cur_r -= 1
            if(cur_r > cur_l):
                seq[cur_l],seq[cur_r] = seq[cur_r],seq[cur_l]
                cur_l += 1
                cur_r -= 1   
            else:
                break          
        qsort(seq, left, cur_r)
        qsort(seq,cur_r+1, right)

    return  seq   
    
N =int(input()) 
arr = list(map(int,input().split()))
s = qsort(arr,0,N-1)
for i in range(N):
    print(s[i],end = " ")

        
