x = 10
y = 20

def swapVal() :
    global x, y
    x, y = y, x

print(x, y)
swapVal()
print(x, y)