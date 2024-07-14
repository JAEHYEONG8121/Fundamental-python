num, result, i = 0, 0, 1
while True :
    num = int(input('1~10 사이의 숫자 입력: '))
    if num < 1 or num > 10 :
        print('잘못 입력 다시')
        continue
    else :
        break
else :
    print('next...')
while i <= num :
    result += i
    i += 1
else :
    print('1~', num, '까지의 합:', result)