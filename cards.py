import random

class Card():
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit
        
    
    def print_card(self):
        print(f"{self.rank} {self.suit}")


class Deck():  
    def __init__(self):
        self.cards = []
        
        suits = ['H', 'S', 'C', 'D']
        ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        
        for card_suit in suits:
            for card_value in ranks:
                card = Card(card_suit, card_value)
                self.cards.append(card)
                
    def reset_deck(self):
        self.cards = []
        
        suits = ['H', 'S', 'C', 'D']
        ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        
        for card_suit in suits:
            for card_value in ranks:
                card = Card(card_suit, card_value)
                self.cards.append(card)
                
    
    def print_deck(self):
        for card in self.cards:
            print(f'{card.rank}, {card.suit}')
        
        
    def shuffle(self):
        random.shuffle(self.cards)


    def deal_card(self):
        return self.cards.pop()


if __name__ == "__main__":
    # This is all here for testing purposes. 
    # This file should be imported into an main game program.
    dealt_card = Card("", "")
    deck = Deck()
    deck.print_deck()
    deck.shuffle()
    deck.print_deck()
    dealt_card = deck.deal_card()
    dealt_card.print_card()

        