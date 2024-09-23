class Car:
    # 생성자
    def __init__(self, type, speed):
        self.type = type
        self.speed = speed

    # self 값을 통해서 접근가능 (Java의 this 역할)
    def move(self):
        print(self.type, self.speed)

    def speed_up(self, amount):
        self.speed += amount

    def speed_down(self, amount):
        self.speed -= amount

c = Car("스포츠카", 100)
c.speed_up(10)
c.move()
c.speed_down(10)
c.move()