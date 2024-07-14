# 10개 숫자를 리스트로 입력받는다!
# lst안에 있는 원소들이 그 리스트에 몇 번 들어있는지 lst.count()를 이용하여
# 그 카운트된 숫자를 또 다른 리스트에 넣는다
# 그 리스트에서 가장 높은 숫자의 인덱스를 추출
# 그 인덱스 숫자를 lst[index] 해주면 최빈값을 구할 수 있다.
'''
lst = []
li = []
lst = [int(input()) for i in range(10)]
for i in lst :
    li.append(lst.count(i))
m = max(li)
index = li.index(m)
print(int(sum(lst)/len(lst)))
print(lst[index])
'''

# collections 모듈의 Counter클래스 사용
# Counter('hello world') # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
# Counter('hello world').most_common() # [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]
# .most_common()메서드를 사용하면 데이터의 개수가 많은 순으로 정렬해준다!
from collections import Counter

arr=[int(input()) for i in range(10)]
val=Counter(arr).most_common()
print(val)
print(sum(arr)//10)
print(val[0][0])

