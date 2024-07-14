T = int(input())
for _ in range(T) :
    N = int(input())
    n_lst = []
    s_lst = []
    for i in range(N) :
        name, s = input().split()
        n_lst.append(name)
        s = int(s)
        s_lst.append(s)
        if i != N-1 :
            pass
        elif i == N-1 :
            for j in range(len(s_lst)) :
                num = 0
                if s_lst[j] == max(s_lst) :
                    num = j
                    print(n_lst[num])

'''
T = int(input())
for _ in range(T) :
    N = int(input())
    n_lst = []
    s_lst = []
    for i in range(N) :
        name, s = input().split()
        s = int(s)
        n_lst.append(name)
        s_lst.append(s)
    
    print(n_lst[s_lst.index(max(s_lst))]) -> .index() 함수로 리스트, 배열에서 값의 위치를 찾아주는 함수
                                          -> 즉, 숫자리스트 s_lst에서 숫자가 최대가 되는 곳의 인덱스를 찾아서 
                                          -> 대학교의 이름이 저장되어 있는 n_lst의 인덱스에다가 집어넣은 것이다!
        
'''

'''
T = int(input())
for i in range(T):
    N = int(input())
    a = ""
    b = -1
    for j in range(N):
        c, d = input().split()
        d = int(d)
        if d > b:
            a = c
            b = d
    print(a)

빈 문자열 변수 a설정, b라는 -1 정수값을 갖는 변수 설정
c로 학교이름, d로 숫자를 받는다
들어온 숫자 d가 b보다 크다면 원래 빈 문자열 변수 a에다가 들어온 학교이름 저장, 원래 -1이었던 변수 b에다가 들어온 숫자 저장
'''
        


    
