V = int(input())
a = list(input())
if len(a) == V :
  if a.count('A') > a.count('B') :
      print('A')
  elif a.count('A') == a.count('B') :
      print('Tie')
  else :
      print('B')