a, b, v = map(int, input().split())
day = (v - b) / (a - b)
print(int(day) if day == int(day) else int(day)+1) # 범위가 10억이므로 무한루프 while문을 돌리면 시간초과가 난다!
                                                   # 원래 a * day - b * (day - 1) >= v 이 조건을 만족하는 day를 출력하면 되는데 
                                                   # while문에 이 조건으로 넣으면 시간초과가 난다 -> 이항을 하여 day에 대한 식으로 변환해준다!
                                                   # day = (v - b) / ( a- b)이므로 수 3개가 들어왔을 때 바로 day를 연산을 통해서 구해주는 것이다!
                                                   # 이렇게 하면 시간초과가 발생하지 않는다!
                                                   # 마지막에 출력할 때 삼항 연산자를 사용하여, day의 값이 분수가 나올 수 있을 때를 방지해주는 것이다!