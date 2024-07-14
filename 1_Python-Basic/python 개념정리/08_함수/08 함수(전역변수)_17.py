num = 10
sum = 0
def display() :
    sumFunc()
    print('10까지의 합:', sum)
    
def sumFunc() :
    global sum 
    for i in range(num + 1) :
        sum += i
        
display()