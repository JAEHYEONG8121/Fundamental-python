n = int(input())
result = 0
for i in range(9) :
    m = int(input())
    result = n - m
    n -= m
print(result)
