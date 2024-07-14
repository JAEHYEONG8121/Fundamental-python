# a의 요소를 모두 int로 반환하기
a = [1.2, 2.5, 3.7, 4.6]

# 리스트 내포
a = [int(i) for i in a]
print(a)

# map()함수
a = list(map(int, a))
print(a)