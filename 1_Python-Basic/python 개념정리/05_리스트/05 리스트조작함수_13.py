ls= []

for i in range(0, 4) :
    ls.append(0)
sum = 0

for i in range(0, len(ls)) :
    ls[i] = int(input(str(i+1) + '번 째 숫자 : '))
    sum += ls[i]
