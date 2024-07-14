# 리스트 모든 요소 제곱 후 출력
numList = [1, 2, 3, 4]

def square (x) :
    return x ** 2

result = list(map(square, numList))
print(result)