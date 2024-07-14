# round(p/h, 1) -> p/h을 소수 첫 번째 자리까지 받겠다! = 소수 두 번째 자리에서 반올림!
# h에다가는 입력받은 c값을 정수로 더해주고
# p값은 입력받은 g를 소수점 계산해야하므로 float로 형변환 해준다!
T = int(input())
for i in range(T):
    N = int(input())
    h = 0
    p = 0
    for i in range(N):
        c, g = map(str, input().split())
        h += int(c)
        p += float(c) * float(g)
    p = round(p / h, 1)
    print(h, p)
