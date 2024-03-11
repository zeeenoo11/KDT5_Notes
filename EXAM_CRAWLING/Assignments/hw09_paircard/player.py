# - 자신이 가지고 있는 카드 관리
#   - 두 개의 리스트를 가짐 (holding_card_list, open_card_list)
# - 두 장의 동일한 카드를 제거하는 기능
#   - 번호가 동일한 경우, holding_card_list에서 open_card_list로 이동: 테이블에 공개하는 기능
# - 두 개의 리스트를 출력하는 기능
from card import Card


class Player:
    def __init__(self, name):
        self.name = name
        self.holding_card_list = []
        self.open_card_list = []

    def add_card_list(self, card_list):
        self.holding_card_list.extend(card_list)

    def display_two_card_lists(self):
        def print_list(list_):
            for i in range(len(list_)):
                if (i == len(list_) - 1) | (((i + 1) % 13) == 0):
                    print(f"{list_[i]}")
                else:
                    print(f"{list_[i]}", end=" ")

        print('='*70)
        print(f'[{self.name}] Open Card List: ', len(self.open_card_list))
        print_list(self.open_card_list)
        print()
        print(f'[{self.name}] Holding Card List: ', len(self.holding_card_list))
        print_list(self.holding_card_list)

    def check_one_pair_card(self):
        for card1 in self.holding_card_list:
            for card2 in self.holding_card_list:
                if ((card1.number == card2.number)
                        & (card1 != card2)):
                    self.open_card_list.append(card1)
                    self.open_card_list.append(card2)
                    self.holding_card_list.remove(card1)
                    self.holding_card_list.remove(card2)
                    break   # break문으로 not in 할 필요 없음


# - 테스트
if __name__ == '__main__':
    player1 = Player('Alice')
    player2 = Player('Bob')

    player1.add_card_list([Card('S', 1), Card('H', 1), Card('q', 1), Card('S', 4), Card('S', 5)])

    player2.add_card_list([Card('H', 1), Card('d', 3), Card('H', 3), Card('H', 4), Card('H', 5)])

    player1.display_two_card_lists()
    player2.display_two_card_lists()

    player1.check_one_pair_card()
    player2.check_one_pair_card()

    player1.display_two_card_lists()
    player2.display_two_card_lists()