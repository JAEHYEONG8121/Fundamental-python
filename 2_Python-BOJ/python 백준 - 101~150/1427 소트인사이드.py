N = list(input())
N.sort()
n = N[::-1]
for i in n :
    print(i, end='')

# 리스트 정렬 -> .sort() / 거꾸로 뒤집기 -> .reverse()
'''
n=list(input())
n.sort()
n.reverse()
for i in n:
	print(i,end='')
'''