naturalNum = set(range(1, 10001))
generatedNum = set()

for i in range(1, 10001) :
    for j in str(i) : # 수를 문자열로 변경한다 -> 만약 i가 850이면 -> '8', '5', '0'을 쪼개서 정수로 변환하여 원래 850인 i에다가 더해주는 것이다!
        i += int(j)
    generatedNum.add(i) # 이렇게 해서 generatedNum에는 생성자로 생성된 숫자들만 담기게 된다!

selfNum = sorted(naturalNum - generatedNum) # 기본 숫자에서 생성자로 생성된 숫자들을 빼주면 셀프 넘버만 남는다!
for i in selfNum :
    print(i)