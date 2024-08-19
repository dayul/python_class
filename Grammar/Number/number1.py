from builtins import type

print(0b110011100)  # 2진수
print(0o130)    # 8진수
print(0xD7A)    # 16진수

print(type(0o130))  # <class 'int'>

print(10e3)     # 10.0 * 10^3
print(1.23456E2)

a = 8 + 24j     # 복소수 표현
print(a)
print(type(a))  # <class 'complex'>
print(a.real)   # 실수 부분 표현
print(a.imag)   # 허수 부분 표현
print(a.conjugate())    # 켤레 복소수 구함

d = 1j
print(d * d.conjugate())    # 실수 부분만 남김

