lst = []
N = int(input())
for i in range(N) :
    a = int(input())
    lst.append(a)
if lst.count(1) > lst.count(0) :
    print("Junhee is cute!")
else :
    print("Junhee is not cute!")
