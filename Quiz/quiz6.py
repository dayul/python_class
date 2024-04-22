# score = map.input("' '로 구분하여 성적을 입력하세요: ").split(" ")
# map : list안 변수를 정수로 만듦

score = input("' '로 구분하여 성적을 입력하세요: ").split(" ")
print(score)
Sum = 0

for i in score:
    Sum += int(i)

print("총합 : {}".format(Sum))
print("평균 : {:.1f}".format(Sum / len(score)))


