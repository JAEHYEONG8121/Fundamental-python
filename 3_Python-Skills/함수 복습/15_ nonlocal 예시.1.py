def mainFunc(arg) :
    memVal = arg
    def showData(arg) :
        nonlocal memVal
        memVal = arg
        print(memVal)
    return showData

show = mainFunc(10)
show(5)
show(100)

