lst1 = input().split()
lst1.sort()
s = set(lst1)
lst2 = list(s)
lst2.sort()
print(lst2)

if len(lst2) == 3 :
    	print(int(lst2[2]) * 100)
elif len(lst2) == 2 :
		if lst1[0] == lst1[1] :
				print(1000 + int(lst1[0]) * 100)
		elif lst1[1] == lst1[2] :
				print(1000 + int(lst1[1]) * 100)
		elif lst1[2] == lst1[0] :
				print(1000 + int(lst1[2]) * 100)
elif len(lst2) == 1 :
    	print(10000 + int(lst2[0]) * 1000)



    	



		