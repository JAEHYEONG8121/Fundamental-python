lst = []
a, b = input().split()
if len(a) >  len(b) :
    b = '0'*(len(a)-len(b)) + b
elif len(b) > len(a) :
    a = '0'*(len(b)- len(a)) + a
    
for i in range(len(a)) :
    lst.append(int(a[i])+int(b[i]))
for i in lst :  
    print(i, end = '')



    
