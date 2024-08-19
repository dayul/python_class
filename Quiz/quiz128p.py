# 이름과 성을 나누어 리턴하는 함수
def div_name(name):
    first = name[0]
    mid = name[1:]
    return first, mid

first, mid = div_name("추다율")
print("성 : {}, 이름 : {}".format(first, mid))