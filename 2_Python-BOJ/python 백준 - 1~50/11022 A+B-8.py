result = []
T = int(input())
for i in range(1, T + 1) :
    A, B = map(int, input().split())
    result.append(A + B)
    print('Case #%d: %d + %d = %d'%(i, A, B, result[i-1]))
