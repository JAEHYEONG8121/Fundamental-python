for i in range(int(input())) :
    h, w, n = map(int, input().split())
    floor = n % h
    num = n // h + 1
    if n % h == 0 :
        floor = h
        num = n // h
    print(floor * 100 + num)

# 별로 어렵지 않은 문제지만, n % h == 0인 경우를 생각하지 못했다
# 모든 경우를 잘 고려하자!
