N = int(input())
list = map(int, input().split())
sum = 0
for i in list :
    if i == N :
        sum += 1
print(sum)