cnt = 1
k = ''
while True :
    a = input()
    b = input()
    if (a == 'END') and (b == 'END') :
        break
    else :
        for i in b :
            if (i in a) and (b.count(i) == a.count(i)) :
                k = 'Y'
            else :
                k = 'N'
                
    if k == 'Y' :
        print('Case %d: same'%cnt)
    elif k == 'N' :
        print('Case %d: different'%cnt)

    cnt += 1

