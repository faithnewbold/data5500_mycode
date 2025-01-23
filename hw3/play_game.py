from DeckofCards import *

play = 0 #to keep track of them wanting to play again

print("\nWelcome to Black Jack! \n")

deck = DeckOfCards()
print("Deck before shuffled: \n")
deck.print_deck()

while play == 0:

    deck.shuffle_deck()
    print("\nDeck after shuffled: \n")
    deck.print_deck()

    #to keep track of aces
    ace = 0
    dealer_ace = 0

    # deal two cards to the user
    card = deck.get_card()
    card2 = deck.get_card()
    if card.val == 11 or card2.val == 11:
        ace += 1

    #deal 2 cards to the dealer
    dealer_card = deck.get_card()
    dealer_card2 = deck.get_card()
    if dealer_card.val == 11 or dealer_card2.val == 11:
        dealer_ace += 1

    score = 0
    # calculate the user's hand score
    score += card.val
    score += card2.val

    dealer_score = 0
    # calculate the user's hand score
    dealer_score += dealer_card.val
    dealer_score += dealer_card2.val

    print("\n Card Number 1 is", card)
    print("Card Number 2 is", card2)
    print("\nYour score is:", score)

    i = 0 #to keep loop going or stop
    #keep track of what card both player and dealer are at
    card_number = 3
    dealer_card_number = 3

    while i == 0:

        # ask user if they would like a "hit" (another card)
        hit = input("\nwould you like a hit (y/n)? ")

        if hit == 'y':
            card3 = deck.get_card()
            if card3.val == 11: #keep track of if they get an ace
                ace += 1
            score += card3.val

            print("\nCard Number", card_number, "is", card3)

            #if they have any aces, subtract 10 for each
            if score > 21 and ace != 0:
                score -= 10 * ace
                print("\nYou got an Ace! Your score is:", score)
                ace = 0
            else:
                print("\nnew score:", score)
            
            if score > 21:
                print("\nYou busted, sorry, you lose.")
                break
            card_number +=1

        else:
            print("\nDealer Card Number 1 is", dealer_card)
            print("Dealer Card Number 2 is", dealer_card2)

            #dealer keeps hitting while score is less than 17
            while dealer_score < 17:
                dealer_card3 = deck.get_card()
                if dealer_card3.val == 11: #keep track if they get an ace
                    dealer_ace += 1
                dealer_score += dealer_card3.val

                print("Dealer Card Number", dealer_card_number, "is", dealer_card3)
                dealer_card_number += 1
            
            #if there are any aces, subtract 10 for each
            if dealer_score > 21 and dealer_ace != 0:
                dealer_score -= 10 * dealer_ace
                dealer_ace = 0

                #if subtracting aces brought score lower than 17, hit again
                while dealer_score < 17:
                    dealer_card3 = deck.get_card()
                    if dealer_card3.val == 11:
                        dealer_ace += 1
                    dealer_score += dealer_card3.val

                    print("Dealer Card Number", dealer_card_number, "is", dealer_card3)
                    dealer_card_number += 1

                print("\nThe dealer got an Ace, Dealer score is:", dealer_score)
            else:
                print("\nDealer score is:", dealer_score, "\n")

            #if the dealer busted
            if dealer_score > 21:
                print("Dealer busted, YOU WIN!!!")
            
            #compare players score to dealers score
            else:
                if score > dealer_score:
                    print("Your score is higher, YOU WIN!!!")
                else: print("Dealer score is higher, you lose.")
            
        
            
            i = 1 #to exit the loop

    #ask user if they would like to play again
    play_again = input("\nWould you like to play again (y/n): ")
    if play_again == 'y':
        play = 0
    else:
        play = 1
