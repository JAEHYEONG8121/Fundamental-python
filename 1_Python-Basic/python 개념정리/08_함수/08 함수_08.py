def calc(su1, op, su2) :
    result22 = 0
    result22 = su1 + su2
    print('cal 실행')
    return result22
    
su1, op, su2 = int(input('숫자: ')), input('부호: '), int(input('숫자: '))
result = calc(su1, op, su2)
print(su1, '+', su2, '=', result)
print('다음 문장 실행')