n = int(input("숫자를 입력하세요 : "))
facto = 1
for i in range(1,n+1):
    facto *= i

print("{}!의 값은 {} 입니다.".format(n, facto))