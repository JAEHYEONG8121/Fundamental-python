list = [30, 20, 10]
print('현재 리스트: %s' % list)
print('10 값의 위치 : %d' % list.index(10))

list.insert(2, 200)
print('insert(2, 200) 후의 리스트: %s' % list)

list.remove(200)
print('remove(200) 후의 리스트: %s' % list)

list.extend([555, 666, 555])
print('extend([555, 666, 555]) 후의 리스트: %s' % list)
print('555값의 개수: %d' % list.count(555))