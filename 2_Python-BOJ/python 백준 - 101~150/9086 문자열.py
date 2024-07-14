for i in range(int(input())) :
    s = input()
    if len(s) == 1 :
        print(s+s)
    elif len(s) == 2 :
        print(s)
    else :
        print(s[0]+s[len(s)-1])