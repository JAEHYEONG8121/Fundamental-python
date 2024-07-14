n = int(input())
l = list(map(int, input().split()))
m = int(input())
lst = list(map(int, input().split()))

for i in lst :
    print(l.count(i), end = ' ')
