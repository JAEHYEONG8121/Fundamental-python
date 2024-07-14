n = int(input())
l = list(map(int, input().split()))
def isPrime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
cnt = 0
for i in l:
    if isPrime(i):
        cnt += 1
print(cnt)
'''
n = int(input())
l = map(int, input().split())
result = 0
for i in l:
    cnt = 0
    if i > 1 :
        for j in range(2, i):  # 2부터 n-1까지
            if i % j == 0:
                cnt += 1  # 2부터 n-1까지 나눈 몫이 0이면 error가 증가
        if cnt == 0:
            result += 1  # error가 없으면 소수.
print(result)
'''








