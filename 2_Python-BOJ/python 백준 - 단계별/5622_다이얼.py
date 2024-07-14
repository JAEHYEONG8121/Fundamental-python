s = input()
t = 0
for i in s:
    if ('A'<= i < 'D') : t += 3
    elif ('D' <= i < 'G') : t += 4
    elif ('G' <= i < 'J') : t += 5
    elif ('J' <= i < 'M') : t += 6
    elif ('M' <= i < 'P') : t += 7
    elif ('P' <= i < 'T') : t += 8
    elif ('T' <= i < 'W') : t += 9
    elif ('W' <= i <= 'Z') : t += 10

print(t)