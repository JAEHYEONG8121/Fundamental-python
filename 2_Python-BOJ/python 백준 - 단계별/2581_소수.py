a = int(input())
b = int(input())
l = []
def isPrime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for i in range(a, b+1) :
    if isPrime(i) :
        l.append(i)
if len(l) == 0 :
    print(-1)
else :
    print(sum(l))
    print(min(l))


