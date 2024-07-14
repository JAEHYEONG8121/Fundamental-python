a = 100
def outer():
    a = 50
    def inner() :
        nonlocal a
        a += 10
    inner()
    print(a)
outer()
print(a)