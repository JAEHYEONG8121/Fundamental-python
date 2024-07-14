A, I = input().split()
A = int(A)
I = int(I)
for i in range(1, A * I + 1) :
	if i == A * (I-1) :
		print(i + 1)
		break


		