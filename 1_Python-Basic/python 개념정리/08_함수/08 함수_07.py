def calc(su1, op, su2) :
    result = 0
    
    result = su1 + su2
    print(su1, '+', su2, '=', result)
    
su1, op, su2 = int(input('숫자: ')), input('부호: '), int(input('숫자: '))
calc(su1, op, su2)