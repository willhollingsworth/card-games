# https://en.wikipedia.org/wiki/Blackjack

import cards



def run_game():
    deck = cards.cards()
    total = 0
    while True:
        drawn_card = deck.draw_card()
        total += int(drawn_card[:-1])
        # print('draw card',drawn_card, ',total is', total)
        if total > 21:
            # print('bust at',total)
            # print(total)
            return total
        elif total > 16:
            # print('stand at', total)
            # print(total)
            return total

results = {}
for x in range(17,21+11):
    results[x] = 0
for x in range(10000):
    result = run_game()
    results[result] += 1

total = sum(results.values())
percentages = []
for x in results.values():
    percentages.append(round(x/total*100,2))
print('percentages',percentages)
print(results)