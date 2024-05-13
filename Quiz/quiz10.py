# 1부터 100까지의 합 구하기
# for문 이용
answer = 0
for i in range(1,101):
    answer += i
print(answer)

# while문 이용
answer = 0
i = 1
while i <= 100 :
    answer += i
    i+=1
print(answer)