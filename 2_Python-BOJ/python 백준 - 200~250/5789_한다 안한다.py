for _ in range(int(input())) :
    s = input()
    if int(s[len(s)//2]) == int(s[len(s)//2-1]) :
        print('Do-it')
    elif int(s[len(s)//2]) != int(s[len(s)//2-1]) :
        print('Do-it-Not')