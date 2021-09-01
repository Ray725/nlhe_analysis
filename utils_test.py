from utils import pretty_print_card, pretty_print_hand
from deck import Deck

class TestUtils():

    def test_pretty_print_works_property(self):
        deck = Deck()
        assert pretty_print_card(1) == 'Ac'
        assert pretty_print_card(13) == 'Kc'
        assert pretty_print_card(24) == 'Jd'
        assert pretty_print_card(51) == 'Qs'

    def test_pretty_print_hand_works_property(self):
        deck = Deck()
        hand = deck.deal_hand()
        assert pretty_print_hand(hand) == 'Qs,Ks'
