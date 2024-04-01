t = ()
xy = (235, 434)
color = 123, 34, 642
print(xy + color)
print(xy * 2)   # list도 같음

# 패킹과 언패킹
color = 134, 342, 534       # 패킹 (134, 342, 534) - 괄호를 생략해도 묶어서 대입
red, green, blue = color    # 언패킹
print(red)
print(green)

# 활용
x,y = 2132, 5235
print(x)
print(y)

a = (123, "abc", True, 123)
print(a[0])     # 인덱싱, 123
print(a[:2])    # 슬라이싱, (123, 'abc')

# a[1] = 2 - error, 값을 수정할 수 없음

x = 10
y = 50
x,y = y,x   # 직관적으로 swap(교환)가능
print(x)

print(a.index("abc"))   # "abc"의 인덱스 값 가져옴, 1 (find와 비교해보기)
print(a.count(123))     # 2개

