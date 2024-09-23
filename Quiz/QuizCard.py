class Card:
    def __init__(self, number, kind):
        self.number = number
        self.kind = kind

    def compare(self, number, kind):
        if number not in list(range(1, 14)):
            self.print_error(number, kind)
        elif kind not in ['heart', 'diamond', 'club', 'spade']:
            self.print_error(number, kind)
        else :
            print('범위에 포함되었습니다.')

    def print_error(self, number, kind):
        print('{}번호의 {}모양 카드는 범위에 포함되지 않았습니다.'.format(number, kind))


(number, kind) = input('카드 숫자와 문자를 입력하세요: ').split(" ")
user = Card(int(number), kind)
user.compare(int(number), kind)

