N = int(input())
sum = 1
if N == 0 :
    pass
else :
    for i in range(1, N+1) :
        sum *= i
print(sum)