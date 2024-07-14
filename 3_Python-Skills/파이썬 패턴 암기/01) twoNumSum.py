n1 = int(input('첫 번째 숫자: '))
n2 = int(input('두 번째 숫자: '))
sum = 0
if n1 > n2 :
    n1, n2 = n2, n1
for i in range(n1, n2 + 1) :
    sum += i
print('%d부터 %d까지의 합: %d' % (n1, n2, sum))