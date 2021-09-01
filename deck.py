import numpy as np

class Deck:
    '''Represents a deck of cards. Optimized for
    dealing NLHE hands thousands of times.
    '''

    def __init__(self) -> None:
        self.deck = np.arange(start=1,stop=53, step=1)
        # Points to one index above the top card in the deck.
        self.above_top_card_ptr = 52

    def shuffle(self) -> None:
        '''Shuffles the deck.'''
        np.random.shuffle(self.deck)

    def reset_deck_and_shuffle(self) -> None:
        '''Returns all cards to deck.'''
        np.random.shuffle(self.deck)
        self.above_top_card_ptr = 52

    def deal_hand(self) -> None:
        '''Randomly selects two cards from deck without
        replacement.

        Returns: two ints in a tuple, sorted for later efficiency.
        '''
        # Creating temp variable for readability.
        hand = self.deck[self.above_top_card_ptr-2:self.above_top_card_ptr]
        self.above_top_card_ptr -= 2
        return np.sort(hand)

