# - 각 클래스의 객체 생성 및 게임 진행
# 1단계
# - GameDealer : 각 player에게 초기 10장, deck[]에서 10장씩 각 player에게
#                deck에는 총 20장이 삭제됨
#                GameDealer가 보유한 deck 출력
# - Player : 자신이 가진 두 리스트 출력하는 함수
#            리스트에서 하나씩 가져와 print(card) 형태로 출력
#            dealer가 전달해 준 10장의 카드를 자신의 holding 에 저장
#            player는 자신이 가진 카드 목록을 화면에 출력

# 2단계 (순차 검색)
# - Player : 번호가 같은 한 쌍의 카드 제거
#            holding 에서 번호가 같은 카드를 open 으로 이동
#            두 리스트의 현황 출력

# 3단계~
# - 반복 수행 : GameDealer 기능 : 각 Player에게 4장씩 카드를 나눠 줌
#               Player 기능     : dealer가 준 카드를 holding 에 저장
#                                 5단계 기능 반복 : 번호가 같은 한 쌍의 카드 제거
# - 게임 종료 조건 : dealer의 deck의 수가 0 혹은 각 player의 holding 카드의 수가 0 이 될 때
from player import Player
from gamedealer import GameDealer


def play_game():
    # 두 명의 player 객체 생성
    player1 = Player('흥부')
    player2 = Player('놀부')
    dealer = GameDealer(); stage = 1

    # 0단계 : 카드 생성 및 섞기
    print('[GameDealer] 초기 카드 생성')
    dealer.make_deck()
    dealer.print_deck()
    print('[GameDealer] 카드 랜덤하게 섞기')
    GameDealer.shuffle_deck(dealer)
    dealer.print_deck()

    # 카드 배분 함수
    def deal_card(stage):
        if stage == 1: count = 10
        else: count = 4
        print(f'카드 나누어 주기: {count}장')
        dealer.deal_card(count, player1)
        dealer.deal_card(count, player2)
        dealer.print_deck()
        player1.display_two_card_lists()
        player2.display_two_card_lists()

    # 한쌍의 숫자 제거 함수
    def check_one_pair(stage):
        input(f'[{stage}]단계: 다음 단계 진행을 위해 Enter 키를 누르세요!\n')
        print(f'[{player1.name}: 숫자가 같은 한 쌍의 카드 검사]')
        player1.check_one_pair_card()
        player2.check_one_pair_card()
        player1.display_two_card_lists()
        player2.display_two_card_lists()

    # 게임 종료 조건 함수
    def check_game_over(dealer_, p1, p2):
        if ((len(dealer_.deck) == 0)
                or (len(p1.holding_card_list) == 0)
                or (len(p2.holding_card_list) == 0)):
            return True
        else:
            return False

    # [ 본문 ]
    while True:
        # 1단계 : 각 player에게 10장 카드 나누기
        # 반복  : 4장씩 나눠주기
        print('='*70)
        deal_card(stage)
        # 종료 조건 확인
        if check_game_over(dealer, player1, player2):
            break   # 종료 조건 확인 함수

        # 2단계  : 번호가 같은 한 쌍의 카드 제거
        # 3단계~ : 반복
        stage += 1
        check_one_pair(stage)


if __name__ == "__main__":
    play_game()
