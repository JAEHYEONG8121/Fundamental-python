# 위의 터렛문제에서 6개의 좌표를 입력했을 때 그때의 출력값이 바로나오느 것이 아니라
# 3가지 경우의 6개의 좌표를 입력하고, 그 후에 출력값 3개가 나오게 하는 법
# result = []와 같은 빈 리스트를 설정하고, 결과값을 이 리스트에 저장해두었다가
# 마지막에 for문을 돌려서 for i in range(len(result)) : 이렇게 해서 
# print(result[i])이렇게 해주면 된다!!
number_list = [1,2,3,4,5,6,7,8,9,10]
print(number_list[3:8:4])
 