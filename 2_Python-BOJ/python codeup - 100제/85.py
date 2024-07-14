w, h, b = map(int, input().split())
print(format(((w*h*b)/8)/1024 ** 2, ".2f"), 'MB')