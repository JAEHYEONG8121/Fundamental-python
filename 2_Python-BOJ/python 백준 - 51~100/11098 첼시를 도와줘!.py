n = int(input())
for i in range(n) :
    p = int(input())
    a = -1
    b = ''
    for j in range(p) :
        c, d = input().split()
        c = int(c)
        if c > a :
            a = c
            b = d
    print(b)
