import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))
dic = {arr2[i] : i for i in range(len(arr2))}
for i in arr:
    print(dic[i], end = ' ')

# 이 문제는 자기 자신보다 작은 서로 다른 수의 개수를 뽑는 것인데
# 이는 중복을 제거하고 만든 리스트를 정렬하여, 각 수의 인덱스를 출력하면 되는 것이다!