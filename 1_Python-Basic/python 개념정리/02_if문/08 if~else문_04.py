old_id = input('저장할 ID 입력: ')
print('인증 프로그램 입니다')
print('ID와 PW를 입력하세요')
new_id = input('ID입력: ')
if old_id == new_id :
    print('인증 통과 했습니다')
else :
    print('인증 실패')