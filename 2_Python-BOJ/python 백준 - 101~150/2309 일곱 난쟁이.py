lst = [int(input()) for _ in range(9)]
s = sum(lst)

for i in range(8) :
    for j in range(i+1, 9) :
        if s - (lst[i] + lst[j]) == 100 :
            n1 = lst[i]
            n2 = lst[j]
lst.remove(n1)
lst.remove(n2)
lst.sort()
for i in lst :
    print(i)
