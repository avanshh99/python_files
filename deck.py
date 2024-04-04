import itertools
import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
print("Initially cards ")

def generate_deck():
    return [{'rank': rank, 'suit': suit} for suit,rank in itertools.product(suits, ranks)]

deck = generate_deck()


for card in deck:
    print(card['rank'], "of", card['suit'])
    
def shuff():
    random.shuffle(deck)
    
shuff()

print("\nShuffled cards: ")
for card in deck:
    print(card['rank'], "of", card['suit'])
