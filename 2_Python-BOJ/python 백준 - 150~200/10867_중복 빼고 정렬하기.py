n = int(input())
m = set(map(int, input().split()))
l = list(m)
l.sort()
for i in l :
    print(i, end = ' ')