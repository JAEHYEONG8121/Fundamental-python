a, b, c = map(int, input().split())
d = int(input())
a += d // 3600
b += (d % 3600) // 60
c += ((d % 3600) % 60) % 60
if c >= 60 :
    b += 1
    c -= 60
if b >= 60 :
    a += 1
    b -= 60
if a >= 24 :
    a -= 24
print(a%24, b, c)

'''
h,m,s = map(int, input().split())
ds = int(input())

s += ds

m += s // 60
s = s % 60

h += m // 60
m = m % 60

h = h % 24

print(h,m,s)
'''
