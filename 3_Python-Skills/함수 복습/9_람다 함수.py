# 람다 함수는 정의와 호출을 한 번에 하는 익명함수이다
# lambda 매개변수 : 실행문(반환값)

# 일반 함수
def Adder(x, y) :
    add = x + y
    return add
print('add =', Adder(10, 20))

# 람다 함수
print('add =', (lambda x, y : x + y) (10, 20))