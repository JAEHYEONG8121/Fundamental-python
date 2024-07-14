'''for i in range(0, 3, 1) :
    for k in range(0, 2, 1) :
        print('이중 for문 (i: %d\tk: %d)'% (i, k))
'''

i, k = 0, 0
while i < 3 :
    while k < 3 :
        print('i: %d\tk: %d' % (i, k))
        k += 1
    else :
        k = 0
    i += 1
    continue
print()
print()
