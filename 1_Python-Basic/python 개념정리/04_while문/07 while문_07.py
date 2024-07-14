i = 0
while i < 5 :
    i += 1
    if i == 3 :
        continue  # continue 문은 제어를 조건식으로 이동하게 한다. -> i < 5로 넘어간다!
        print('3---출력')
    print(i, '출력')
print('다음 문장')