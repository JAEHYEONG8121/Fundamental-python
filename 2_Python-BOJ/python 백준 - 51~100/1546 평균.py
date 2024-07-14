lst = []
N = int(input())
list = list(map(int, input().split()))
for i in list :
    k = (i / max(list)) * 100
    lst.append(k)
print('%.10f' % (sum(lst) / len(lst)))