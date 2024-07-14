# builtins 함수
dataset = list(range(1, 6))
print('len=', len(dataset))
print('sum=', sum(dataset))
print('max=', max(dataset))
pprint('min=', min(dataset))

# import 함수
import statistics # 방법1
print('평균=', statistics.mean(dataset))
print('중위수=', statistics.median(dataset))

from statistics import variance, stdev # 방법2
print('표본 분산=', variance(dataset))
print('표본 표준편차=', stdev(dataset))
