ls= [10, 20, 30]
ls.append(100)

for i in range(0, 4) :
    print('ls[%d]: %d' % (i, ls[i]))
print('리스트의 총 개수:', len(ls))
print('ls:', ls)
ls = []
print('ls초기화 후:',ls)