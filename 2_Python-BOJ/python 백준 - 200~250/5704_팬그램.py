from collections import Counter

def pangram(s) :
    result = 'N'
    s = s.replace(' ', '')
    cnt = Counter(s)

    if len(cnt.keys()) == 26 :
        result = 'Y'
    
    return result

while True :
    s = input()
    if s == '*' :
        break
    
    print(pangram(s))

# 이 문제도 Counter를 이용한다
# 모든 알파벳을 다 사용했는지 확인했는지의 여부를 Counter를 통해서
# 각 알파벳이 몇 번 나왔는지 dict형태로 나올 것이다
# 그 때 key값은 알파벳이므로, dict의 key값들을 list에 담아주는
# dict.keys()함수를 사용하여, 그 list의 길이가 알파벳 소문자의 갯수 26이라면
# Y를 출력해주도록 함수를 만든 것이다!
