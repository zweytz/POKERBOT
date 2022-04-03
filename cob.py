import random
import itertools
from stat import FILE_ATTRIBUTE_NO_SCRUB_DATA

def play(player, flop, current_bet, players_still_in):
    if current_bet > player['funds']:
        return 'fold'
    else:
        return 'raise 10'
    
# return formatting:
# for fold, return 'fold'
# for stay, return 'stay'
# for raise, return 'raise {amount}' e.g 'raise 10'