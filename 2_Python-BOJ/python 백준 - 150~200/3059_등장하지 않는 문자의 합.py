for _ in range(int(input())) :
    str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sum = 0
    s = input()
    for i in s :
        if i in str :
            str = str.replace(i, "")
    for i in str :
        sum += ord(i)
    print(sum)