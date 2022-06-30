
def createTable(pattern):
    skip = [0] * len(pattern)
    score = 0
    for i in range(1,len(pattern)-1):
 
        if pattern[i] == pattern[score]:
            score += 1
            skip[i+1] = score
        else:
            score = 0
            skip[i+1] = score
            

    return skip
            
def kmp(text,pattern):
    skip = createTable(pattern)
    t_len = len(text)
    p_len = len(pattern)
    t_i = p_i = 0
    if t_len < p_len: return -1
    while t_i < t_len and p_i < p_len:
        if text[t_i] == pattern[p_i]:
            t_i += 1
            p_i += 1
        elif p_i == 0:
            t_i += 1
        else:
            p_i = skip[p_i]
    if p_i == p_len:
        return t_i - p_i
    else:
        return -1

S = input()
T = input()
print(kmp(S,T))