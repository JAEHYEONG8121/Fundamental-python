def myType(su) :
    if type(su) == int :
        return str(su) + '정수(int)형태입니다'
    elif type(su) == str :
        return su + '문자(str)형태입니다'
    else :
        return '어떤것인지 모르겠습니다'
n1 = input('수 입력: ')
n2 = int(input('수 입력: '))
n3 = float(input('수 입력: '))
print(myType(n1))
print(myType(n2))
print(myType(n3))
