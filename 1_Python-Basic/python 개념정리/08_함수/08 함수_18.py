def sum_func(x1, x2, x3 = 100) :
    result = 0
    result = x1 + x2 + x3
    return result

def display() :
    Sum = 0
    a,b,c = 10, 20, 30
    Sum = sum_func(a, b)
    print('매개변수 2개 함수 호출:', Sum)
    Sum = sum_func(a, b, c)
    print('매개변수 3개 함수 호출:', Sum)

display()