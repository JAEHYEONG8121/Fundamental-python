for _ in range(int(input())) :
    a, b = map(int, input().split())
    print(b*2 - a, end = ' ')
    print(b - (b*2 - a))