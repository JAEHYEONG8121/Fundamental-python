'''
import sys

T = int(input())
mi = 0
for i in range(T) :
	lst = []
	A, B = map(int, sys.stdin.readline().split())
	for j in range(1, (A * B) + 1) :
		if j % A == 0 and j % B == 0 :
			lst.append(j)
			break
	s = set(lst)
	lst = list(s)
	mi = min(lst)
	print(int(mi))
'''
# 최소공배수 = 두 수의 곱 / 최대 공약수
# ==최대공약수 구하는법==
# 2개의 자연수  a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면 (단 a>b), 
# a와 b의 최대공약수는 b와 r의 최대공약수와 같다. 
# 이 성질에 따라, b를 r로 나눈 나머지 r0를 구하고, 
# 다시 r을 r0로 나눈 나머지를 구하는 과정을 반복하여 
# 나머지가 0이 되었을 때 나누는 수가 a와 b의 최대공약수이다
num = int(input())
for i in range(num):
    a,b = map(int,input().split())
    A,B = a,b
    while a!=0:
        b = b%a
        a,b = b,a   
        # print(a,b)
    lcm = A * B // b
    print(lcm)
    
		

	

	
