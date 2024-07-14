import math

N = int(input())

count = 0                                    
l = []

for _ in range(N):
    a, b = map(int, input().split())
    distance = b - a                         

    n = math.floor(math.sqrt(distance))  
    n2 = n**2                

    if distance == n2:
        count = (n*2)-1

    elif n2 < distance <= n2 + n:
        count = (n*2)

    elif (n2 + n) < distance:
        count = (n*2) + 1

    elif distance < 4:
        count = distance
    l.append(count)

for i in l:
    print(i)