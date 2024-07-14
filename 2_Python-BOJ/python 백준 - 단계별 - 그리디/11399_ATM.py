n = int(input())
lst = []
l = list(map(int, input().split()))
l.sort()
sum1 = 0
sum2 = 0
for i in l :
    sum1 += i
    sum2 += sum1
print(sum2)
