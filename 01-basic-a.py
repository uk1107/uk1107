import sys

m, l = map(int,input().split())
n = int(input())
item_list = []
for i in range(n):
    item,*values = input().split()
    price,level = map(int,values)
    lst = [item,price,level]
    item_list.append(lst)       

for j in range(n):
    if item_list[j][1] <= m and item_list[j][2] <= l:
        print(item_list[j][0],item_list[j][1])

    

    