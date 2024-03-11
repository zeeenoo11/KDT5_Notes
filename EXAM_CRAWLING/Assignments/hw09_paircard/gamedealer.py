# - 1벌의 카드(deck) 생성 기능: 리스트로 구현
# - 각 Player 들에게 카드를 나누어 주는 기능
#   - 자신이 가진 deck에서 제거하여 다른 선수들에게 제공
from card import Card
import random


class GameDealer:
    def __init__(self):
        self.deck = list()
        self.suit_number = 13

    def make_deck(self):
        """
        초기 카드 생성
        """
        card_suits = ['♠', '♥', '♦', '♣']
        card_numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for suit in card_suits:
            for number in card_numbers:
                self.deck.append(Card(suit, number))

    def shuffle_deck(self):
        """카드 섞기"""
        random.seed()
        random.shuffle(self.deck)

    def deal_card(self, count, player):
        """
        카드 나누기
        :param count: 나눌 카드 개수
        :param player: 카드를 받을 선수
        :return:
        """
        card_list = list()
        for _ in range(count):
            card = self.deck.pop()
            card_list.append(card)
        player.add_card_list(card_list)

    def print_deck(self):
        """
        13개씩 한 줄로 출력
        """
        print(f"""{'-' * 70}
[GameDealer] 딜러가 가진 카드 수: {len(self.deck)}""")
        for i in range(len(self.deck)):
            if (i == len(self.deck)-1)|(((i+1) % 13) == 0):
                print(f"{self.deck[i]}")
            else:
                print(f"{self.deck[i]}", end=" ")

# if  __name__ == "__main__":
#     game_dealer = GameDealer()
#     game_dealer.make_deck()
#     game_dealer.shuffle_deck()
#     print(game_dealer.print_deck())
