import random


cards = { 

    1: 'Ace of Spades', 
    2: '2 of Spades', 
    3: '3 of Spades', 
    4: '4 of Spades',
    5: '5 of Spades', 
    6: '6 of Spades',
    7: '7 of Spades', 
    8: '8 of Spades', 
    9: '9 of Spades', 
    10: '10 of Spades', 
    11: 'Jack of Spades', 
    12: 'Queen of Spades', 
    13: 'King of Spades',
    14: 'Ace of Hearts', 
    15: '2 of Hearts', 
    16: '3 of Hearts', 
    17: '4 of Hearts', 
    18: '5 of Hearts', 
    19: '6 of Hearts', 
    20: '7 of Hearts', 
    21: '8 of Hearts',
    22: '9 of Hearts', 
    23: '10 of Hearts', 
    24: 'Jack of Hearts', 
    25: 'Queen of Hearts', 
    26: 'King of Hearts',
    27: 'Ace of Clubs',
    28: '2 of Clubs',
    29: '3 of Clubs',
    30: '4 of Clubs',
    31: '5 of Clubs',
    32: '6 of Clubs',
    33: '7 of Clubs',
    34: '8 of Clubs',
    35: '9 of Clubs',
    36: '10 of Clubs',
    37: 'Jack of Clubs',
    38: 'Queen of Clubs',
    39: 'King of Clubs',
    40: 'Ace of Diamonds',
    41: '2 of Diamonds',
    42: '3 of Diamonds',
    43: '4 of Diamonds',
    44: '5 of Diamonds',
    45: '6 of Diamonds',
    46: '7 of Diamonds',
    47: '8 of Diamonds',
    48: '9 of Diamonds',
    49: '10 of Diamonds',
    50: 'Jack of Diamonds',
    51: 'Queen of Diamonds',
    52: 'King of Diamonds',

}

random_numbers = []


for i in range(9):
    while True:
        random_number = random.randint(1, 52)
        if random_number not in random_numbers:
            break
    random_numbers.append(random_number)


def playerhand():

    p1CARD = []
    p1CARD1 = random_numbers[0]
    p1CARD2 = random_numbers[1]
    p1CARD.append(cards[p1CARD1])
    p1CARD.append(cards[p1CARD2])
    cards.pop(p1CARD1)
    cards.pop(p1CARD2)
    print(p1CARD)

    p2CARD = []
    p2CARD1 = random_numbers[2]
    p2CARD2 = random_numbers[3]
    p2CARD.append(cards[p2CARD1])
    p2CARD.append(cards[p2CARD2])
    cards.pop(p2CARD1)
    cards.pop(p2CARD2)
    print(p2CARD)

    river = []
    riverCARD1 = random_numbers[4]
    riverCARD2 = random_numbers[5]
    riverCARD3 = random_numbers[6]
    riverCARD4 = random_numbers[7]
    riverCARD5 = random_numbers[8]
    river.append(cards[riverCARD1])
    river.append(cards[riverCARD2])
    river.append(cards[riverCARD3])
    river.append(cards[riverCARD4])
    river.append(cards[riverCARD5])
    cards.pop(riverCARD1)
    cards.pop(riverCARD2)
    cards.pop(riverCARD3)
    cards.pop(riverCARD4)
    cards.pop(riverCARD5)
    print(river)


