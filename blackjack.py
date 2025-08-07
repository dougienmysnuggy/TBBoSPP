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
BACKSIDE = 'backside'

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

def display_hand(dealer, player, show_dealer_hand):
    # for each card in hand
    # build lines (5 columns 5 rows)
    #  ___
    # |R  |
    # | S |
    # |__R|
    #  
    
    #show dealer's hand
    if show_dealer_hand:
        #show both cards
        print('DEALER:', get_hand_value(dealer))
        display_cards(dealer)
    else:
        #2nd card is face down
        print('DEALER: ???', )
        display_cards([BACKSIDE] + dealer[1:])
        
    #show player's hand
    print('Player:', get_hand_value(player))
    display_cards(player)
        
def display_cards(hand):  
    #build the cards row by row. 
    rows = ['', '', '', '', '']
    for i, card in enumerate(hand):
        #print top row
        rows[0] += ' ___ '
        if card == 'backside':
            #print backside of card
            rows[1] += '|## |'
            rows[2] += '|###|'
            rows[3] += '|_##|'
        else:
            rank, suit = card
            rows[1] += '|{}  |'.format(rank)
            rows[2] += '| {} |'.format(suit)
            rows[3] += '|__{}|'.format(rank)           
        
    for row in rows:
        print(row)         
    
def get_hand_value(hand):
    # gets the value of the hand passed
    
    aces = 0 #check our aces later, they'll be 1 and then at the end we'll see if they can be 10
    value = 0 #initialize hand value
    
    for card in hand:
        rank = card[0]
        if rank == 'A':
            aces += 1
        elif rank in ["J", "Q", "K"]:
            value += 10
        else:
            value += int(rank)
    
    # now add 1 for each ace
    value += aces
    
    for i in range(aces):
        if value + 10 <= 21:
            value += 10
    
    return value    

def get_player_command():
    player_command = (input('(h)it (s)tand or (d)ouble? '))
    if player_command.upper() not in ["H", "S", "D"]:
        get_player_command

    return player_command.upper()

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
        print()
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
        display_hand(dealer_hand, player_hand, False)
        #now player needs to hit stand or double until he busts or stands or doubles and gets 1 card
        while True:
            #loop for player inputs
            action = get_player_command()
            if action == "D":
                #doubled down (get 1 card, break)
                player_hand.append(deck.pop())
                display_hand(dealer_hand, player_hand, False)
                break
            elif action == "H":
                #hit 
                player_hand.append(deck.pop())
                display_hand(dealer_hand, player_hand, False)
            else:
                #stand
                display_hand(dealer_hand, player_hand, False)
                break

            # evaluate player_hand to see if we continue
            if get_hand_value(player_hand) > 21:
                print('YOU BUSTED! GAME OVER')
                break
            elif get_hand_value(player_hand) == 21:
                # dealer's turn!
                break


        #now dealer needs to hit on <=16 and stand on >= 17
        while True:
            if get_hand_value(dealer_hand) < 17:
                dealer_hand.append(deck.pop())
                display_hand(dealer_hand, player_hand, True)
            else:
                break
            if get_hand_value(dealer_hand) > 21:
                print('DEALER BUSTED! YOU WIN!')
                money += bet * 2
                break
            if get_hand_value(player_hand) > get_hand_value(dealer_hand):
                print('YOU WIN!')
                money += bet * 2
                break
            elif get_hand_value(player_hand) < get_hand_value(dealer_hand):
                print('DEALER WINS!')
                break
            else:
                print('PUSH! YOU GET YOUR BET BACK')
                money += bet
                break
if __name__ == '__main__':
    main()