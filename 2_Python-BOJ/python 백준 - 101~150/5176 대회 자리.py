for _ in range(int(input())) :
    p, m = map(int, input().split())
    l = []
    for i in range(p) :
        n = int(input())
        l.append(n)
    s = set(l)
    l = list(s)
    