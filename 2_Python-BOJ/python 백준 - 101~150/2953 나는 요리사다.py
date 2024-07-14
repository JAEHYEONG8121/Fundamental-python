lst = []
for i in range(5) :
    li = list(map(int, input().split()))
    lst.append(sum(li))
print(lst.index(max(lst))+1, max(lst))