# Counter를 import해서 most_common()메서드를 통해서 리스트에 튜플 형식으로
# 빈도값이 높은 알파벳 순으로 정리가 된다
# 리스트 안의 튜플 인덱싱 -> 0 - 0
# 어차피 대문자로 출력해야됨
# 근데 순전히 알파벳의 수이므로 z이든 Z이든 zZ이면 알파벳 Z가 2번 쓰인 것이다
# 그냥 s에다가 zZ라고 쓰면 l = [('z', 1), ('Z', 1)]로 l이 생성된다
# 그런데 만약 zZbb라고 하면 z 2번, b 2번이므로 물음표가 출력되어야 한다
# 근데 zZ로 입력하면 소문자와 대문자로 따로 구분되므로 
# 애초에 입력한 s를 upper()메서드로 모두 대문자로 만들어줘서 Counter에다가 대입하면 된다!
from collections import Counter
s = input()
l = Counter(s.upper()).most_common()
if len(l) == 1 :
    print(l[0][0])
elif l[0][1] == l[1][1] :
    print('?')
else :
    print(l[0][0])


