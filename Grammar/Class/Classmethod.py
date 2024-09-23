class Car1:
    # 따로 정의되어 있는 것 == 클래스 메소드
    count = 0

    def __init__(self, type, speed):
        self.type = type
        self.speed = speed
        Car1.count += 1

    # classmethod는 self 대신, cls 사용
    @classmethod
    def get_count(cls):
        # 그냥 멤버변수도 접근 가능, 하지만 에러
        # 클래스 메소드에서는 클래스 변수만 사용 가능
        # cls.speed
        return cls.count

print(Car1.get_count())     # 0 초기화만 됨

c1 = Car1('스포츠카', 100)
c2 = Car1('트럭', 50)

print(Car1.get_count())     # 2 : __init__()