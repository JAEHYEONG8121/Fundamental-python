def isPrime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for i in range(int(input())) :
    n = int(input())
    a = n // 2
    b = a
    for j in range(10000) :
        if isPrime(a) and isPrime(b):
                print(a, b)
                break
        else :
            a -= 1
            b += 1

    
# 입력받은 수를 반으로 나누고 a와 b의 값을 점점 멀어지게 하면서 가장 가까운 쌍을 찾는 생각!
# isPrime()함수 이용!

