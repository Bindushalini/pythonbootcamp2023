import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
blackjack = 21


def score(cards_deck):
    if 10 in cards_deck and 11 in cards_deck:
        return 0
    if 11 in cards_deck and sum(cards_deck) > 21:
        val = cards_deck.index(11)
        cards_deck[val] = 1
    return sum(cards_deck)


def compare(user_val, dealer_val):
    if user_val > 21 and dealer_val > 21:
        return "You went over. You lose 😤"

    if user_val == dealer_val:
        return "Draw 🙃"
    elif dealer_val == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_val == 0:
        return "Win with a Blackjack 😎"
    elif user_val > 21:
        return "You went over. You lose 😭"
    elif dealer_val > 21:
        return "Opponent went over. You win 😁"
    elif user_val > dealer_val:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
        user_cards = dealer_cards = []
        print(art.logo_blackj)
        game_over = False
        user_cards = random.choices(cards, k=2)
        dealer_cards = random.choices(cards, k=2)

        print(user_cards, dealer_cards)

        while not game_over:
            usr_score = score(user_cards)
            del_score = score(dealer_cards)
            print(f"you cards : {user_cards}, current score: {sum(user_cards)}")
            print(f"computers first card: {dealer_cards[0]}")
            if usr_score == 0 or del_score == 0 or usr_score > 21:
                game_over = True
            else:
                my_val = input("type 'y' to get another card, type 'n' to pass:? ").lower()
                if my_val == 'y':
                    user_cards.append(random.choice(cards))
                else:
                    game_over = True

        while del_score != 0 and del_score < 17:
            dealer_cards.append(random.choice(cards))
            del_score = score(dealer_cards)

        print(f"   Your final hand: {user_cards}, final score: {usr_score}")
        print(f"   Computer's final hand: {dealer_cards}, final score: {del_score}")
        print(compare(usr_score, del_score))


flag = input("do u want to play a game of blackjack? Type 'y' or 'n'").lower()
while flag == 'y':
    play_game()