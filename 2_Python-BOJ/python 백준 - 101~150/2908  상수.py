a, b = input().split()
A, B = int(a[::-1]), int(b[::-1])
if A > B :
    print(A)
elif A < B :
    print(B)
