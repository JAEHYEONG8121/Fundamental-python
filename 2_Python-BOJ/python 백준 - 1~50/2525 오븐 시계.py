# 먼저 시간, 분을 입력받고 / 분 단위로 숫자를 또 입력해준다
# 우선 들어온 c를 60을 기준으로 나눈 몫은 h(시간) 변수에 더해주고
# c를 60으로 나눈 나머지는 m(분) 변수에 더해주면 우선 c를 더해준 후에 h와 m의 값이 나온다
# 이 상태에서 h가 24이상일때, m이 60이상일 때 조건을 걸어주면 된다!
h, m = map(int, input().split())
c = int(input())
h += c // 60
m += c % 60

if m >= 60 :
    h += 1
    m -= 60
if h >= 24 :
    h-=24
print(h, m)