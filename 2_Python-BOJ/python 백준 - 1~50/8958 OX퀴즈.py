T = int(input())
for _ in range(T) :
    score = 0
    o = 0
    s = input()
    for i in range(len(s)) :
        if s[i] == 'O' :
            o += 1
            score += o    
        elif s[i] == 'X' :
            o = 0
    print(score)

