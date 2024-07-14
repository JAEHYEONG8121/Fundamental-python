for _ in range(int(input())) :
    a, b = map(int, input().split())
    if a < b :
        print(1)
    elif a % b == 0 :
        print(a//b)
    elif a % b != 0 :
        print(a//b + 1)