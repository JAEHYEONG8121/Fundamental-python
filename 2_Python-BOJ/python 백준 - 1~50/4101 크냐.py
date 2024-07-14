while True :
	A, B = map(int, input().split())
	if A > B :
		if A == 0 or B == 0 :
			break
		else :
			print('Yes')
	elif A <= B :
		if A == 0 or B == 0 :
			break
		else :
			print('No')
		