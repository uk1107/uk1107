def RollingHashMatch(text, pattern): 
    base = 31
    h = 10**9 + 7
    t_len = len(text)
    p_len = len(pattern)
    t_hash = 0
    p_hash = 0
    k = 0
    for i in range(p_len):
        t_hash += (((base) **(p_len-(i+1)))* (text[i])) % h
        p_hash += (((base) **(p_len-(i+1)))* (pattern[i])) % h
    t_hash %= h
    p_hash %= h
    if t_hash == p_hash:
        print(0) 
    j = p_len
    count = 0
    basemod = 1
    for i in range(p_len):
        basemod *= base
        if basemod > h:
            basemod %= h

    while j < t_len:
        t_hash = (base*t_hash - basemod*text[count] + text[j]) % h
        count += 1
        j += 1
        if t_hash == p_hash:
            print(count)
    return " "

S = [s for s in input()]
for i in range(len(S)):
    S[i] = ord(S[i])
T = [t for t in input()]
for i in range(len(T)):
    T[i] = ord(T[i])
print(RollingHashMatch(S,T))
