def change(a, b, c) :
    return a + 10, b + 20, c + 30

a, b, c = change(10, 20, 30)
d = change(10, 20, 30)
print('a,b,c:', a,b,c)
print('d:{}, type{}'.format(d, type(d)))

