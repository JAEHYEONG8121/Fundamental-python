result, temp = 0, 0
result = int(input('수 입력: '))
while True :
    temp = int(result % 10)
    result = int(result / 10)
    print(temp, end = '')
    if not result :
        break
print('\n프로그램 종료')