lst = []
li = []
l = []
for i in range(8) :    
    n = int(input())
    lst.append(n)
    li.append(n)
li.sort()
li = li[-5:]
for i in li :
    l.append(lst.index(i))
l.sort()

print(sum(li))
for i in l :
    print(i+1, end = ' ')

'''
A = [int(input()) for i in range(8)]
B = sorted(A, reverse=True)[0:5]
C = []
for i in B:
    C.append(A.index(i) + 1)
    C.sort()
print(sum(B))
print(*C)
'''


