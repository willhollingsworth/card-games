# https://en.wikipedia.org/wiki/Blackjack

import cards

deck = cards.cards()

total = 0

while True:
    drawn_card = deck.draw_card()
    total += int(drawn_card[:-1])
    print('draw card',drawn_card, ',total is', total)
    if total > 21:
        print('bust at',total)
        break
    elif total > 16:
        print('stand at', total)
        break

