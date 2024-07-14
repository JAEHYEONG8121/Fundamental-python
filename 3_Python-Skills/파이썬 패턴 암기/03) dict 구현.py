keyList = ['key1', 'key2', 'key3']
valList = [10, 20, 30]

# zip()함수 이용
dic = dict(zip(keyList, valList))
print(dic)
 
# tuple 형변환
tupleList = [('key1', 10), ('key2', 20), ('key3', 30)]
dic = dict(tupleList)
print(dic)