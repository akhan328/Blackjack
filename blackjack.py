import random

playerNum = 0
enemyNum = 0
pCards = []
eCards = []


def main():
    global playerNum, enemyNum, pCards, eCards
    print("WELCOME TO BLACKJACK!")
    draw_Card()
    draw_Card()
    w = True

    while (w == True):
        q_draw = input("Would you like to draw another card? (Y/N)").upper()

        if q_draw == "Y":
            draw_Card()
        elif q_draw == "N":
            w = False
            end_game()
        else:
            print("Say Y or N")


def draw_Card():
    global playerNum, pCards
    card = random.randint(1, 14)
    num_to_card(card)
    ace_card = 0

    if card == 14:
        print("THE CARD DRAWN IS AN ACE, WOULD YOU LIKE IT AS A one OR eleven?")
        one = input().lower()
        ace_card = 14

        if one == "one":
            card = 1
        else:
            card = 11

    if 10 < card < 14 and ace_card != 14:
        card = 10

    playerNum += card
    print(pCards)


def num_to_card(card):
    global pCards
    if card == 14:
        pCards.append("Ace")
    elif card < 11:
        pCards.append(str(card))
    elif card == 11:
        pCards.append("Jack")
    elif card == 12:
        pCards.append("Queen")
    else:
        pCards.append("King")


def e_draw_card():
    global enemyNum, eCards
    card = random.randint(1, 14)
    e_num_to_card(card)
    ace_card = 0

    if card == 14:
        ace_card = 14

        if enemyNum + 11 <= 21:
            card = 11
        else:
            card = 1

    if 10 < card < 14 and ace_card != 14:
        card = 10

    enemyNum += card
    print(eCards)


def e_num_to_card(card):
    global eCards
    if card == 14:
        eCards.append("Ace")
    elif card < 11:
        eCards.append(str(card))
    elif card == 11:
        eCards.append("Jack")
    elif card == 12:
        eCards.append("Queen")
    else:
        eCards.append("King")


def end_game():
    global playerNum, enemyNum, pCards, eCards
    e_draw_card()

    if enemyNum <= 12:
        e_draw_card()

        if enemyNum <= 15:
            e_draw_card()

            if enemyNum <= 16:
                e_draw_card()

    print(f"DEALER CARDS: {eCards} ({enemyNum})")
    print(f"YOUR CARDS: {pCards} ({playerNum})")

    if enemyNum > 21 and playerNum > 21:
        print("BOTH PLAYERS BUSTED AND LOST")
    elif enemyNum > 21:
        print("CONGRATULATIONS, THE DEALER BUSTED AND YOU WON")
    elif playerNum > 21:
        print("SORRY, YOU BUSTED AND THE DEALER WON")
    elif playerNum == 21 and enemyNum == 21:
        print("DRAW! BOTH PLAYERS GOT A BLACKJACK")
    elif playerNum == 21:
        print("CONGRATULATIONS, YOU GOT A BLACKJACK AND WON!")
    elif enemyNum == 21:
        print("SORRY, THE DEALER GOT A BLACKJACK AND YOU LOST")
    elif playerNum == enemyNum:
        print("DRAW! BOTH PLAYERS GOT THE SAME AMOUNT!")
    elif playerNum > enemyNum:
        print("CONGRATULATIONS, YOU WON!")
    else:
        print("SORRY, YOU LOST!")


main()
