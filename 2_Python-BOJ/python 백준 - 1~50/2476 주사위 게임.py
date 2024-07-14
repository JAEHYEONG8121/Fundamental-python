N = int(input())
lst = []
for i in range(N) :
	li = list(map(int, input().split()))
	li.sort()
	if li[0]==li[2]:
		lst.append(10000 + 1000*li[0])
	elif li[0]==li[1]:
		lst.append(1000 + 100*li[0])
	elif li[1]==li[2]:
		lst.append(1000 + 100*li[1]) 
	else:
		lst.append(100*li[2])
m = int(max(lst))
print(m)
