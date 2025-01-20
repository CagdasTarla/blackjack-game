import random
logo = '''
 ____    ____    ____    ____
|2   |  |A   |  |Q   |  |T   |
|(\/)|  | /\ |  | /\ |  | &  |
| \/ |  | \/ |  |(__)|  |&|& |
|   2|  |   A|  | /\Q|  | | T|     
`----`  `----'  `----'  `----' '''
percentage = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
dict_of_cards = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10, "A":11}
def hit_user():
    global new_card
    new_card = random.choice(list(dict_of_cards.keys()))
    new_card_value = dict_of_cards[new_card]
    global user_point 
    global user_cards
    user_cards.append(new_card)
    user_point += new_card_value
    print(f"Your card is {new_card}")
def hit_computer():
    global new_card
    new_card = random.choice(list(dict_of_cards.keys()))
    new_card_value = dict_of_cards[new_card]
    global computer_point 
    global computer_cards
    computer_cards.append(new_card)
    computer_point += new_card_value
loop = True
while loop == True:
    user_point = 0
    user_cards = []
    computer_point = 0
    computer_cards = []
    new_card = ""
    input("Press enter to start: ")
    print(logo)
    print("Welcome to blackjack!")
    hit_user()
    hit_user()
    hit_computer()
    hit_computer()
    print(f"You got {user_cards}. You have {user_point} points.")
    print(f"Dealer got {new_card} and an unknown card.")
    start_stop = input("Would hou like to hit or stand? Type 'hit' or 'stand'. ")
    indicator = 0
    while start_stop == "hit":
        hit_user()
        if user_point <= 21:
            print(f"You got {user_cards}. You have {user_point} points.")
            start_stop = input("Would hou like to hit? Type 'hit' or 'stand'. ")
        elif user_point > 21 :
            if "A" in user_cards:
                if user_cards[0] == "A":
                    if indicator == 0:
                        user_point -= 10
                if user_cards [1] == "A":
                    if indicator == 0:
                        user_point -= 10
                if new_card == "A":
                    user_point -= 10
                    print(f"You got {user_cards}. You have {user_point} points.")
                    start_stop = input("Would hou like to hit? Type 'hit' or 'stand'. ")
                else:
                    start_stop = "stand"
            else:
                start_stop = "stand"
        indicator += 1
    while True:
        indicator1 = 0
        if computer_point <= 11:
            hit_computer()
        elif computer_point == 12:
            if random.choice(percentage) > 31:
                hit_computer()
                continue
            else:
                break
        elif computer_point == 13:
            if random.choice(percentage) > 39:
                hit_computer()
                continue
            else:
                break
        elif computer_point == 14:
            if random.choice(percentage) > 56:
                hit_computer()
                continue
            else:
                break
        elif computer_point == 15:
            if random.choice(percentage) > 58:
                hit_computer()
                continue
            else:
                break
        elif computer_point == 16:
            if random.choice(percentage) > 62:
                hit_computer()
                continue
            else:
                break
        elif computer_point == 17:
            if random.choice(percentage) > 69:
                hit_computer()
                continue
            else:
                break
        elif computer_point == 18:
            if random.choice(percentage) > 77:
                hit_computer()
                continue
            else:
                break
        elif computer_point == 19:
            if random.choice(percentage) > 85:
                hit_computer()
                continue
            else:
                break
        elif computer_point == 20:
            if random.choice(percentage) > 92:
                hit_computer()
                continue
            else:
                break
        elif computer_point == 21:
            break
        else:
            if computer_point > 21 and "A" in computer_cards:
                if computer_cards[0] == "A":
                    if indicator1 == 0:
                        computer_point -= 10
                if computer_cards [1] == "A":
                    if indicator1 == 0:
                        computer_point -= 10
                if new_card == "A":
                    computer_point -= 10
                    continue
                else:
                    break
            else:
                break
        indicator1 += 1
    # Final phase. Code will calculate the winner.
    print("\n")
    if user_point == 21:
            if computer_point == 21:
                print(f"Your cards were {user_cards} and you got {user_point} points.")
                print(f"Dealer's cards were {computer_cards} and dealer got {computer_point} points.")
                print("It is a draw with two BLACKJACKS!!! ")
            else:
                print(f"Your cards were {user_cards} and you got {user_point} points.")
                print(f"Dealer's cards were {computer_cards} and dealer got {computer_point} points.")
                print("You won with a BLACKJACK!!! Dealer lost!")
    elif computer_point == 21:
            print(f"Your cards were {user_cards} and you got {user_point} points.")
            print(f"Dealer's cards were {computer_cards} and dealer got {computer_point} points.")
            print("Dealer won with a BLACKJACK!!! You lost!")
    elif user_point > 21:
        print(f"You bust and lost! Your cards were {user_cards} and you had {user_point} points.")
    elif computer_point > 21:
        print(f"Dealer bust and lost! Dealer's cards were {computer_cards}. Dealer had {computer_point} points. ")
    elif user_point < computer_point:
        print(f"Your cards were {user_cards} and you got {user_point} points.")
        print(f"Dealer's cards were {computer_cards} and dealer got {computer_point} points.")
        print("Dealer won! You lost!")
    elif user_point > computer_point:
        print(f"Your cards were {user_cards} and you got {user_point} points.")
        print(f"Dealer's cards were {computer_cards} and dealer got {computer_point} points.")
        print("You won! Dealer lost!")
    elif user_point == computer_point:
        print(f"Your cards were {user_cards} and you got {user_point} points.")
        print(f"Dealer's cards were {computer_cards} and dealer got {computer_point} points.")
        print("It is a draw!")