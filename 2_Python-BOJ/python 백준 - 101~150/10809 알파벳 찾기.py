s = input()
for i in range(ord('a'), ord('z') + 1) :
    if s.count(chr(i)) == 0 :
        print(-1, end =' ')
    elif s.count(chr(i)) >= 1:
        print(s.index(chr(i)), end = ' ')

'''
<파이썬 문자열 find()함수>
- string.find(찾을 문자, 시작 index, 끝 index)
- 찾는 문자가 존재한다면 해당 위치의 index를 반환
- 찾는 문자가 존재하지 않는다면 -1을 반환

s = input()
alpha = list(range(97, 123))

for i in alpha :
    print(s.find(chr(i)), end = ' ')
'''
