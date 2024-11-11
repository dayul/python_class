f = open('text.txt', 'r', encoding='utf-8')

List = []
for l in f:
    List.append(l)

print(List)
f.close()