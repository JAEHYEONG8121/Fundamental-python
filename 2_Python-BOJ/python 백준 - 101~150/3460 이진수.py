l = []
for i in range(int(input())) :
    n = int(input())
    b = bin(n)
    print(b)
    for j in b :
        if j == '1' :
            print(b.index(j), end = ' ')