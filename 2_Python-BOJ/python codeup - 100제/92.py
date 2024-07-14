n = int(input())
l = [0 for i in range(23)]
lst = list(map(int, input().split()))
for i in lst :
    l[i - 1] += 1
for i in l :
    print(i)

