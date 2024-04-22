greeting = 'hello'
to = "world!"
print(greeting)
print(type(to))      # <class 'str'>

say_hello = greeting + " " + to
print(say_hello)
print(greeting * 5)   # 곱한만큼 반복 출력

print("\" h \n i \" " + to)
multiline = '''Happy    
            programming'''      # 여러줄로 이루어진 문자열 표현1
multiline_1 = """Happy
            programming"""      # 여러줄로 이루어진 문자열 표현2
print(multiline)
print(multiline_1)

a = '"hi"'  # 안에 "" 따옴표 출력
print(a)