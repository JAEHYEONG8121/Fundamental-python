# 변수는 특정 지역에서만 사용되는 지역변수와 지역에 상관없이 전 지역에서 사용되는 전역변수로 분류된다
# 변수가 사용되는 범위를 스코프라고 한다
# 함수 내부에서 전역 변수를 사용하기 위한 명령문 형식 : global 전역변수

# 지역변수 예
x = 50 # 전역변수
def local_func(x) :
    x += 50

local_func(x)
print('x=', x)

# 전역변수 예
def global_func() :
    global x
    x += 50

global_func()
print('x=', x)