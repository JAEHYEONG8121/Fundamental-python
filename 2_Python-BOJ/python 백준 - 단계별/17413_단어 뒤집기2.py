import sys
s = list(sys.stdin.readline().rstrip())

i = 0
idx = 0

while i < len(s):
    if s[i] == "<":       
        i += 1 
        while s[i] != ">":    # 닫힌 괄호를 만날 때까지 i증가 시킨후 
            i += 1          
        i += 1                # 닫힌 괄호 만나면 i 1증가 
    elif s[i].isalnum():      # 알파벳이거나 숫자면 -> 시작인덱스는 i
        idx = i
        while i < len(s) and s[i].isalnum(): 
            i+=1
        tmp = s[idx:i]
        tmp.reverse()       
        s[idx:i] = tmp
    else:                   
        i+=1              
print("".join(s))