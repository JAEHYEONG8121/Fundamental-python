import math

def isPrime(num):
    if num == 1: 
        return False

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0: 
            return False
    return True


li = list(range(2,246912))
l = []
for i in li:
    if isPrime(i):
        l.append(i)

while(1):
    answer = 0
    n = int(input())
    if n == 0: break

    for i in l:
        if n < i <= n*2:
            answer += 1

    print(answer)