l = []
for _ in range(int(input())) :
    n = int(input())
    if n != 0 :
        l.append(n)
    else :
        del l[len(l)-1]
print(sum(l))
    