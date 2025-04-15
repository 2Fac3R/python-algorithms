"""
    Book: Fluent Python by Luciano Ramalho
    A Pythonic Card Deck
    Example 1-1. A deck as a sequence of playing cards
"""
# from collections import namedtuple
from typing import NamedTuple

# Card = namedtuple('Card', ['rank', 'suit'])


class Card(NamedTuple):
    rank: str
    suit: str


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card: Card) -> int:
    """Return a value for the card for sorting."""
    rank_value: int = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


class FrenchDeck:
    """ A standard deck of playing cards.
    The deck is a sequence of 52 cards, each with a rank and suit.
    The ranks are '2' to '10', 'J', 'Q', 'K', and 'A'.
    The suits are 'spades', 'hearts', 'diamonds', and 'clubs'.

    Tests:
        >>> beer_card = Card('7', 'diamonds')
        >>> beer_card
        Card(rank='7', suit='diamonds')
        >>> deck = FrenchDeck()
        >>> len(deck)
        52
        >>> deck[0]
        Card(rank='2', suit='spades')
        >>> deck[-1]
        Card(rank='A', suit='hearts')
        >>> deck[:2]
        [Card(rank='2', suit='spades'), Card(rank='3', suit='spades')]
        >>> for card in deck:  # doctest: +ELLIPSIS
        ...     print(card)
        Card(rank='2', suit='spades')
        Card(rank='3', suit='spades')
        Card(rank='4', suit='spades')
        ...
        >>> Card('Q', 'hearts') in deck
        True
        >>> Card('7', 'beasts') in deck
        False
        >>> for card in sorted(deck, key=spades_high):  # doctest: +ELLIPSIS
        ...     print(card)
        Card(rank='2', suit='clubs')
        Card(rank='2', suit='diamonds')
        Card(rank='2', suit='hearts')
        ...
    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self) -> int:
        return len(self._cards)

    def __getitem__(self, position: int) -> Card:
        return self._cards[position]


if __name__ == '__main__':
    from doctest import testmod
    testmod()
