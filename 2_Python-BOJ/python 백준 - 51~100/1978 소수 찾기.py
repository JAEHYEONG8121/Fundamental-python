N = int(input())
lst = list(map(int, input().split()))
print(lst)
li = []
for i in range(N) :
    for j in range(2, lst[i]) :
        if lst[i] != 1 and lst[i] % j != 0 :
            li.append(lst[i])
            s = set(li)
            le = list(li)
print(le)
print(len(le))
