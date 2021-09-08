import numpy as np

def pretty_print_card(card_number: int) -> str:
    '''Formats card in deck to be human-readable.

    Args:
        card_number: card position in deck array.

    Returns:
        String of the form 'Ah', '2c', etc.
    '''
    card_suit = 'INVALID_SUIT'
    if card_number <= 13:
        # the first thirteen digits are clubs
        card_suit = 'c'
    elif card_number <= 26:
        # the second thirteen digits are diamonds
        card_suit = 'd'
    elif card_number <= 39:
        # the third thirteen digits are hearts
        card_suit = 'h'
    else:
        # the fourth thirteen digits are spades
        card_suit = 's'

    # the card values are determined by modulo thirteen
    modulo = card_number % 13
    card_value = 'INVALID_VALUE'
    modulo_to_value = {
        0: 'K',
        1: 'A',
        11: 'J',
        12: 'Q'
    }
    if modulo not in modulo_to_value:
        card_value = str(modulo)
    else:
        card_value = modulo_to_value[modulo]

    return card_value + card_suit

def pretty_print_cards(cards: np.ndarray) -> str:
    '''Formats dealt cards to be human-readable.

    Args: cards, cards randomly dealt w/out
        replacement from the deck.

    Returns: string of the form 'Ah,2c'.
    '''
    card_strings = []
    for card_idx in range(len(cards)):
        card_strings.append(pretty_print_card(cards[card_idx]))

    return ','.join(card_strings)

def determine_hand_status(hand: np.ndarray, board: np.ndarray) -> np.ndarray:
    '''Returns the types of hands made or semi-made.
    '''
    hands = {
        'high_card_in_hand': 0,
        'two_high_cards_in_hand': 1,
        'under_pair': 2,
        'pair': 3,
        'top pair': 4,
        'over_pair': 5,
        'two_pair': 6,
        'set': 7,
        'backdoor_straight_draw': 8,
        'straight_draw': 9,
        'straight': 10,
        'backdoor_flush_draw': 11,
        'flush_draw': 12,
        'flush': 13,
        'full_house': 14,
        'quads': 15,
        'straight_flush': 16
    }

    # analyze for card values
    # analyze for card matching combos
    # analyze for straights
    # analyze for flushes
    # analyze for straight flushes

def pretty_print_hand_status(hand_status_array: np.ndarray) -> str:
    pass
