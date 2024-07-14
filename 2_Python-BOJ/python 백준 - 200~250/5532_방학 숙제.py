l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
n, m = 0, 0
if a % c == 0 :
    n = a // c
else :
    n = a // c + 1
if b % d == 0 :
    m = b // d
else :
    m = b // d + 1
if n > m :
    print(l - n)
else :
    print(l - m)


