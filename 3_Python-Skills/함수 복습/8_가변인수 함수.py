# 일반적인 함수에서는 하나의 매개변수를 이용하여 하나의 실인수를 받도록 되어있다.
# 가변인수 함수 -> 하나의 매개변수로 여러 개의 실인수를 받을 수 있는 가변인수를 제공
# 여러 개의 실인수를 하나의 매개변수로 받을 때 '*매개변수' 형식은 튜플(tuple) 자료구조로 받고
# '**매개변수' 형식은 딕트(dict) 자료구조로 받는다

# 튜플형 가변인수
def Func1(name, *names) :
    print(name)
    print(names)

Func1('홍길동', '이순신', '유관순')

# statistics 모듈 import
from statistics import mean, variance, stdev

def statis(func, *data) :
    if func == 'avg' :
        return mean(data)
    elif func == 'var' :
        return variance(data)
    elif func == 'std' :
        return stdev(data)
    else :
        return 'TypeError'

print('avg =', statis('avg', 1, 2, 3, 4, 5))
print('var =', statis('var', 1, 2, 3, 4, 5))
print('std =', statis('std', 1, 2, 3, 4, 5))

# 딕트형 가변인수
def emp_func(name, age, **other) :
    print(name)
    print(age)
    print(other)

emp_func('홍길동', 35, addr = '서울시', height = 175, weight = 65)
