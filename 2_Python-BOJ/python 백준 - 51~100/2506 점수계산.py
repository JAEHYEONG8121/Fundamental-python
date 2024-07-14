N = int(input())
list = input().split()
sum = 0
score = 0
for i in list :
    if i == '1' :
        score += 1
        sum += score
    elif i == '0' :
        score = 0
print(sum)
