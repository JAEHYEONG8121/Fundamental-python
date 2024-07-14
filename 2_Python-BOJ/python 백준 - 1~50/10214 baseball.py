y_result = 0
k_result = 0
T = int(input(''))
for i in range(T) :
    for j in range(9) :
        y, k = map(int, input().split())
        y_result += y
        k_result += k
    if y_result > k_result : print('Yonsei')
    elif y_result < k_result : print('Korea')
    else : print('Draw')



