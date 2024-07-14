for i in range(int(input())) :
    l = []
    a, *b = map(int, input().split())
    b = list(b)
    b.sort(reverse=True)
    for j in range(len(b)-1) :
        l.append(b[j] - b[j+1])
    print('Class %d' % (i+1))
    print('Max %d, Min %d, Largest gap %d' % (max(b), min(b), max(l)))

