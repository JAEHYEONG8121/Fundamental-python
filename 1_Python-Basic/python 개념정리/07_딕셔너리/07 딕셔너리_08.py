name = {'이순신' : '거북선', '세종대왕' : '훈민정음', '파이썬' : '프로그래밍 언어'}
for key, value in name.items() :
    print(key, ':', value)

print('삭제:', name.clear())
print('삭제 후 값:', name)