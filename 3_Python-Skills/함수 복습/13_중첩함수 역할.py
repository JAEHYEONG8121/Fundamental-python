# 외부함수 : 함수에서 사용할 자료를 만들고, 내부 함수를 포함하는 역할을 한다
# 내부함수 : 외부 함수에서 만든 자료를 연산하고 조작하는 역할을 한다
# 다음은 외부 함수에서 데이터 셋을 만들고, 내부 함수에서 데이터 셋의 분산과 표준편차를 구하는 예문이다
from statistics import mean
from math import sqrt

data = [4, 5, 3.5, 2.5, 6.3, 5.5]

# 외부 함수
def scattering_func(data) :
    dataSet = data # data는 메인에서 설정된 것이므로 scattering 함수 안에서 dataSet으로 따로 설정해주어 접근한다!
    
    def avgFunc() :
        avgVal = mean(dataSet)
        return avgVal
    def varFunc(avg) :
        diff = [(data - avg)**2 for data in dataSet]
        varVal = sum(diff) / (len(dataSet) - 1)
        return varVal
    def stdFunc(var) :
        stdVal = sqrt(var)
        return stdVal
    return avgFunc, varFunc, stdFunc # 외부 함수내의 3개의 내부함수를 반환!

avg, var, std = scattering_func(data)
print('평균=', avg())
print('분산=', var(avg()))
print('표준편차=', std(var(avg())))