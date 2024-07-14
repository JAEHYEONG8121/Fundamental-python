import math
l = []
lst = []
gcd = 0
for i in range(int(input())):
    l.append(int(input()))
    if i == 1:
        gcd = abs(s[1] - s[0])
    gcd = math.gcd(abs(s[i] - s[i - 1]), gcd)
gcd_a = int(gcd ** 0.5)
for i in range(2, gcd_a + 1):
    if gcd % i == 0:
        lst.append(i)
        lst.append(gcd // i)
lst.append(gcd)
lst = list(set(lst))
lst.sort()
for i in lst:
    print(i, end = ' ')