# 반복 입력을 처리하는 map()함수
N = int(input('몇 행?: '))
arr = [list(map(int, input().split()) for row in range(N))]
print(arr)

# map안의 input에다가 2 3 4 와 같은 열거형객체를 넣어주면,
# 스페이스바를 기준으로 2하나 3하나 4하나 각각 분리하여 list로 만들어진다