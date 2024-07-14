M = int(input())
N = int(input())
sum, min = 0, N * N
for i in range(1, N) :
    if (M <= i * i and i * i <= N) :
        sum += i * i
        if i * i < min :
            min = i * i

if sum == 0 :
    print(-1)
else :
    print(sum)
    print(min)

    


