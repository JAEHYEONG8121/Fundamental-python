for _ in range(int(input())) :
    l = []
    n = list(map(int, input().split()))
    for i in n :
        if i % 2 == 0 :
            l.append(i)
    print(sum(l), end = ' ')
    print(min(l))

'''
for _ in range(int(input())):
    a = [x for x in map(int, input().split()) if not x % 2] -> 리스트 내포
    print(sum(a), min(a))
'''