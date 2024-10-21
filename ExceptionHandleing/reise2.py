class InsufficientBalanceError(Exception):
    pass


class WrongAccountNumberError(Exception):
    pass


class Account:
    def __init__(self, money):
        self.money = money

    def checkAccountNumber(self, pwd):
        if pwd != "1234":
            raise WrongAccountNumberError
        else:
            print("맞는 계좌 번호")

    def payment(self, money):
        if self.money - money < 0:
            raise InsufficientBalanceError
        else:
            self.money -= money
            return self.money


account = Account(100)
try:
    # 위에서 에러가 나면 밑에 에러 메세지는 실행되지 않음
    account.checkAccountNumber("1234")
    print(account.payment(101))

except InsufficientBalanceError as e:
    print("잔액 부족!")
except WrongAccountNumberError as e:
    print("계좌번호가 잘못됨!")
else:
    print("문제 없음")
finally:
    print("나는 마지막에 무조건 실행")
