import random

class cards:
    def __init__(self):
        self.cards = self.build_deck()
        
    def build_deck(self):
        suits = 'CDHS' # clubs hearts hearts spades
        cards = []
        for suit in range(4):
            for card in range(1,14):
                cards.append(str(card)+suits[suit])
        return cards

    def draw_card(self):
        drawn_card = random.choice(self.cards)
        self.cards.pop(self.cards.index(drawn_card))
        return drawn_card


if __name__ == '__main__':
    deck = cards()
    print(deck.draw_card())
    print(deck.draw_card())
