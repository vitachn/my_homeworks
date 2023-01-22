cards = ['2 spade', '2 club', '2 heart', '2 diamond', '3 spade', '3 club', '3 heart', '3 diamond', '4 spade',
         '4 club', '4 heart', '4 diamond', '5 spade', '5 club', '5 heart', '5 diamond', '6 spade', '6 club',
         '6 heart', '6 diamond', '7 spade', '7 club', '7 heart', '7 diamond', '8 spade', '8 club', '8 heart',
         '8 diamond',
         '9 spade', '9 club', '9 heart', '9 diamond', '10 spade', '10 club', '10 heart', '10 diamond', 'jack spade',
         'jack club', 'jack heart', 'jack diamond', 'queen spade', 'queen club', 'queen heart', 'queen diamond',
         'king spade', 'king club', 'king heart', 'king diamond', 'ace spade', 'ace club', 'ace heart', 'ace diamond']


def CardDeck(numbers):
    for card in numbers:
        yield card


my_game = CardDeck(cards)

print(next(my_game))
print(next(my_game))
print(next(my_game))
print(next(my_game))


# Task CardDeck via Iterator
cards = ['2 spade', '2 club', '2 heart', '2 diamond', '3 spade', '3 club', '3 heart', '3 diamond', '4 spade',
             '4 club', '4 heart','4 diamond', '5 spade', '5 club', '5 heart', '5 diamond', '6 spade', '6 club',
             '6 heart', '6 diamond','7 spade','7 club','7 heart','7 diamond','8 spade','8 club','8 heart','8 diamond',
             '9 spade','9 club','9 heart','9 diamond','10 spade','10 club','10 heart','10 diamond','jack spade',
             'jack club', 'jack heart', 'jack diamond', 'queen spade', 'queen club', 'queen heart','queen diamond',
             'king spade','king club', 'king heart', 'king diamond', 'ace spade', 'ace club', 'ace heart', 'ace diamond']

cardsIterator=iter(cards)
print(cardsIterator)

print(next(cardsIterator))
print(next(cardsIterator))
print(next(cardsIterator))
print(next(cardsIterator))

