s = input()
if len(s) < 10 :
    print(s)
else :
    for i in range(len(s)//10) :
        print(s[10*i:10*(i+1)])
        if i == (len(s)//10 - 1) :
            print(s[10*(i+1):])