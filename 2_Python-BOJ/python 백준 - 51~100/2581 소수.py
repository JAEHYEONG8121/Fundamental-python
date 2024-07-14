M = int(input())
N = int(input())
lst = []
for i in range(M, N+1) :
    cnt = 0
    if i == 1 :
        cnt = 1
    else :
        for j in range(2, i) :
            if i == 1 :
                cnt +=1
            elif i % j == 0 :
                cnt+=1

    if cnt == 0 :
        lst.append(i)
if len(lst) == 0 :
    print(-1)
else :       
    print(sum(lst))
    print(min(lst))