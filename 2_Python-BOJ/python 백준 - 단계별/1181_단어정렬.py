l = []
for i in range(int(input())) :
    s = input()
    l.append(s)
s = set(l)
l = list(s) # 리스트 중복제거
l.sort()    # 알파벳 순으로
l.sort(key=len) # key값을 이용하여 길이를 기준으로 정렬
for i in l :
    print(i)