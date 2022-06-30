
def reversecheck(a,b):
    if (a == "p" and b == "d") or (a == "d" and b == "p") or (a == "b" and b == "q") or (a == "q" and b == "b"):
        return True
    else:
        return False

def reverse(S):
    L = len(S)
    R = [0] * L

    i = 1
    j = 0
    while i < L:
        while 0 <= i+j < L and 0 <= i-1-j < L and reversecheck(S[i+j],S[i-1-j]):
            j += 1 
        R[i] = j
        k = 1
        while j-R[i-k] > k <= i < L-k:
            R[i+k] = R[i-k]
            k += 1
        i += k
        j -= k
        if j < 0:
            j = 0
    return sum(R)

N = int(input())
S = input()
print(reverse(S))



