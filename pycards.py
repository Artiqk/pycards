import random

class Card:

	_rank = None


	_suit = None


	def __init__(self, rank=None, suit=None):
		if rank is None:
			self._rank = random.choice(self.get_ranks())
		else:
			if rank.lower() not in self.get_ranks():
				raise ValueError(f'Invalid rank : {rank}')
			self._rank = rank.lower()

		if suit is None:
			self._suit = random.choice(self.get_suits())
		else:
			if suit.lower() not in self.get_suits():
				raise ValueError(f'Invalid suit : {suit}')
			self._suit = suit.lower()


	def __str__(self):
		rank = self.get_rank()
		suit = self.get_suit()
		rank_symbole = self.get_rank_symbol(rank)
		suit_symbole = self.get_suit_symbole(suit)
		return f'{rank_symbole}{suit_symbole}'


	def __repr__(self):
		return self.__str__()


	def __eq__(self, other):
		if isinstance(other, Card):
			return self.is_same_value(other) and self.is_same_suit(other)
		else:
			return False


	def __gt__(self, other, is_ace_high=False):
		if isinstance(other, Card):
			return self.get_card_value() > other.get_card_value()
		else:
			raise TypeError(f'Unsupported operand type(s) : {type(self)} and {type(other)}')


	def __lt__(self, other):
		if isinstance(other, Card):
			return self.get_card_value() < other.get_card_value()
		else:
			raise TypeError(f'Unsupported operand type(s) : {type(self)} and {type(other)}')
		

	def __ge__(self, other):
		if isinstance(other, Card):
			return self.get_card_value() >= other.get_card_value()
		else:
			raise TypeError(f'Unsupported operand type(s) : {type(self)} and {type(other)}')
		

	def __le__(self, other):
		if isinstance(other, Card):
			return self.get_card_value() <= other.get_card_value()
		else:
			raise TypeError(f'Unsupported operand type(s) : {type(self)} and {type(other)}')
		
	
	def is_same_color_suit(self, other):
		black_suits = self.get_black_suits()
		red_suits   = self.get_red_suits()
		return (self.get_suit() in black_suits and other.get_suit() in black_suits) or (self.get_suit() in red_suits and other.get_suit() in red_suits)
	

	def is_same_suit(self, other):
		return self.get_suit() == other.get_suit()
	

	def is_same_value(self, other):
		return self.get_card_value() == other.get_card_value()


	def get_card_value(self, is_ace_high=False):
		rank = self.get_rank()
		card_values = self.get_card_values()
		if rank == 'ace':
			if is_ace_high:
				return card_values[rank][1]
			else:
				return card_values[rank][0]
		else:
			return card_values[rank]


	def get_rank(self):
		return self._rank
	

	def get_suit(self):
		return self._suit
	

	def is_spade(self):
		return self.get_suit() == 'spades'
	

	def is_heart(self):
		return self.get_suit() == 'hearts'
	

	def is_club(self):
		return self.get_suit() == 'clubs'
	

	def is_diamond(self):
		return self.get_suit() == 'diamonds'
	

	def is_red_suit(self):
		return self.get_suit() in self.get_red_suits()
	

	def is_black_suit(self):
		return self.get_suit() in self.get_black_suits()
	

	@classmethod
	def create_deck(cls, shuffled=False):
		deck = [Card(rank, suit) for suit in Card.get_suits() for rank in Card.get_ranks()]
		if shuffled:
			random.shuffle(deck)
		return deck


	@classmethod
	def get_ranks(cls):
		return ['ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']


	@classmethod
	def get_suits(cls):
		return ['spades', 'hearts', 'clubs', 'diamonds']
	

	@classmethod
	def get_card_values(cls):
		return {
			'ace': (1, 14),
			'two': 2,
			'three': 3,
			'four': 4,
			'five': 5,
			'six': 6,
			'seven': 7,
			'eight': 8,
			'nine': 9,
			'ten': 10,
			'jack': 11,
			'queen': 12,
			'king': 13
		}
	

	@classmethod
	def get_rank_symbol(cls, rank):
		symboles = {
			'ace':    'A',
			'two':    '2',
			'three':  '3',
			'four':   '4',
			'five':   '5',
			'six':    '6',
			'seven':  '7',
			'eight':  '8',
			'nine':   '9',
			'ten':   '10',
			'jack':   'J',
			'queen':  'Q',
			'king':   'K'
		}
		return symboles[rank]


	@classmethod
	def get_suit_symbole(cls, suit):
		symboles = {
			'spades':   '\u2660',
			'hearts':   '\u2665',
			'clubs':    '\u2663',
			'diamonds': '\u2666'
		}
		return symboles[suit]
	

	@classmethod
	def get_black_suits(cls):
		return ['spades', 'clubs']
	

	@classmethod
	def get_red_suits(cls):
		return ['hearts', 'diamonds']
	


if __name__ == '__main__':
	deck = Card.create_deck(True)
	print(deck)