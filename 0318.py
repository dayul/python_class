# 추가된 연산자
print(8 // 5)   # 몫 구하기
print(8 ** 5)   # 제곱 수 구하기

age = 18    # 변수 타입 안 씀, 바로 값을 대입해서 사용

age += 2
age -= 2
age *= 2
age /= 2    # 정수라도 소수점이 붙음
print(age)
age //= 2   # 마찬가지로 소수점이 붙음
print(age)
age %= 3    # 마찬가지로 소수점이 붙음
age **= 3

age = 18
print(type(age))    # <class 'int'>
pi = 3.14
print(type(pi))     # <class 'float'>