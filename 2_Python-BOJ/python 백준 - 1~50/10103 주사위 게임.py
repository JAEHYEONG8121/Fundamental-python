n = int(input())
A, B = 100, 100
for i in range(n) :
    a, b = map(int, input().split())
    if a > b :
        B -= a
    elif a == b :
        pass
    else :
        A -= b
    
print(A, B)
