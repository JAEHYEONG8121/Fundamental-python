n, k = map(int, input().split())
lst = []
cnt = 0
for _ in range(n) :
    lst.append(int(input()))

for i in reversed(range(n)) : # reversed를 이용하여 range범위를 뒤집을 수 있다
    cnt += k // lst[i]        # k를 리스트안의 큰 숫자들부터 나눈 몫을 cnt로 세준다
    k %= lst[i] 
print(cnt)



