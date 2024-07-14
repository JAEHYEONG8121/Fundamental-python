l = []
lst = []
for _ in range(int(input())) :
    s = input()
    l.append(s[0])

for i in l :
    if l.count(i) >= 5 :
        lst.append(i)
    else :
        pass
s_ = set(lst)
lst = list(s_)
lst.sort()
if len(lst) == 0 :
    print('PREDAJA')
else :
    for i in lst :
        print(i, end='')


