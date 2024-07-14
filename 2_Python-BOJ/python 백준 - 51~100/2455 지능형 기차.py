m = 0
lst = []
for i in range(4) :
    li = list(map(int, input().split()))
    m += li[1] - li[0]
    lst.append(m)
print((max(lst)))