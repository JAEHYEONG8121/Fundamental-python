for i in range(int(input())) :
    n = int(input())
    l = list(map(int, input().split()))
    print((max(l) - min(l)) * 2)