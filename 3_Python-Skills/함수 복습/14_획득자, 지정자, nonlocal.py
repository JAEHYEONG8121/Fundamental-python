def main_func(num) :
    num_val = num
    def getter() :
        return num_val
    def setter(value) :
        nonlocal num_val
        num_val = value
    
    return getter, setter # 내부함수 getter와 setter는 일급함수로서의 역할을 한다!

getter, setter = main_func(100) # main_func()에서 내부함수 g와 s를 반환하여 이를 main에서 사용가능!

print('num=', getter()) # main_func(num)의 num에다가 100을 넣어줌 -> num_val = 100이 된다
                        # getter()는 그 num_val을 반환해주므로 num = 100이 출력됨

setter(200) # setter(value)의 value에다가 200을 넣어줌 -> nonlocal num_val이므로 num_val = 200이 된다
            # getter()는 그 num_val을 반환해주므로 num = 200이 출력됨
print('num=', getter())

# 즉, nonlocal은 내부함수 자기자신의 지역변수가 아니다! 외부함수의 변수를 사용하는 것이다!