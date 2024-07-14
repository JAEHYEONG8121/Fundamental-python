ls = [0, 0, 0, 0]
sum, i = 0, 0

while i < len(ls) :
    ls[i] = int(input(str(i) + '째 숫자입력: '))
    sum += ls[i]
    i += 1
else :
    i = 0

while i < len(ls) :
    print('ls[%d]: %d' % (i, ls[i]))
    i += 1
print('sum=', sum)
    