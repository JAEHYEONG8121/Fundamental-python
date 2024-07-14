import sys
from collections import Counter
l = []
for i in range(int(sys.stdin.readline())) :
    l.append(int(sys.stdin.readline()))

# 산술평균
avg = round(sum(l) / len(l))
print(avg)

# 중앙값
l.sort()
print(l[int((len(l)-1)/2)])

# 최빈값 -> collection 모듈의 Counter사용!!!
if len(l) == 1:
    most = l[0]
    print(most)
else :
    cnt = Counter(l)
    most = cnt.most_common(2)
    if most[0][1] == most[1][1] :
        print(most[1][0])
    else :
        print(most[0][0])

# 범위
print(l[-1] - l[0])

