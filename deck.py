import numpy as np

class Deck:
    '''Represents a deck of cards. Optimized for
    dealing NLHE thousands of times.
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
        self.shuffle()
        self.above_top_card_ptr = 52

    def deal_cards(self, num_cards: int, with_burn=True) -> np.ndarray:
        '''Randomly deals cards from deck.

        Args:
            num_cards: the number of cards to deal from the deck.
            with_burn: whether or not to burn a card before dealing.

        Returns: ints representing cards in a numpy array, sorted for
            later efficiency.
        '''
        if with_burn:
            self.above_top_card_ptr -= 1

        dealt = self.deck[self.above_top_card_ptr-num_cards:self.above_top_card_ptr]
        self.above_top_card_ptr -= num_cards
        return np.sort(dealt)

    def deal_hand(self) -> np.ndarray:
        '''Randomly selects two cards from deck without
        replacement.

        Returns: two ints in a numpy array, sorted for later
            efficiency.
        '''
        return self.deal_cards(num_cards=2, with_burn=False)

    def deal_flop(self) -> np.ndarray:
        '''Randomly flops three cards from deck without
        replacement.

        Returns: three ints in a numpy array, sorted for later
            efficiency.
        '''
        return self.deal_cards(num_cards=3, with_burn=True)

    def deal_turn(self) -> np.ndarray:
        '''Randomly turns a card from deck without
        replacement.

        Returns: an int in a numpy array.
        '''
        return self.deal_cards(num_cards=1, with_burn=True)

    def deal_river(self) -> np.ndarray:
        '''Randomly rivers a card from deck without
        replacement.

        Returns: an int in a numpy array.
        '''
        return self.deal_cards(num_cards=1, with_burn=True)
