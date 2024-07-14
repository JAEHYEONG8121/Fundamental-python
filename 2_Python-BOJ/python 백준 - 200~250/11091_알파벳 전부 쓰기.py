for _ in range(int(input())) :
    s = input().lower()
    miss = ''
    
    for i in range(ord('a'), ord('z')+1) :
        if s.find(chr(i)) == -1 :
            miss += chr(i)
    
    if miss == '' :
        print('pangram')
    else :
        print(f'missing {miss}')

# 입력한 문자열을 모두 소문자로 변경 -> lower()함수 사용
# 입력한 문자열을 for문을 통해 알파벳 소문자 a부터 z까지의 범위 안에 있는지 확인
# 만약 어떤 알파벳이 없다면, find()함수로부터 얻은 값이 -1일테니
# -1이나오면 miss변수의 빈 문자열에다가 알파벳을 더해준다
# miss변수의 문자열이 비어있으면 빠진 알파벳이 없다는 뜻이므로 pangram출력
# 아니면 빠진 알파벳을 출력하면 된다!