while True :
    l = list(map(int, input().split()))
    l.sort()
    if l[0] == 0 & l[1] == 0 & l[2] == 0 :
        break
    else : 
        if l[2] ** 2 == l[0] ** 2 + l[1] ** 2 :
            print('right')
        else :
            print('wrong')
