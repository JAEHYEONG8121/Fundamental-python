sum = 0
s = 0
for i in range(1, int(input())+1) :
    s += i
    if i == 1 :
        sum = 3
    else :
        sum += 3 * s
print(sum)


