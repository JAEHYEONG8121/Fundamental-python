i, sum = 0, 0
num = 0

num = int(input('값 입력: '))
for i in range(num + 1) :
    print(i)
    sum += i
print('0에서 %d까지의 합: %d' % (num, sum))
