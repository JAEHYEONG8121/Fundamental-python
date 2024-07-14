l = []
for _ in range(int(input())) :
    x, y = map(int, input().split())
    l.append((x, y))

for i in l :
    rank = 1
    for j in l :
        if i[0] < j[0] and i[1] < j[1] :
            rank += 1
    print(rank, end = ' ')

# 키와 몸무게를 튜플로 묶어서 한꺼번에 리스트에 담기
# rank = 1로 두고, 이중 for문을 돌려서 리스트안에서 키와 몸무게를 둘 다 비교하여
# 작으면 rank를 1증가시켜준다!
# 결국 이 문제는 자기 등수만 구하면 되는 문제이다!