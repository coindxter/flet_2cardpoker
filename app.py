import flet as ft
import random
import time

cards = { 

    1: ['Ace of Spades',13],
    2: ['2 of Spades', 1],
    3: ['3 of Spades', 2],
    4: ['4 of Spades', 3],
    5: ['5 of Spades', 4],
    6: ['6 of Spades', 5],
    7: ['7 of Spades', 6],
    8: ['8 of Spades', 7],
    9: ['9 of Spades', 8],
    10: ['10 of Spades', 9],
    11: ['Jack of Spades', 10],
    12: ['Queen of Spades', 11],
    13: ['King of Spades', 12],
    14: ['Ace of Hearts', 13],
    15: ['2 of Hearts', 1],
    16: ['3 of Hearts', 2],
    17: ['4 of Hearts', 3],
    18: ['5 of Hearts', 4],
    19: ['6 of Hearts', 5],
    20: ['7 of Hearts', 6],
    21: ['8 of Hearts', 7],
    22: ['9 of Hearts', 8],
    23: ['10 of Hearts', 9],
    24: ['Jack of Hearts', 10],
    25: ['Queen of Hearts', 11],
    26: ['King of Hearts', 12],
    27: ['Ace of Clubs', 13],
    28: ['2 of Clubs', 1],
    29: ['3 of Clubs', 2],
    30: ['4 of Clubs', 3],
    31: ['5 of Clubs', 4],
    32: ['6 of Clubs', 5],
    33: ['7 of Clubs', 6],
    34: ['8 of Clubs', 7],
    35: ['9 of Clubs', 8],
    36: ['10 of Clubs', 9],
    37: ['Jack of Clubs', 10],
    38: ['Queen of Clubs', 11],
    39: ['King of Clubs', 12],
    40: ['Ace of Diamonds', 13],
    41: ['2 of Diamonds', 1],
    42: ['3 of Diamonds', 2],
    43: ['4 of Diamonds', 3],
    44: ['5 of Diamonds', 4],
    45: ['6 of Diamonds', 5],
    46: ['7 of Diamonds', 6],
    47: ['8 of Diamonds', 7],
    48: ['9 of Diamonds', 8],
    49: ['10 of Diamonds', 9],
    50: ['Jack of Diamonds', 10],
    51: ['Queen of Diamonds', 11],
    52: ['King of Diamonds', 12],

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

    p2CARD = []
    p2CARD1 = random_numbers[2]
    p2CARD2 = random_numbers[3]
    p2CARD.append(cards[p2CARD1])
    p2CARD.append(cards[p2CARD2])
    cards.pop(p2CARD1)
    cards.pop(p2CARD2)

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

    return p1CARD, p2CARD, river

def build_container(name, color):
    return ft.Container(
        content=ft.Text(name),
        bgcolor=color,
        padding=15,
    )

def build_button(name, color, callbac=None):
    if callbac is None:
        button = ft.ElevatedButton(
            name,
            bgcolor=color,
        )
    else:
        button = ft.ElevatedButton(
            name,
            bgcolor=color,
            on_click=callbac
        )
    return button

def app(page: ft.Page):
    (p1CARD, p2CARD, river) = playerhand()

    count_text = ft.TextField(value="0")

    r1 = build_container("", ft.colors.BLUE)
    r2 = build_container("", ft.colors.BLUE)
    r3 = build_container("", ft.colors.BLUE)
    r4 = build_container("", ft.colors.BLUE)
    r5 = build_container("", ft.colors.BLUE)

    p1 = build_container(p1CARD[0][0], ft.colors.BLUE)
    p2 = build_container(p1CARD[1][0], ft.colors.BLUE)
    p3 = build_container(p2CARD[0][0], ft.colors.BLUE)
    p4 = build_container(p2CARD[1][0], ft.colors.BLUE)

    pot = build_container("0", ft.colors.BLACK)

    bank1 = build_container("100", ft.colors.GREEN)
    bank2 = build_container("100", ft.colors.GREEN)

    p1BET = ft.TextField(label="Bet")
    p2BET = ft.TextField(label="Bet")

    p1CALL = build_button("CALL", ft.colors.YELLOW)
    p2CALL = build_button("CALL", ft.colors.YELLOW)

    winner = build_container("", ft.colors.BLACK)

    def p1BET_BUTTON(e):
        sum1 = int(p1BET.value)
        sum2 = int(pot.content.value)
        sum3 = sum1 + sum2
        pot.content.value = str(sum3)
        sum4 = int(bank1.content.value)
        sum5 = sum4 - sum1
        bank1.content.value = str(sum5)
        page.update()

    def highcard():
        p1MAX =  max(p1CARD[0][1], p1CARD[1][1])
        p2MAX =  max(p2CARD[0][1], p2CARD[1][1])
        if p1MAX == p2MAX:
            p1MIN = min(p1CARD[0][1], p1CARD[1][1])
            p2MIN = min(p2CARD[0][1], p2CARD[1][1])
            if p1MIN > p2MIN:
                winner.content.value = "Player One Wins"
                sum1 = int(pot.content.value)
                sum2 = int(bank1.content.value)
                sum3 = sum1 + sum2
                bank1.content.value = str(sum3)
                page.update()
            else:
                winner.content.value = "Player Two Wins"
                sum1 = int(pot.content.value)
                sum2 = int(bank2.content.value)
                sum3 = sum1 + sum2
                bank2.content.value = str(sum3)
                page.update()
        elif p1MAX > p2MAX:
            winner.content.value = "Player One Wins"
            sum1 = int(pot.content.value)
            sum2 = int(bank1.content.value)
            sum3 = sum1 + sum2
            bank1.content.value = str(sum3)
            page.update()
        else:
            winner.content.value = "Player Two Wins"
            sum1 = int(pot.content.value)
            sum2 = int(bank2.content.value)
            sum3 = sum1 + sum2
            bank2.content.value = str(sum3)
            page.update()
              
    def p2BET_BUTTON(e):

        count = int(count_text.value) + 1
        count_text.value = str(count)

        sum1 = int(p2BET.value)
        sum2 = int(pot.content.value)
        sum3 = sum1 + sum2
        pot.content.value = str(sum3)
        sum4 = int(bank2.content.value)
        sum5 = sum4 - sum1
        bank2.content.value = str(sum5)
        if count == 1:
            r1.content.value = river[0][0]
        if count == 2:
            r2.content.value = river[1][0]
        if count == 3:
            r3.content.value = river[2][0]
        if count == 4:
            r4.content.value = river[3][0]
            r5.content.value = river[4][0]
            highcard()
 
        page.update()
        
    p1BET_BUTTON = build_button("BET", ft.colors.ORANGE, callbac=p1BET_BUTTON)
    p2BET_BUTTON = build_button("BET", ft.colors.ORANGE, callbac=p2BET_BUTTON)
    
    pColumn1 = ft.Container(
                content=ft.Column(
                    [
                        ft.Text(("Player One"), size=16),
                        bank1,
                        p1,
                        p2,
                        p1BET,
                        p1BET_BUTTON,
                        #p1CALL,
                        #p1FOLD,
                    ],
                ),
            )

    pColumn2 = ft.Container(
                content=ft.Column(
                    [
                        ft.Text(("Player Two"), size=16),
                        bank2,
                        p3,
                        p4,
                        p2BET,
                        p2BET_BUTTON,
                        #p2CALL,
                        #p2FOLD,
                    ],
                ),
            )

    pColumns = ft.Container(
                content=ft.Row(
                    [
                        pColumn1,
                        pColumn2,
                    ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=400,
                ),
            )

    river3 = ft.Container(
                content=ft.Row(
                    [
                        r1,
                        r2,
                        r3
                    ],
                alignment=ft.MainAxisAlignment.CENTER
                ),
            )

    river2 = ft.Container(
                content=ft.Row(
                    [
                        r4,
                        r5
                    ],
                alignment=ft.MainAxisAlignment.CENTER
                ),
            )

    riverPOT = ft.Container(
                content=ft.Row(
                    [
                        pot,
                    ],
                alignment=ft.MainAxisAlignment.CENTER
                ),
            )

    winnerROW = ft.Container(
        content=ft.Row(
            [
                winner,
            ],
            alignment=ft.MainAxisAlignment.CENTER
            ),
        )

    def start_button(e):
        page.controls.pop()
        page.update()
        page.add(
            river3,
            river2,
            riverPOT,
            pColumns,
            winnerROW,
        )

    page.add(
        ft.FilledButton(
            "play", 
            on_click=start_button,
            style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30),
            ),
    )

ft.app(target=app, view=ft.AppView.WEB_BROWSER)