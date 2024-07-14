
for _ in range(3) :
    l = []
    cnt = 1
    n = input()
    for i in range(1, len(n)) :
        if n[i - 1] == n[i] :
            cnt += 1
            l.append(cnt)
        elif n[i - 1] != n[i] :
            l.append(cnt)
            cnt = 1
    print(max(l))
    

