import random

# print("Welcome to Black Jack")

import pyfiglet
print(pyfiglet.figlet_format("BLACK JACK", font="big"))
# print("Welcome to Black Jack!\n")

# get user details
name = str(input("Please enter your name: "))
age = int(input("Please enter your age: "))


# check if user is old enough to play
if age >= 18:
    print("Welcome", name)
else:
    print("You are not old enough to play ", name)
    exit()


cards = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 0,
}

#suits = ["hearts", "diamonds", "clubs", "spades"]

# soorce for icons: https://www.unicode.org/charts/PDF/U2600.pdf
suits = ["Hearts \u2665", "Diamonds \u2666", "Clubs \u2663", "Spades \u2660"]

game_over = False

# first card
card_1 = random.choice(list(cards))
suit_1 = random.choice(suits)

# second card
card_2 = random.choice(list(cards))
suit_2 = random.choice(suits)

print(f"Your first card is: {card_1} of {suit_1}")
print(f"Your second card is: {card_2} of {suit_2}")

# add up the first two cards - ace is worth 1 or 11, so ask the player
total = 0

if card_1 == "ace":
    ace_value = int(input("Your first card is an ace! Count it as 1 or 11? "))
    total = total + ace_value
else:
    total = total + cards[card_1]

if card_2 == "ace":
    ace_value = int(input("Your second card is an ace! Count it as 1 or 11? "))
    total = total + ace_value
else:
    total = total + cards[card_2]

print("Your total is:", total)

#  now start hit or stick loop

while game_over is False:
    hs = input("Would you like to hit or stick? (h/s): ")
    # get new card and add total
    if hs == "h":
        new_card = random.choice(list(cards))
        new_suit = random.choice(suits)
        print(f"Your new card is: {new_card} of {new_suit}")

        if new_card == "ace":
            ace_value = int(input("You got an ace! Count it as 1 or 11? "))
            total = total + ace_value
        else:
            total = total + cards[new_card]

        print("Your updated total is:", total)

        # if total is more thab 21,  see gave over to true causing while loop to exit
        if total > 21:
            game_over = True
            print("You have busted! Game over.")

    # If users choses stick - show current total and exit loop
    elif hs == "s":
        print("You chose to stick. Your final total is:", total)
        game_over = True

    else:
        print("Please enter h to hit or s to stick.")



