a = list(map(int, input().split()))
b = list(map(int, input().split()))
A, B = 0, 0

for i in range(len(a)) :
    if a[i] > b[i] :
        A += 1
    elif a[i] < b[i] :
        B += 1
    else :
        pass
if A == B :
    print('D')
elif A > B :
    print('A')
elif B > A :
    print('B')