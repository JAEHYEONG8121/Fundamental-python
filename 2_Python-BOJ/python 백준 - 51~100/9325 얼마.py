T = int(input())
sum = 0
for i in range(T) :
    sum = 0
    s = int(input())
    sum += s
    n = int(input())
    for j in range(n) :
        q, p = map(int, input().split())
        sum += q * p
    print(sum)

# 옵션의 갯수 q와 가격 p를 동시에 a라는 변수로 받는다
# a는 리스트이므로 eval()함수를 이용해서 a리스트의 인덱스로 각각의 문자열을 추출하고
# 이 두개를 곱셈으로 표현해서 나타낸 것이다!
'''
t=int(input())
for i in range(t):
    s=int(input())
    n=int(input())
    for j in range(n):
        a=input().split()
        s+=eval(a[0]+'*'+a[1])
    print(s)
'''