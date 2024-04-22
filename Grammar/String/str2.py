h = "  Happy Programming!  "
len(h)      # 글자 수 세기

h.count("p")    # h 문자열에서 p의 개수 세기

h.upper()       # 모두 대문자로 변환

h.lower()       # 모두 소문자로 변환

h.strip()       # 왼쪽, 오른쪽 공백 모두 제거

h.replace("Happy", "Funny")     # 문자열 대체하기

print(h.find("ap"))        # h 문자열에서 'ap'를 왼쪽부터 찾기, 3

print(h.rfind("a"))       # h 문자열에서 'a'를 오른쪽부터 찾기, 13

print(h.find("zoo"))       # 찾지 못하면 -1을 리턴

print("a" in h)        # h 문자열에 "a"가 있는지 확인, True

x = "01::23::ab::&&"
y = x.split("::")      # "::"기준으로 나누어 리스트를 만듦
print(y)        # ['01', '23', 'ab', '&&']

z = ", ".join(y)
print(z)        # 01, 23, ab, &&, 리스트를 ", "를 통해서 문자열로 붙임