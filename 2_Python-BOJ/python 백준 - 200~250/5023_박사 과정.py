for _ in range(int(input())) :
    s = input()
    if s == 'P=NP' :
        print('skipped')
    else :
        a, b = map(int, s.split('+'))
        print(a+b)