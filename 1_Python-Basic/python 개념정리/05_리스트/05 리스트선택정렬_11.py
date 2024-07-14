ls = [4, 8, 2, 6, 7]
i, j = 0, 0

for i in range(4) :
    for j in range(i + 1, 5) :
        if ls[i] > ls[j] :
            ls[i], ls[j] = ls[j], ls[i]

print(ls)
        