import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return ("이름 : " + self.name + "\n나이 : " + str(self.age))

f = open("person_data.bin", 'rb')
person = pickle.load(f)     # 직렬화 되어 저장된 파일을 load 메소드에 전달 -> 리스트 객체를 얻음
print(person)
f.close()

f = open("person_data.bin", 'rb')
persons = pickle.load(f)

for p in persons:
    print(p)

f.close()