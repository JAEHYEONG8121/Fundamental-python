n = int(input())
cnt = 0
for i in range(1, n+1) :
    if i < 100 :      
        cnt += 1
    else :       
        s = str(i)    
        if int(s[0]) == int(s[1]) == int(s[2]) :
            cnt += 1
        else :
            if (int(s[0]) - int(s[1])) == (int(s[1]) - int(s[2])) :
                cnt += 1
            else :
                pass
print(cnt)
        
# 100보다 작은 수들은 모두 한수 조건에 만족한다!
# n의 범위가 1000까지 이므로 100보다 크거나 같으면 무조건 3자리 수이다! 이를 받아서 문자열로 변경하여 하나하나 쪼개준다!