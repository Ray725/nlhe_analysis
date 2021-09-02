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

    def test_flops_unique_without_replacement(self):
        deck = Deck()
        unique_cards = set()
        first_hand = deck.deal_hand()
        assert len(first_hand) == 2
        unique_cards.update(first_hand)

        flop = deck.deal_flop()
        assert len(flop) == 3
        unique_cards.update(flop)

        # We expect the set to contain five elements.
        # If it contains otherwise, there were likely
        # duplicates or some other error in dealing.
        assert len(unique_cards) == 5
        assert deck.above_top_card_ptr == 52 - (2 + 4)

    def test_turns_unique_without_replacement(self):
        deck = Deck()
        unique_cards = set()
        first_hand = deck.deal_hand()
        assert len(first_hand) == 2
        unique_cards.update(first_hand)

        turn = deck.deal_turn()
        assert len(turn) == 1
        unique_cards.update(turn)

        assert len(unique_cards) == 3
        assert deck.above_top_card_ptr == 52 - (2 + 2)

    def test_rivers_unique_without_replacement(self):
        deck = Deck()
        unique_cards = set()
        first_hand = deck.deal_hand()
        assert len(first_hand) == 2
        unique_cards.update(first_hand)

        river = deck.deal_river()
        assert len(river) == 1
        unique_cards.update(river)

        assert len(unique_cards) == 3
        assert deck.above_top_card_ptr == 52 - (2 + 2)
