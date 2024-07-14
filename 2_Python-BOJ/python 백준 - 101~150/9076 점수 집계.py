for i in range(int(input())) :
    l = list(map(int, input().split()))
    l.remove(max(l))
    l.remove(min(l))
    if max(l) - min(l) >= 4 :
        print('KIN')
    else :
        print(sum(l))
