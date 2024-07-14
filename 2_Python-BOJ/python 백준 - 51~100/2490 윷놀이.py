for i in range(3) :
    list = input().split()
    if list.count('0') == 1 and list.count('1') == 3 :
        print('A')
    elif list.count('0') == 2 and list.count('1') == 2 :
        print('B')
    elif list.count('0') == 3 and list.count('1') == 1 :
        print('C')
    elif list.count('0') == 4 :
        print('D')
    elif list.count('1') == 4 :
        print('E')
