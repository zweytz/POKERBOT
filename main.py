import random
import coon
import cob

CARD_ORDER = '1234567890JQKA'
SUITS = 'DCHS'

DECK = []
for card in CARD_ORDER:
    for suit in SUITS:
        DECK.append(card + suit)

def deal_cards(DECK, PLAYERS):
    random.shuffle(DECK)

    for player in PLAYERS:
        i = 0
        while i < 2:
            player['hand'].append(DECK[i])
            DECK.pop(i)
            i = i+1

number_of_players = 2
players = []
flop = []

for i in range(1,number_of_players+1):
    name = 'Player ' + str(i)
    hand = []
    funds = 50
    players.append({'name': name, 'hand': hand, 'funds': funds, 'current_bet': 10, 'still_in': True, 'previous_play': ''})

deal_cards(DECK, players)

current_bet = 10
print('\nThe game has begun.')
print('Betting starts at $10\n')
i = 0
while len(flop) < 5:
    players_still_in = 0
    for player in players:
        if player['still_in'] == True:
            players_still_in += 1
    if players_still_in < 2:
        break



















    

    # #while players[0]['previous_play'] != 'stay' and players[1]['previous_play'] != 'stay':

    # #Player 1 Turn
    # player1_play = cob.play(players[0], flop, current_bet, players)
    # print('Player one returned:', player1_play)
    # if player1_play == 'fold':
    #     players[0]['still_in'] = False
    #     players[0]['previous_play'] = player1_play
    # elif player1_play == 'stay':
    #     players[0]['still_in'] = False
    #     players[0]['previous_play'] = player1_play
    # elif player1_play == 'call':
    #     players[0]['previous_play'] = player1_play
    #     players[0]['current_bet'] += (current_bet - players[0]['current_bet'])
    #     players[0]['funds'] -= (current_bet - players[0]['current_bet'])
    # else:
    #     player1_play = player1_play.split(' ')
    #     if player1_play[0] == 'raise':
    #         current_bet += int(player1_play[1])
    #         players[0]['previous_play'] = player1_play
    #         players[0]['current_bet'] += int(player1_play[1])
    #         players[0]['funds'] -= int(player1_play[1])
    # print('The current bet is now:',current_bet,'\n')
    
    # #Player 2 Turn
    # player2_play = coon.play(players[1], flop, current_bet, players)
    # print('Player two returned:', player2_play)
    # if player2_play == 'fold':
    #     players[1]['still_in'] = False
    #     players[1]['previous_play'] = player2_play
    # elif player2_play == 'stay':
    #     players[1]['previous_play'] = player2_play
    # else:
    #     player2_play = player2_play.split(' ')
    #     if player2_play[0] == 'raise':
    #         current_bet += int(player2_play[1])
    #         players[1]['previous_play'] = player2_play
    #         players[1]['current_bet'] += int(player2_play[1])
    #         players[1]['funds'] -= int(player2_play[1])

    # flop.append(DECK[i])
    # DECK.pop(i)

for player in players:
    if player['still_in'] == True:
        print('\n' + player['name'], 'has won the hand!\n')

        

