def sum_func(*par) :
    result = 0
    print('type:', type(par))
    print('par:', par)
    for num in par :
        result = result + num
        print('num: %d' % num)
    return result

Sum = 0
Sum = sum_func(10, 20)
print('매개변수 2개 함수: %d' % Sum)
Sum = sum_func(10, 20, 30, 40)
print('매개변수 4개 함수: %d' % Sum)