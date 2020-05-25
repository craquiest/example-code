# coding: utf-8
from random import choice 
from frenchdeck import Card, FrenchDeck

Card

beer_card = Card('7', 'diamonds')
beer_card

deck = FrenchDeck()
deck
len(deck)
deck[:3]
deck[-1]
deck[12::13]

choice(deck)
choice(deck)
choice(deck)

Card('Q', 'hearts') in deck
Card('Q', 'hearts') in deck
Card('Z', 'clubs') in deck

for card in deck:
    print(card)
    
for card in reversed(deck):
    print(card)
    
for n, card in enumerate(deck, 1):
    print(n, ':', card)
    
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
suit_values['spades']

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
    
spades_high(Card('2', 'clubs'))
spades_high(Card('A', 'spades'))

for card in sorted(deck, key=spades_high):
    print(card)
    
