# for문 활용
str = ""
for i in "Hello Python, one two three four":
    str += i.replace("o", "")
print(str)

# while문 활용
str2 = ""
x = list("Hello Python, one two three four")
while x.count("o"):
    x.remove("o")
print("".join(x))