# 입력받은 정수 n이 정수인지 소수인지 판별하는 코드를 작성하시오
# 소수 : 1과 자기자신 외에는 나누어지지 않는 수

n = int(input("숫자 1개를 입력하세요: "))

for i in range(2, n):
    if n % i == 0:
        print("소수가 아님")
        break
    elif i == n-1 :
        print("소수임")