def alba(day = 30, time = 8, won = 8500) :
    result = day * time * 8500
    return result

def display() :
    num = int(input('1.기본금\n2.일한 날짜 입력\n'))
    if num == 1:
        result = alba()
    elif num == 2 :
        day = int(input('일한 날짜 입력(몇일): '))
        result = alba(day)
    print('당신의 급여:{}원 입니다'.format(result))

display()