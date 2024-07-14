def func1() :
    global a 
    a = 1222
    print('func1의 a: %d' % a)

def func2() :
    print('func2의 a: %d' % a)

a = 200
func1()
func2()