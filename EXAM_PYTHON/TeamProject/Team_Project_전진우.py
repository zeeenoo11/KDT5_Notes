# ----------------------------------------------
# BlackJack
# ----------------------------------------------
import random
import time

def blackjack(balance):  # main func
    time.sleep(1)
    print("♥ ◆ ♣ ♠ Welcome to BlackJack ♥ ◆ ♣ ♠")

    # 1. betting
    print('your Balance:',balance,'$')
    bet_amount = betting(balance)
    time.sleep(1)

    # 2. game Start
    playerDeck, dealerDeck = [], []
    gameStart(playerDeck, dealerDeck)  # nothing returned
    print()

    # 3. player Turn
    # time.sleep(1)
    playerChoice(playerDeck)
    print()

    # 4. Dealer Turn
    dealerChoice(dealerDeck)
    time.sleep(1)
    print()

    # 5. Consider Winner & Price
    balance = considerWinner_givePrice(playerDeck,dealerDeck,balance,bet_amount)
    time.sleep(1)

    # 6. consider Replay
    considerReplay(balance)

    # 7. Ranking
    Ranking(balance)
    # blackjack(balance) fin.


def randomCard():
    return random.randint(1,11)


def betting(balance):
    while True:
        bet_amount = input('How much do you bet? ')
        if not bet_amount.isnumeric(): print('Wrong enter; only type number')
        elif balance < int(bet_amount): print("You don't have enough money.")
        elif 0 >= int(bet_amount): print("Wrong Amount of bet. Try again.")
        else: break
    return bet_amount


def gameStart(playerDeck, dealerDeck):
    print("Game Started."); time.sleep(1)
    playerDeck += [randomCard() for _ in range(2)]  # append initial card
    dealerDeck += [randomCard() for _ in range(2)]  # append initial card
    print(f"Dealer's first Card: {dealerDeck[0]}"); time.sleep(1)  # Show one dealer's card


def playerChoice(playerDeck):  # player act in this function
    print(f'Card draw: {playerDeck[0]}, {playerDeck[1]}'); time.sleep(1)  # show initial deck
    if sum(playerDeck) == 21:  # if blackjack:
        print("You are BlackJack!"); return
    while True:  # hit or stop; if over 21, turn ended
        print(f"Your Deck : {playerDeck}, total: {sum(playerDeck)}")
        choice = input("Choose how you act (.. hit, - stay) ")
        time.sleep(1)
        if choice == '..':  # if hit
            playerDeck += [randomCard()]; print('Card draw:',playerDeck[-1]); time.sleep(1)
            if sum(playerDeck) > 21: print(f'Total: {sum(playerDeck)}, You busted.'); break
        elif choice == '-': print("Stay."); break  # if player stop, turn ended
        else: print('Wrong gesture; Try again.')  # if not .. or -
    time.sleep(1)


def dealerChoice(dealerDeck):
    while True:
        print(f"Dealer's Deck : {dealerDeck}, total: {sum(dealerDeck)}")
        time.sleep(1)
        if 21 >= sum(dealerDeck) >= 17: print("""Dealer: "Stay." """); break
        elif 21 < sum(dealerDeck): print('Dealer has busted!'); break
        else: dealerDeck += [randomCard()]
    return sum(dealerDeck)


def considerA(sum):
    pass


def considerWinner_givePrice(playerDeck,dealerDeck,balance,bet_amount):  # define winner and consider bet
    def considerWinner(playerDeck, dealerDeck):  # define winner and return 1 or 0 or -1
        def compareDeck():  # compare Deck and return number
            # bust check
            if sum(playerDeck) > 21:  # player Busted
                return 0 if sum(dealerDeck) > 21 else -1  # both busted: 0, dealer alive: -1
            elif sum(playerDeck) <= 21:  # player alive
                if sum(dealerDeck) > 21:
                    return 1  # dealer busted
                else:
                    if sum(playerDeck) == sum(dealerDeck):  # if sum is same
                        return len(dealerDeck) - len(playerDeck)  # check length
                    else:
                        return sum(playerDeck) - sum(dealerDeck)  # check sum
        if compareDeck() > 0:
            return 1  # player win
        elif compareDeck() == 0:
            return 0  # push
        elif compareDeck() < 0:
            return -1  # dealer win

    time.sleep(1)
    betRate = 1  # 100%
    if considerWinner(playerDeck, dealerDeck) == 1:  # if player win
        print('Player Win!'); print('You earn', int(bet_amount) * betRate, '$')
        balance += int(bet_amount) * betRate
        return balance  # bets are transferred to balance
    elif considerWinner(playerDeck, dealerDeck) == 0:  # if pushed
        print('Push.'); print('Your bets are returned.')  # Nothing changed
        return balance
    elif considerWinner(playerDeck, dealerDeck) == -1:  # if dealer win
        print('Dealer Win!'); print('You lost', int(bet_amount), '$')
        balance -= int(bet_amount)
        return balance  # lost bets

def considerReplay(balance):
    print("Your balance is",balance); time.sleep(1)
    if balance <= 0: print("You got bankrupt, Game Over.")
    else:
        replayQuestion = input("\nEnter '1' if you want to try again. ")
        print()
        if replayQuestion.isnumeric():
            if int(replayQuestion) == 1: return blackjack(balance)  # recursive func.
        else:
            time.sleep(1)
            print("Game Ended.",end=' ')
            if balance > BALANCE: print("You have earned",balance-BALANCE,'$!')
    time.sleep(1)


def Ranking(balance):
    while True:
        name_in = input("Enter your name : ")
        if len(name_in) == 3:
            name = name_in; break
        else:
            print("Only 3 alphabets is approved")
    with open('ranking_sys', mode='r', encoding='utf-8') as f_r:
        f_r.readline()
        data = sorted(f_r.readlines() + [f'{balance:5d} $ - {name}\n'], reverse=True)
        data_w = ''
        for line in data:
            data_w += line
        with open('ranking_sys', mode='w', encoding='utf-8') as f:
            f.write('----- <BlackJack Ranking> -----\n')
            f.write(data_w)
        print("Your Rank has been uploaded.")
        f_r.seek(0); print(f_r.read())

    time.sleep(3)
# cardDictMain = {'♥1': 1, '♥2': 2, '♥3': 3, '♥4': 4, '♥5': 5, '♥6': 6, '♥7': 7, '♥8': 8, '♥9': 9, '♥10': 10, '♥J': 10, '♥Q': 10,
#  '♥K': 10, '♥A': 11, '◆1': 1, '◆2': 2, '◆3': 3, '◆4': 4, '◆5': 5, '◆6': 6, '◆7': 7, '◆8': 8, '◆9': 9, '◆10': 10,
#  '◆J': 10, '◆Q': 10, '◆K': 10, '◆A': 11, '♣1': 1, '♣2': 2, '♣3': 3, '♣4': 4, '♣5': 5, '♣6': 6, '♣7': 7, '♣8': 8,
#  '♣9': 9, '♣10': 10, '♣J': 10, '♣Q': 10, '♣K': 10, '♣A': 11, '♠1': 1, '♠2': 2, '♠3': 3, '♠4': 4, '♠5': 5, '♠6': 6,
#  '♠7': 7, '♠8': 8, '♠9': 9, '♠10': 10, '♠J': 10, '♠Q': 10, '♠K': 10, '♠A': 11}


BALANCE = 100
blackjack(BALANCE)