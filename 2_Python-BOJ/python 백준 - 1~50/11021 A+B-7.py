result = []
T = int(input())
for i in range(T) :
    A, B = map(int, input().split())
    result.append(A + B)

for i in range(1, len(result) + 1) :
    print('Case #%d: %d'%(i, result[i-1]))

