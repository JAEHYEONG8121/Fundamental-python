for _ in range(int(input())) :
    l = []
    n = int(input())
    s = str(n)
    for i in s :
        l.append(i)
    m = set(l)
    l2 = list(m)
    print(len(l2))

'''
t = int(input())

for _ in range(t) :
  x = input()
  data = []

  result = 0
  for i in range(len(x)) :
    if int(x[i]) not in data : 
      result += 1
      data.append(int(x[i]))

  print(result)
data라는 리스트에 입력된 숫자(=문자열)를 for문을 돌려 
숫자 하나씩 리스트에 저장하는데, not in data를 사용하여 data리스트에
숫자가 없을 경우만 result를 1증가시켜서 출력해준다!
'''