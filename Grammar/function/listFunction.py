list = ['a', 'b', 'c', 'd']
list.sort(reverse=True)     # 내림차순 정렬

for index, value in enumerate(list):        # 2가지 값
    print("인덱스", index, "위치의 값은 ", value)

print(len(list))

list.sort(reverse=True)
for index, value in enumerate(list) :
    print(index, value)