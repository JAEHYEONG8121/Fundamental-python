list = [30, 20, 10]
print('현재 리스트: %s' % list)

list.append(40)
print('append(40)후의 리스트 : %s' % list)

print('pop() 으로 추출한 값: %s' % list.pop())
print('pop() 후의 리스트: %s' % list)

list.sort()
print('sort() 후의 리스트 : %s' % list)

list.reverse()
print('reverse() 후의 리스트: %s' % list)

del(list[2])
print('del() 후의 리스트 : %s' % list)