#word = input()
#if word[:int(len(word)/2)] == word[-1:-(int(len(word) / 2) + 1):-1] :
#    print(1)
#else :
#    print(0)

w = input()
if w[:] == w[::-1] :
    print(1)
else :
    print(0)