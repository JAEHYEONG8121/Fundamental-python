# 입력된 두 수 사이에서 0의 개수를 구하는 것이므로
# 일단 정수로 두 수를 받아서 for문의 range의 범위로 설정한다
# for문 안에서 이 두 수를 문자열 형태로 변환하여 .count('0')을 이용하여
# 문자열 안의 0의 개수를 찾고, 이를 cnt 변수에다가 더해간다
for _ in range(int(input())) :
    a, b = map(int, input().split())
    cnt = 0
    for i in range(a, b+1) :
        cnt += str(i).count('0')
    print(cnt)

