# https://en.wikipedia.org/wiki/Blackjack

import cards
class blackjack():
    def __init__(self,player_count=1):
        self.cards = cards.cards()
        self.hands = []
        self.player_count = player_count
        for player in range(player_count):
            self.hands.append([])
    
    def draw_card(self,player):
        drawn_card = self.cards.draw_card()
        self.hands[player].append(drawn_card)
        return
    
    def setup_standard_game(self):
        for player in range(self.player_count):
            for draw in range(2):
                self.draw_card(player)

    def count_hand_total(self,player):
        total = 0
        for card in self.hands[player]:
            total += int(card[:-1])
        return total

    def format_cards(self,player):
        out_string = ''
        for card in self.hands[player]:
            string = card
            replacements = [('11','Jack'),('12','Queen'),('13','King'),('1','Ace'),('S',' of Spades'),('H',' of Hearts'),('C',' of Clubs'),('D',' of Diamonds')]
            for char in replacements:
                if char[0] in string:
                    if '10' in string and char[0] == '1':
                        continue
                    string = string.replace(*char)
            out_string += string
            if card is not self.hands[player][-1]:
                out_string += ', '
        return out_string

    def print_status(self):
        print('Dealer has {}, total is {}'.format(self.format_cards(0),self.count_hand_total(1)))
        for player in range(1,self.player_count):
            print('Player {} has {}, total is {}'.format(player,self.format_cards(player),self.count_hand_total(player)))


def simulate_game(debug=0,player_limit=17):
    game = blackjack(player_count=2)
    game.setup_standard_game()
    while game.count_hand_total(0) < 17:
        game.draw_card(0)
    if game.count_hand_total(0) > 21:
        if debug:
            print('deal busts')
        return True
    while game.count_hand_total(1) < player_limit:
        game.draw_card(1)
    if game.count_hand_total(1) > 21:
        if debug:
            print('player busts')
        return False
    if game.count_hand_total(1) > game.count_hand_total(0):
        if debug:
            print('player count higher')
        return True
    else:
        if debug:
            print('dealer count higher')
        return False

def run_big_sim(sim_count=100,tests=[*range(14,21)]):
    results = {}
    for test in tests:
        results[test] = 0
        for sim in range(sim_count):
            if simulate_game(player_limit=test):
                results[test] += 1
        results[test] = str(round(results[test] / sim_count * 100,2)) + '%'
    print(results)



if __name__ == '__main__':    
    run_big_sim(1000)
    # print('Setup standard 2 player game')        
    # game = blackjack(player_count=2)
    # game.setup_standard_game()
    # game.print_status()
    # results = 0
    # for x in range(100):
    #     if simulate_game():
    #         results += 1
    # print (results)
    # print(run_game())


# print(game.hands)




# def run_game():
#     deck = cards.cards()
#     total = 0
#     while True:
#         drawn_card = deck.draw_card()
#         total += int(drawn_card[:-1])
#         # print('draw card',drawn_card, ',total is', total)
#         if total > 21:
#             # print('bust at',total)
#             # print(total)
#             return total
#         elif total > 16:
#             # print('stand at', total)
#             # print(total)
#             return total

# results = {}
# for x in range(17,21+11):
#     results[x] = 0
# for x in range(10000):
#     result = run_game()
#     results[result] += 1

# total = sum(results.values())
# percentages = []
# for x in results.values():
#     percentages.append(round(x/total*100,2))
# print('percentages',percentages)
# print(results)