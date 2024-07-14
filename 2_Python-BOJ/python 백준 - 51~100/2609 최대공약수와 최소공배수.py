a, b = map(int, input().split())
A, B = a, b
while b != 0 :
    a = a%b
    a,b = b,a
print(a)
print(int(A * B / a))

'''
import math
A, B = map(int, input().split())
print(math.gcd(A, B))
print(math.lcm(A, B))

'''

