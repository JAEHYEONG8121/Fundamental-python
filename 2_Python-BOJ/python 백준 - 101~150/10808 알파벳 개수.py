# 아스키 값을 반환하는 ord()함수를 이용하여 for문의 range를 설정할 수 있다!
# 또한, 이때 아스키 값을 i가 받으므로 chr(i)로 해주면 그 아스키 값에 맞는 알파벳을 알 수 있다!
s = input()
for i in range(ord('a'), ord('z') + 1) :
    print(s.count(chr(i)), end = ' ')