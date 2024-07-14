def inputNum() :
    x = int(input('첫 번째 수를 입력하세요: '))
    y = int(input('두 번째 수를 입력하세요: '))
    return x, y
def swapVal(x, y) :
    x, y = y, x
    return x, y
def twoNumSum(x, y) :
    if  x > y :
        x, y = swapVal(x, y)
    sum = 0
    for i in range(x, y+1) :
        sum += i
    return sum

n1, n2 = inputNum()
print('%d부터 %d까지의 합 : %d' % (n1, n2, twoNumSum(n1, n2)))


