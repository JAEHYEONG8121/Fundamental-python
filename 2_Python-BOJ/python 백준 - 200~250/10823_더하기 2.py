import sys
s=""
while True:
    try:
        s+=input()
    except : break
print(sum(map(int, s.split(","))))
# 이 문제 예외처리하는게 왜하는건지 잘 모르겠다...