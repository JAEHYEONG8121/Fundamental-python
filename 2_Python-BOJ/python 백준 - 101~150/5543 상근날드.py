a_lst = []
b_lst = []
lst = []
for _ in range(3) :
    a_lst.append(int(input()))
for _ in range(2) :
    b_lst.append(int(input()))
for i in a_lst :
    for j in b_lst :
        lst.append(i+j - 50)

print(min(lst))

'''
a=[0]*3
b=[0]*2

for i in range(3):
    a[i]=int(input())

for g in range(2):
    b[g]=int(input())

print(min(a)+min(b)-50)

'''
