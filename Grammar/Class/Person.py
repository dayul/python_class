class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print(self.name + "가 " + food + "을 먹습니다.")

    def __str__(self):
        return self.name + "는 " + str(self.age) + "살 입니다."


# Person을 Employee에 상속
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)     # super() : 부모의 생성자를 정확히 명시
        self.salary = salary

    def get_salary(self):
        print("급료를 받습니다.")
        return self.salary

e = Employee("철수", 19, 100)
print(e)        # __str__을 출력 (객체를 문자열로 출력할 때 사용)
e.eat("밥")

r = e.get_salary()
print("급료는 " + str(r) + "만 원입니다.")