## Card Class

The `Card` class represents a standard playing card with rank and suit.

### Attributes

| Attribute | Description                                       |
|-----------|---------------------------------------------------|
| `_rank`   | The rank of the card (e.g., 'ace', 'king').      |
| `_suit`   | The suit of the card (e.g., 'spades', 'hearts', 'diamonds', 'clubs'). |

### Methods

| Method                            | Description                                                                                           |
|-----------------------------------|-------------------------------------------------------------------------------------------------------|
| `__init__(self, rank=None, suit=None)` | Initializes a card object with a random rank and suit if not specified.                          |
| `__str__(self)`                   | Returns a string representation of the card.                                                          |
| `__repr__(self)`                  | Returns a string representation of the card.                                                          |
| `__eq__(self, other)`             | Checks if two cards are equal in value and suit.                                                      |
| `__gt__(self, other)`             | Compares the value of two cards.                                                                      |
| `__lt__(self, other)`             | Compares the value of two cards.                                                                      |
| `__ge__(self, other)`             | Compares if one card's value is greater than or equal to another card's value.                        |
| `__le__(self, other)`             | Compares if one card's value is less than or equal to another card's value.                           |
| `is_same_color_suit(self, other)` | Checks if two cards have the same color suit.                                                         |
| `is_same_suit(self, other)`       | Checks if two cards have the same suit.                                                               |
| `is_same_value(self, other)`      | Checks if two cards have the same value.                                                              |
| `get_card_value(self, is_ace_high=False)` | Returns the numeric value of the card. (optionally considering Ace as high)                   |
| `get_rank(self)`                  | Returns the rank of the card.                                                                         |
| `get_suit(self)`                  | Returns the suit of the card.                                                                         |
| `is_spade(self)`                  | Checks if the card is a spade.                                                                        |
| `is_heart(self)`                  | Checks if the card is a heart.                                                                        |
| `is_club(self)`                   | Checks if the card is a club.                                                                         |
| `is_diamond(self)`                | Checks if the card is a diamond.                                                                      |
| `is_red_suit(self)`               | Checks if the card's suit is red.                                                                     |
| `is_black_suit(self)`             | Checks if the card's suit is black.                                                                   |

### Class Methods

| Method                              | Description                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| `create_deck(cls, shuffled=False)`  | Creates a standard deck of 52 cards.If `shuffled` is set to `True`, the deck will be shuffled.             |
| `get_ranks(cls)`                    | Returns a list of possible card ranks.                                                                     |
| `get_suits(cls)`                    | Returns a list of possible card suits.                                                                     |
| `get_card_values(cls)`              | Returns a dictionary with values assigned to each card rank.                                               |
| `get_rank_symbol(cls, rank)`        | Returns the symbol associated with a given card rank.                                                      |
| `get_suit_symbol(cls, suit)`        | Returns the symbol associated with a given card suit.                                                      |
| `get_black_suits(cls)`              | Returns a list of black suits (spades and clubs).                                                          |
| `get_red_suits(cls)`                | Returns a list of red suits (hearts and diamonds).                                                         |

### Examples

Here are some examples illustrating the usage of the `Card` class:


#### Creating specific cards and displaying their representations
```python
from pycards import *

ace_of_hearts = Card('ace', 'hearts')

random_card = Card()

print(f"Specific Card: {ace_of_hearts}, Random Card: {random_card}")

# Output: Specific Card: A♥, Random Card: K♠
```

#### Comparing cards
```python
from pycards import *

card1 = Card('king', 'spades')

card2 = Card('queen', 'hearts')

print(f"Is card1 > card2 ? {card1 > card2}")

# Output: Is card1 > card2 ? True
```

#### Comparing cards v2
```python
from pycards import *

card1 = Card('Ace ', 'Spades')

card2 = Card('Ace', 'Clubs')

print(f"Is card1 == card2 ? {card1 == card2}")

# Output : Is card1 == card2 ? False
```

#### Creating a deck and displaying the first few cards
```python
from pycards import *

deck = Card.create_deck()

print(f"First 5 cards in the deck: {deck[:5]}")

# Output: First 5 cards in the deck: [list of 5 Card objects]
```

#### Getting rank and suit symbols
```python
from pycards import *

print(f"Symbol for 'king': {Card.get_rank_symbol('king')}, Symbol for 'diamonds': {Card.get_suit_symbol('diamonds')}")

# Output: Symbol for 'king': K, Symbol for 'diamonds': ♦
```