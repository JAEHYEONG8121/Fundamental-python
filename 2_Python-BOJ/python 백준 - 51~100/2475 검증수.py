lst = list(map(int,input().split()))
li = []
for i in lst :
    li.append(i ** 2)
print(sum(li) % 10)

'''
a = input()
b = 0
for i in range(0, len(a), 2) :
    b += int(a[i])**2
c = b % 10
print(c)

'''