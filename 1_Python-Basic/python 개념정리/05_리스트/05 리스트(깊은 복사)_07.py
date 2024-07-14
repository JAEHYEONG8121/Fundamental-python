ls = [10, 20, 30, 40]
arr = ls[:]
arr[2] = 20000

print('ls:', ls, 'ls(id):', id(ls))
print('arr:', arr, 'arr(id):', id(arr))
