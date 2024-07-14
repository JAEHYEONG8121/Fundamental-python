x = 10
y = 20
def swapVal(x, y) :
    print('2 :', id(x), id(y), x, y)
    x, y = y, x
    print('3 :', id(x), id(y), x, y)

print('1 :', id(x), id(y), x, y)
swapVal(x, y)
print('4 :', id(x), id(y), x, y)