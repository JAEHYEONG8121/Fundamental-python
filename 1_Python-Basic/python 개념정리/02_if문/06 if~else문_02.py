arr = [1, 2, 3, 4, 5]
na = int(input('찾을 숫자 입력: '))
if na in arr :
    print('arr:', arr, '찾는 숫자가 존재 합니다:', na)
else :
    print('arr:', arr, '안에는 찾고자 하는 숫자가 없습니다:', na)
print('결과:', na in arr)