for i in range(int(input())):
    n = int(input())
    k = int(input())
    l = [i for i in range(1, k+1)]
    for i in range(n-1) :
        for j in range(k) :
            if j == 0 :
                l[j] = 1
            else :
                l[j] = l[j-1] + l[j]
    print(sum(l[:k+1]))
            
                

    