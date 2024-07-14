for _ in range(int(input())):
    a = [x for x in map(int, input().split()) if not x % 2]
    print(a)
    print(sum(a), min(a))