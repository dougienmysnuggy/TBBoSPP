'''
Blackjack

Text version of blackjack. 

Steps:

Show Money
Get Bet
    Make sure it's a valid bet
create a deck
shuffle the deck
deal cards to build player hand and dealer hand
    show both player's cards, but only 1 of the dealer's
evaluate hands
Hit, Stand, Double
If Hit, deal another card, evaluate hand, back to hsd
If Stand, dealer's turn, evaluate hands and see who wins
Double player gets 1 more hit only, then dealer's turn, evaluate and see who wins

Author: Wes Leonard
Email: leonardw@gmail.com
'''

import sys, random

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

def get_bet():
    wager = input('Enter Bet Amount: ')
    if wager == "QUIT":
        sys.exit()
    return int(wager)

def build_deck():
    card_deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2,11):
            card_deck.append((str(rank), suit))
        for rank in ("J", "Q", "K", "A"):
            card_deck.append((rank, suit))
    random.shuffle(card_deck)
    return card_deck

def display_hand(player):
    '''
     ---
    | R |
    | S |
     ---
    '''

    
    pass

def main():
    money = 5000
    # game loop
    while True:
        print('You have ${}'.format(money))
        valid_bet = False
        # make sure we get a valid bet
        while valid_bet == False:
            bet = get_bet()
            if bet < 5 or bet > money:
                print('Invalid Wager. Try again.')
                valid_bet = False
            else:
                valid_bet = True
        
        #subtract wager from total
        money -= bet
        dealer_hand = []
        player_hand = []
        # get a new, shuffled deck
        deck = build_deck()
        # time to deal
        # deal one to player, one to dealer, repeate
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())
        #Display dealer hand (first card is backside), other is face up
        #Display player hand (both cards face up)
        display_hand(dealer_hand)
        display_hand(player_hand)
        
        

if __name__ == '__main__':
    main()