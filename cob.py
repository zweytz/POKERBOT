import random
import itertools
from stat import FILE_ATTRIBUTE_NO_SCRUB_DATA

CARD_ORDER = '1234567890JQKA'
SUITS = 'DCHS'

def sort_cards(cards):
    sorted_hand = sorted(cards, key=Card_Key)
    return sorted_hand


def Card_Key(card):
    rank_score = CARD_ORDER.index(card[0])
    suit_score = SUITS.index(card[1])
    return rank_score, suit_score

def get_pairs(cards):
    cards = sort_cards(cards)
    pairs = []
    for i in range(len((cards)) - 1):
        if CARD_ORDER.index(cards[i][0]) == CARD_ORDER.index(cards[i + 1][0]):
            pairs.append([cards[i], cards[i+1]])
    return pairs

def get_threes(cards):
    cards = sort_cards(cards)
    threes = []
    for i in range(len((cards)) - 2):
        if CARD_ORDER.index(cards[i][0]) == CARD_ORDER.index(cards[i+1][0]) and CARD_ORDER.index(cards[i][0]) == CARD_ORDER.index(cards[i+2][0]):
            threes.append([cards[i], cards[i+1], cards[i+2]])
    return threes    

def get_fours(cards):
    cards = sort_cards(cards)
    fours = []
    for i in range(len((cards)) - 3):
        if CARD_ORDER.index(cards[i][0]) == CARD_ORDER.index(cards[i+1][0]) and CARD_ORDER.index(cards[i][0]) == CARD_ORDER.index(cards[i+2][0]) and CARD_ORDER.index(cards[i][0]) == CARD_ORDER.index(cards[i+3][0]):
            fours.append([cards[i], cards[i+1], cards[i+2], cards[i+3]])
    return fours     

def play(player, flop, current_bet, players_still_in):

    hand = player['hand'] + flop

    if current_bet > player['funds']:
        return 'fold'
    else:
        return 'raise 10'
    
# return formatting:
# for fold, return 'fold'
# for stay, return 'stay'
# for raise, return 'raise {amount}' e.g 'raise 10'

print(get_threes(['3D', 'AC', 'KD', '3H', 'AH', '4D', '4C', '4H', 'KH', 'KC', '3C', '3S']))