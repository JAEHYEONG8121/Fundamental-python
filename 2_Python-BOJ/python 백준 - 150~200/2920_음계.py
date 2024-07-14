l = list(map(int, input().split()))
c1, c2, c3 = 0, 0, 0
for i in range(1, len(l)) :
    if l[i] - l[i-1] == 1 :
        c1 += 1
    elif l[i-1] - l[i] == 1 :
        c2 += 1
    else :
        pass
if c1 == 7 :
    print('ascending')
elif c2 == 7 :
    print('descending')
else :
    print('mixed')
