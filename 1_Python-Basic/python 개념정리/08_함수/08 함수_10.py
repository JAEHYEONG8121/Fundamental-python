def func2(a, b) :
    a += 5; b *= 10
    print('func2: a = {}, b = {}'.format(a, b))
def func1() :
    a = 5; b = 10
    func2(a, b)
    print('func1: a = {}, b = {}'.format(a, b))
func1()