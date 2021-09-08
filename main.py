from deck import Deck
from utils import pretty_print_cards

d = Deck()

for game_idx in range(5):
    print('GAME:', game_idx)
    d.shuffle()
    utg_hand = d.deal_hand()
    btn_hand = d.deal_hand()

    print('UTG:', pretty_print_cards(utg_hand))
    print('BTN:', pretty_print_cards(btn_hand))

    flop = d.deal_flop()
    print('FLOP:', pretty_print_cards(flop))

    turn = d.deal_turn()
    print('TURN:', pretty_print_cards(turn))

    river = d.deal_river()
    print('RIVER:', pretty_print_cards(river))
    print('---------------------------------')
