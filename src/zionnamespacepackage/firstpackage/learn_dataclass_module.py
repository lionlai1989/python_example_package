"""Check real python to discuss this topic."""

from dataclasses import dataclass
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple


@dataclass
class DataClassCard:
    """A data class is a regular Python class. The only thing that sets it apart is that it has basic data model methods like .__init__(), .__repr__(), and .__eq__() implemented for you."""

    rank: str
    suit: str

    # >>> queen_of_hearts = DataClassCard('Q', 'Hearts')
    # >>> queen_of_hearts.rank
    # 'Q'
    # >>> queen_of_hearts
    # DataClassCard(rank='Q', suit='Hearts')
    # >>> queen_of_hearts == DataClassCard('Q', 'Hearts')
    # True


class RegularCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    # >>> queen_of_hearts = RegularCard('Q', 'Hearts')
    # >>> queen_of_hearts.rank
    # 'Q'
    # >>> queen_of_hearts
    # <__main__.RegularCard object at 0x7fb6eee35d30>
    # >>> queen_of_hearts == RegularCard('Q', 'Hearts')
    # False


class RegularCardImitatesDataclass:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.__class__.__name__}" f"(rank={self.rank!r}, suit={self.suit!r})"

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.rank, self.suit) == (other.rank, other.suit)


# Alternatives to Data Classes
# >>> queen_of_hearts_tuple = ('Q', 'Hearts')
# >>> queen_of_hearts_dict = {'rank': 'Q', 'suit': 'Hearts'}
# >>> NamedTupleCard = namedtuple('NamedTupleCard', ['rank', 'suit'])
# >>> queen_of_hearts = NamedTupleCard('Q', 'Hearts')
# >>> queen_of_hearts.rank
# 'Q'
# >>> queen_of_hearts
# NamedTupleCard(rank='Q', suit='Hearts')
# >>> queen_of_hearts == NamedTupleCard('Q', 'Hearts')
# True


@dataclass
class PlayingCard:
    rank: str
    suit: str


# Don’t do this! This introduces one of the most common anti-patterns in Python: using mutable
# default arguments(https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments). The
# problem is that all instances of Deck will use the same list object as the default value of the
# .cards property. This means that if, say, one card is removed from one Deck, then it disappears
# from all other instances of Deck as well. Actually, data classes try to prevent you from doing
# this, and the code above will raise a ValueError.
# @dataclass
# class Deck:  # Will NOT work
#     make_french_deck returns a list
#     cards: List[PlayingCard] = make_french_deck()


@dataclass
class Deck:
    cards: List[PlayingCard] = field(default_factory=make_french_deck)


if __name__ == "__main__":
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
    SUITS = "♣ ♢ ♡ ♠".split()

    def make_french_deck():
        return [PlayingCard(r, s) for s in SUITS for r in RANKS]
