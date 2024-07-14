l = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
dict = {'black':1, 'brown':10, 'red':100, 'orange':1000,
            'yellow':10000, 'green':100000, 'blue':1000000,
            'violet':10000000, 'grey':100000000, 'white':1000000000}
sum = 0
for i in range(3) :
    s = input()
    if i == 0 :
        sum += l.index(s) * 10
    elif i == 1 :
        sum += l.index(s)
    else :
        sum *= dict[s]
print(sum)

'''
a={}
a['black']=0
a['brown']=1
a['red']=2
a['orange']=3
a['yellow']=4
a['green']=5
a['blue']=6
a['violet']=7
a['grey']=8
a['white']=9

B= input()
C= input()
D= input()

print( (10**a[D]) * (10*a[B]+a[C]))
'''


