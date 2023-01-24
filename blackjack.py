import random

player_cards = []
dealer_cards = []

player_total = 0
dealer_total = 0
dealer_hidden = 0
maximum_value = 21
dealer_max = 17

card_value = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]

def player_hand():
    player_total = card1 + card2
    while len(player_cards) < 2:
        player_cards = random.choice(card_value)
        player_cards.append(card_value)

        player_total += player_cards.card_value()

def dealer_hand():
    dealer_total = card3 + card4
    while len(dealer_cards) < 2:
        dealer_cards = random.choice(card_value)
        dealer_cards.append(card_value)

        dealer_total += dealer_cards.card_value()

print("Welcome! Let's play a game of Blackjack")
user_choice = input("Would you like to start a game y/n? ")



if user_choice.upper().startswith('Y'):
    player_card1 = random.choice(card_value)
    player_card2 = random.choice(card_value)
    player_total = player_card1 + player_card2
    print("You draw a", player_card1, "and a", player_card2, " Your total is:", player_total )
    dealer_card1 = random.choice(card_value)
    dealer_card2 = random.choice(card_value)
    print("The dealer draws a", dealer_card1, "and a hidden card.")
 #(player_total <= 21):
    player_move = input("Do you wish to hit or stand? Press h or s : ")
else:
    print("Suit yourself, Goodbye")
    exit()
    break
(player_move.upper() == 'H')
player_card_value = random.choice(card_value)
player_total += player_card_value

if (player_total <= 21):
    input("Hit! You draw a " + str(player_card_value) + " Your total is " + str(player_total) + "\nHit or stand? (h/s): ")
elif (player_total > 22):
    print("You draw a", player_card_value, "Your total is", player_total)
    print("You bust. Game over")
if (player_move.upper() == 'S'):
        dealer_total = dealer_card1 + dealer_card2
        print("You stand. The dealer has a", dealer_card1, "and a", dealer_card2)
        print("The dealer's total is", dealer_total)

if (dealer_total < dealer_max):
        dealer_card_value = random.choice(card_value)
        dealer_total += dealer_card_value
        print("The dealer's total is" , dealer_total)
elif (dealer_total >= dealer_max):
        print(dealer_total)
else: (dealer_total > 21)
print("Dealer busts you win!")

if(player_total > dealer_total):
    print("Player's total is: " ,player_total, "Dealer's total is: ",dealer_total, "You won!")
else: (dealer_total >= player_total)
print("Dealer's total is: ", dealer_total, "Player's total is: ", dealer_total)
print("The Dealer wins, you lose.")

#dealer greater 21
#bust
#dealer greater 17
#break
