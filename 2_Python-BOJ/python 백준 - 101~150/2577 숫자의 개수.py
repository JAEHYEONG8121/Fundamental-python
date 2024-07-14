A = int(input())
B = int(input())
C = int(input())
s = str(A*B*C)
lst = []
for i in s :
    lst.append(i)
for j in range(10) :
    print(lst.count(str(j)))
