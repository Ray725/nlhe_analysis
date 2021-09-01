from utils import pretty_print_card
from deck import Deck

class TestDeck():
    def test_creates_expected_card_deck(self):
        deck = Deck()
        assert len(deck.deck) == 52

    def test_deals_unique_hands_without_replacement(self):
        deck = Deck()
        unique_cards = set()
        first_hand = deck.deal_hand()
        assert len(first_hand) == 2
        unique_cards.update(first_hand)

        second_hand = deck.deal_hand()
        assert len(second_hand) == 2
        unique_cards.update(second_hand)

        third_hand = deck.deal_hand()
        assert len(third_hand) == 2
        unique_cards.update(third_hand)

        # We expect the set to contain six elements.
        # If it contains otherwise, there were likely
        # duplicates or some other error in hand size.
        assert len(unique_cards) == 6
        assert deck.above_top_card_ptr == 52 - 6
