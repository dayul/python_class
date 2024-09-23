class Person1:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    # 클래스에 대한 설명을 return
    def __str__(self):
        return f'이름 : {self.name} 나이: {self.age}, 키 : {self.height}'

    # 길이 관련된 것을 return
    def __len__(self):
        return self.height

    def __getitem__(self, key):
        if key == "name":
            return self.name
        if key == "age":
            return self.age
        return None

p = Person1("영희", 18, 170)
print(p)            # __str__()
print(len(p))       # 170 출력 : __len__ 객체를 넘긴 상황
print(p['age'])     # 18 출력 : __getitem__()
print(p['unknown']) # None