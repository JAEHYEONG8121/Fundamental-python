i = 1
odd, even = 0, 0
while i <= 10 :
    if i % 2 == 0 :
        even += i
    else :
        odd += i
    i += 1
print('1-10 짝수의 합:', even)
print('1-10 홀수의 합:', odd)

    