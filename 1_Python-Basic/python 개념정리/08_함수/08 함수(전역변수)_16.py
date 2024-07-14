def display() :
    print('10까지의 합: ', sum(num))

def sum(num) :
    sum = 0
    for i in range(num + 1) :
        sum += i
    return sum
num = 10
display()