print(10, "의 절댓값 : ", abs(10))
print(10, "의 절댓값 : ", abs(-10))

print(128, "의 2진수 : ", bin(128))
print(7, "의 8진수 : ", oct(7))
print(15, "의 16진수 : ", hex(15))


numbers = [1, 2, 3, 4, 5]
print(numbers, "중 가장 큰 값은 ", max(numbers))
print(numbers, "중 가장 작은 값은 ", min(numbers))
print(numbers, "의 합계는 ", sum(numbers))
print("2의 10승은 ", pow(2, 10))

pi = 3.141592
print(pi, "의 소수점 1자리 반올림은", round(pi))      # 정수 부분만 표현
print(pi, "의 소수점 1자리 반올림은", round(pi,0))    # 0번째 소수점까지
print(pi, "의 소수점 1자리 반올림은", round(pi,1))    # 1번째까지
print(pi, "의 소수점 1자리 반올림은", round(pi,2))    # 2번째까지