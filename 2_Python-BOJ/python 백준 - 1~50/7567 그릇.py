h = 10
p = list(input())
for i in range(0, len(p)-1) :
    if p[i] == '(' and p[i+1] == '(' :
        h += 5
    elif p[i] == ')' and p[i+1] == '(' :
        h += 10
    elif p[i] == '(' and p[i+1] == ')' :
        h += 10
    elif p[i] == ')' and p[i+1] == ')' :
        h += 5
print(h)


