import cards
import random

"""
    Blackjack by Wes Leonard @dougienmesnuggy on Twitter. 
    
    This is a simple Python Blackjack game that uses the cards library that I
    created for various card games.
    
"""

class Player():
    def __init__(self, name, bankroll, hand, bet):
        self.player_name = name
        self.player_money = bankroll
        self.player_hand = hand
        self.player_bet = bet
        
    
    def draw_card(self, deck):
        self.player_hand.append(deck.deal_card())

        
def get_player_bet(p):
    bet_amount = int(input(f'{p.player_name} - Enter bet amount ($1-500): '))
    if bet_amount not in range (1, 501):
        print('Illegal bet. Try again')
        get_player_bet(p)
    else:
        return bet_amount
    
    
def get_num_players():
    num = int(input('Number of Players? (1-4): '))
    if num not in range(1,5):
        print('Invalid entry. Try again.')
        get_num_players()
    else:
        return num    
    

def get_hand_value(ply_hand):
    # pass this function a hand and it will return the blackjack value
    value = 0
    has_aces = False
    for c in ply_hand:
        #check for aces
        if int(c.rank) == 1:
            has_aces = True
        value += min(c.rank, 10)
    if has_aces:
        if value + 10 <= 21:
            value += 10
        has_aces == False
    return value
    
 
def format_card(c):
    """
        ranks:
        11 = J
        12 = Q
        13 = K
        1 = A
        
        suits:
        D = ♦
        H = ♥
        C = ♣
        S = ♠
    """
    card_string = ''
    if c.rank == 1:
        card_string += "A"
    elif c.rank == 11:
        card_string += "J"
    elif c.rank == 12:
        card_string += "Q"
    elif c.rank == 13:
        card_string += "K"
    else:
        card_string += str(c.rank)
        
    if c.suit == "D":
        card_string += "♦"
    elif c.suit == "H":
        card_string += "♥"
    elif c.suit == "C":
        card_string += "♣"
    elif c.suit == "S":
        card_string += "♠"
    else:
        #This should never happen
        card_string += "E"
    return card_string

    
def print_player_hands(p):
    """
    Player 1 (bet): XX, XX (value)
    Player 2 (bet): XX, XX (value)
    Player 3 (bet): XX, XX (value)
    
    Player X Turn:
    Bet:
    Current Hand:
    (H)it, (S)tand, (D)ouble Down, Sur(r)ender
    """
    p_name = p.player_name
    p_bet = p.player_bet
    p_hand = []
    for c in p.player_hand:
        p_hand.append(format_card(c))
    p_hand_value = get_hand_value(p.player_hand)
    print(f'{p_name} (${p_bet}): {p_hand} ({p_hand_value})')
    
    
def get_player_action(p, deck):
    # Hit, Stand, Double, Surrender
    action = input(f'{p.player_name} (H)it, (S)tand, (D)ouble, Sur(R)ender').upper()
    if action not in ['H', 'S', 'D', 'R']:
        print('Invalid action. Try again!')
        get_player_action(p, deck)
    return action    
    

def main():
    # Initialize round                
    blackjack_deck = cards.Deck()
    blackjack_deck.shuffle()
    all_players = []
    num_players = get_num_players()

    #create appropriate amount of players.   
    for i in range(num_players):
        name = "PLAYER " + str(i + 1)
        new_player = Player(name, 5000, [], 0)
        all_players.append(new_player)
        
    # dealer will always be last player in the list (num_players + 1)
    new_player = Player("DEALER", 999999, [], 0)
    all_players.append(new_player)
    
    #blackjack_card = cards.Card("","")

    # Main game loop
    while True:
        # Get a bet from each player (except Dealer)
        for player in all_players[:-1]:
            # if we have money, set player bet, reduce player bankroll
            if player.player_money > 0:
                player.player_bet = int(get_player_bet(player))
                # IF player has money, but not enough to cover bet, it will adjust bet to remaining money
                if player.player_bet > int(player.player_money):
                    player.player_bet = int(player.player_money)
                player.player_money -= player.player_bet

       
        # Deal 2 cards to each player & dealer
        for player in all_players:
            player.draw_card(blackjack_deck)
            
        for player in all_players:
            player.draw_card(blackjack_deck)
             
        # Need to display the hands in a pleasing manner
        for player in all_players:
            print_player_hands(player)

        # Will implement splitting later
         
        # Starting at player 1, get player action until they stand or bust
        for player in all_players:
            is_bust = False
            while is_bust == False: #Player loop (end when bust, or stand, or double (later))
                player_action = get_player_action(player, blackjack_deck)
                if player_action == "H":
                    player.player_hand.append(player.draw_card(blackjack_deck))
                elif player_action == "S":
                    continue
                #elif player_action == "D":
                #    pass
                #elif player_action == "R":
                #    pass
                
                # see if we busted
                hand_value = get_hand_value(player.player_hand)
                if int(hand_value) > 21:
                    is_bust = True
                else:
                    is_bust = False
                    
                if is_bust:
                    print('BUSTED!')

        # if not bust go back to beginning of player loop with updated hand
        # continue loop for each player. Then do dealer with qualifying conditions like in casinos
        
        # determine winners
        
        # pay winners
        
        # repeat until game quit.
        

if __name__ == "__main__":
    main()

