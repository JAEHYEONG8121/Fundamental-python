s = input()
l = ['a', 'e', 'i', 'o', 'u']
cnt = 0
for i in l :
    cnt += s.count(i)
print(cnt)