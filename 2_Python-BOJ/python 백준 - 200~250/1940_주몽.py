n = int(input())
m = int(input())
cnt = 0
lst = []
l = list(map(int, input().split()))
l.sort()
for i in range(len(l)-1) :
    for j in range(i+1, len(l)) :
        if l[i] + l[j] == m :
            lst.append(l[i])
            lst.append(l[j])
            cnt += 1
s = set(lst)
l2 = list(s)
if (len(lst) == len(l2)) :
    print(len(lst)//2)
else :
    


