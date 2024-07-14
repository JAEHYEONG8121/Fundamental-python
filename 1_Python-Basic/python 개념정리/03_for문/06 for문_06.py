i, sum = 0, 0
start, en , grow = 0, 0, 0

start = int(input('시작값 입력: '))
en = int(input('끝값 입력: '))
grow = int(input('증가값 입력: '))

for i in range(start, en + 1, grow) :
    sum += i

print('%d에서 %d까지 %d씩 증가한 값의 합: %d' % (start, en, grow, sum))
