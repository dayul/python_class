import pickle

class Person:
     def __init__(self, name, age):
         self.name = name
         self.age = age

     def __str__(self):
         return ("이름 : " + self.name + "\n나이 : " + str(self.age))

f = open('person_data.bin', 'wb')

p = Person("철수", 20)
pickle.dump(p, f)       # p 변수의 내용을 파일에 저장
f.close()