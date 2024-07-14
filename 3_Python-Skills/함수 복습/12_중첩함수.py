# 중첩함수는 함수 내부에 또 다른 함수가 내장된 형태를 의미한다
# 파이썬의 중첩함수는 외부함수나 내부함수를 '변수'에 저장할 수 있다! -> 이러한 함수를 일급함수라고 한다
# 특히 내부함수는 외부함수의 return 명령문을 이용하여 반환하는 형태를 '함수 클로저'라고 한다

# 일급 함수
def a() :
    print('a 함수')
    def b() :
        print('b 함수')
    return b
b = a()
b()
# 함수 a()를 호출하면 내부함수 b()가 반환된다
# 이렇게 반환된 함수를 변수 b에 저장한다
# 즉 함수를 객체로 만들어서 사용하는 것을 일급함수라고 한다

# 함수 클로저
data = list(range(1, 101))
def outer_func(data) :
    dataSet = data
    def tot() :
        tot_val = sum(dataSet)
        return tot_val
    def avg() :
        avg_val = tot_val / len(dataSet)
        return avg_val
    return tot, avg

tot, avg = outer_func(data) # 외부함수에 의해서 반환된 tot, avg함수는 외부함수가 종료되어도 객체로 만들어지기 때문에
                            # 합계와 평균을 계산하는데 이용할 수 있다
tot_val = tot()
print('tot=', tot_val)
avg_val = avg()
print('avg=', avg_val)