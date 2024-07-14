T = int(input())
for _ in range(T) :
	a, *b = input().split()
	a = float(a)
	for i in range(len(b)) :
		if b[i] == '@' :
				a *= 3
		elif b[i] == '%' :
				a += 5
		elif b[i] == '#' :
				a -= 7
	print(format(a, '.2f')) # 소수점 둘째 짜리까지 표현하는 formating 암기하자!


    			

