# https://realpython.com/python-data-classes/
# https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass
from dataclasses import asdict, field


@dataclass
class DataClassCard:
    rank: str
    suit: str

# The boilerplate code of the __init__ method is replaced.

queen_of_hearts = DataClassCard('Q', 'Hearts')
print(queen_of_hearts.rank)
print(queen_of_hearts == DataClassCard('Q', 'Hearts'))  # True, won't be with equal normal objects


# Advantages over dictionaries are:
# - you won't have to remember what it represents (explained in the Class name).
# - you won't have to remember the variable names.
# - we can add default values
# namedtuples is a good alternative if you want immutability or need tuple behaviour.



@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

print(Position("Greenwich", lat=51.8))

# Type hints are mandatory, but not enforced at runtime.
# If you do not want type hints, set the type to Any (must be imported from typing).

# You can add any method.

from typing import List

@dataclass
class PlayingCard:
    rank: str
    suit: str

@dataclass
class Deck:
    cards: List[PlayingCard]

# https://docs.python.org/3/library/dataclasses.html#dataclasses.asdict  # <== Kjører med 3.9, men ikke 3.8(!)
# For <=3.8, use from typing import List

deck = Deck([PlayingCard("Q", "Hearts"), PlayingCard("A", "Spades")])
print(Deck)