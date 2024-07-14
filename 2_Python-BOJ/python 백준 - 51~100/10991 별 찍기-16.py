# 이중for문을 잘 돌리면서 생각하기!
N = int(input())

for i in range(1, N+1):
    print(' '* (N-i), end = '')
    for j in range(i): 
        print('*', end = ' ')
    print()
            
