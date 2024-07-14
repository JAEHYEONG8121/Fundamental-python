import sys
sum = 0
N = int(sys.stdin.readline())
for i in range(N) :
    n = int(sys.stdin.readline())
    if i == N-1 :
        sum += n
    else :
        sum += n-1
print(sum)
