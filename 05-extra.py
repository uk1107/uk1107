

def battle(a,b):
    a.sort()
    b.sort()
    onum = 0
    enum = 0
    win = 0
    while(onum < len(a)):
        if a[onum] > b[enum]:
            win += 1
            onum += 1
            enum += 1
        else:
            onum += 1

    return win

N = int(input())
our = [None] * N
enemy = [None] * N
for i in range(N):
    a,b = map(int,input().split())
    our[i] = a*b
for i in range(N):
    c,d = map(int,input().split())
    enemy[i] = c*d

print(battle(our,enemy))

