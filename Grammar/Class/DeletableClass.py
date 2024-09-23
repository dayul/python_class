class DeletableClass:
    def __del__(self):
        print("Delete")

d = DeletableClass()
del d        # 지워질 때 출력
            # del 하지 않아도 소멸될 때 출력됨