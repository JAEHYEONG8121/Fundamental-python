import math
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
width = 0
height = 0
if x1 == x2 :
	width = abs(x3 - x2)
	height = abs(y1 - y2)
	if y1 == y3 :
		print('%d %d' % (x3, y2))
	elif y2 == y3 :
		print('%d %d' % (x3, y1))	
			
elif x2 == x3 :
	width = abs(x1 - x2)
	height = abs(y2 - y3)
	if y2 == y1 :
		print('%d %d' % (x1, y3))
	elif y3 == y1 :
		print('%d %d' % (x1, y2))

elif x3 == x1 :
	width = abs(x3 - x2)
	height = abs(x3 - x1)
	if y3 == y2 :
		print('%d %d' % (x2, y1))
	elif y1 == y2 :
		print('%d %d' % (x2, y3))





