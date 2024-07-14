l = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
for i in l:
    s = s.replace(i, '*')
print(s)
print(len(s))

# 문자열 replace함수 사용! -> 리스트안에 크로아티아 문자를 담아두고
# 입력받은 문자열에서 리스트에 담긴 문자를 '*'로 대체하여 문자열의 길이를 출력하는 아이디어!