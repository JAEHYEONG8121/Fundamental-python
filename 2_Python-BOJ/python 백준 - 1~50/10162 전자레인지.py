while True :
    n = int(input())
    if n == -1 :
        break
    else :
        lst = []
        for i in range(1, n) :
            if n % i == 0 :
                lst.append(i)
                sum = 0
                for j in range(len(lst)) :
                    sum += lst[j]
        if n == sum :
            print('%d =' % n, end = '')
            for k in range(len(lst)) :
                if 0 <= k < len(lst) -1 :
                    print(' %d +' % lst[k], end = '')
                if k == len(lst) - 1 :
                    print(' %d' % lst[len(lst) - 1])
        else :
            print('%d is NOT perfect.' % n)