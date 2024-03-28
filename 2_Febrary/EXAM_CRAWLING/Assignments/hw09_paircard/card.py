# - 한 장의 카드를 나타내기 위한 클래스
# - suit와 number의 값을 가짐

class Card:
    def __init__(self, card_suit, card_number):
        self.suit = card_suit
        self.number = card_number

    def __repr__(self):  # 공식 문자열 표현 [ ]
        """
        객체를 공식적인 문자열로 반환(인터프리터에서 객체 표현에 사용)
        """
        return f'[{self.suit},{self.number:>2}]'

    def __str__(self):  # 비공식 문자열 표현 ( )
        """
        객체를 문자열로 반환: print(객체)에 사용
        :return:
        """
        return f"({self.suit},{self.number:>2})"


if __name__ == "__main__":
    card = Card('♠', 10)
    print(card)     # card의 주소를 반환
