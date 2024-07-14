lst = []
sum = 0
for i in range(10) :
    a, b = map(int, input().split())
    sum += (b-a)
    lst.append(sum)
print(max(lst))