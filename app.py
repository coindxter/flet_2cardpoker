import flet as ft
import random
from icecream import ic
#[51,23,2,45,6,3,48,8,40]

CARDS = { 

    1: ['Ace of Spades',13, 1],
    2: ['2 of Spades', 1, 1],
    3: ['3 of Spades', 2, 1],
    4: ['4 of Spades', 3, 1],
    5: ['5 of Spades', 4, 1],
    6: ['6 of Spades', 5, 1],
    7: ['7 of Spades', 6, 1],
    8: ['8 of Spades', 7, 1],
    9: ['9 of Spades', 8, 1],
    10: ['10 of Spades', 9, 1],
    11: ['Jack of Spades', 10, 1],
    12: ['Queen of Spades', 11, 1],
    13: ['King of Spades', 12, 1],
    14: ['Ace of Hearts', 13, 2],
    15: ['2 of Hearts', 1, 2],
    16: ['3 of Hearts', 2, 2],
    17: ['4 of Hearts', 3, 2],
    18: ['5 of Hearts', 4, 2],
    19: ['6 of Hearts', 5, 2],
    20: ['7 of Hearts', 6, 2],
    21: ['8 of Hearts', 7, 2],
    22: ['9 of Hearts', 8, 2],
    23: ['10 of Hearts', 9, 2],
    24: ['Jack of Hearts', 10, 2],
    25: ['Queen of Hearts', 11, 2],
    26: ['King of Hearts', 12, 2],
    27: ['Ace of Clubs', 13, 3],
    28: ['2 of Clubs', 1, 3],
    29: ['3 of Clubs', 2, 3],
    30: ['4 of Clubs', 3, 3],
    31: ['5 of Clubs', 4, 3],
    32: ['6 of Clubs', 5, 3],
    33: ['7 of Clubs', 6, 3],
    34: ['8 of Clubs', 7, 3],
    35: ['9 of Clubs', 8, 3],
    36: ['10 of Clubs', 9, 3],
    37: ['Jack of Clubs', 10, 3],
    38: ['Queen of Clubs', 11, 3],
    39: ['King of Clubs', 12, 3],
    40: ['Ace of Diamonds', 13, 4],
    41: ['2 of Diamonds', 1, 4],
    42: ['3 of Diamonds', 2, 4],
    43: ['4 of Diamonds', 3, 4],
    44: ['5 of Diamonds', 4, 4],
    45: ['6 of Diamonds', 5, 4],
    46: ['7 of Diamonds', 6, 4],
    47: ['8 of Diamonds', 7, 4],
    48: ['9 of Diamonds', 8, 4],
    49: ['10 of Diamonds', 9, 4],
    50: ['Jack of Diamonds', 10, 4],
    51: ['Queen of Diamonds', 11, 4],
    52: ['King of Diamonds', 12, 4],

}

 #function to set or reest containers
    
river = []
p1CARD = []
p2CARD = []



#function to generate p1 and p2 and river hands
def playerhand():

    random_numbers = []

    cards = CARDS.copy()
    for i in range(9):
        while True:
            random_number = random.randint(1, 52)
            if random_number not in random_numbers:
                break
        random_numbers.append(random_number)
        
    p1CARD1 = random_numbers[0]
    p1CARD2 = random_numbers[1]
    p1CARD.append(cards[p1CARD1])
    p1CARD.append(cards[p1CARD2])
    cards.pop(p1CARD1)
    cards.pop(p1CARD2)

    p2CARD1 = random_numbers[2]
    p2CARD2 = random_numbers[3]
    p2CARD.append(cards[p2CARD1])
    p2CARD.append(cards[p2CARD2])
    cards.pop(p2CARD1)
    cards.pop(p2CARD2)

    # Building the River
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


#helper function to build containers
def build_container(name, color):
    return ft.Container(
        content=ft.Text(name),
        bgcolor=color,
        padding=15,
    )

#helper function to build buttons
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

#main function
def app(page: ft.Page):

    playerhand()


    count_text = ft.TextField(value="0")

    #river
    r1 = build_container("", ft.colors.BLUE)
    r2 = build_container("", ft.colors.BLUE)
    r3 = build_container("", ft.colors.BLUE)
    r4 = build_container("", ft.colors.BLUE)
    r5 = build_container("", ft.colors.BLUE)

    #player cards
    p1 = build_container(p1CARD[0][0], ft.colors.BLUE)
    p2 = build_container(p1CARD[1][0], ft.colors.BLUE)
    p3 = build_container(p2CARD[0][0], ft.colors.BLUE)
    p4 = build_container(p2CARD[1][0], ft.colors.BLUE)

    #pot
    pot = build_container("0", ft.colors.BLACK)

    #p1 and p2 banks
    bank1 = build_container("100", ft.colors.GREEN)
    bank2 = build_container("100", ft.colors.GREEN)

    #p1 and p2 bet text input
    p1BET = ft.TextField(label="Bet")
    p2BET = ft.TextField(label="Bet")

    #p1CALL = build_button("CALL", ft.colors.YELLOW)
    #p2CALL = build_button("CALL", ft.colors.YELLOW)

    winner = build_container("", ft.colors.BLACK)


    #function to add to pot to pp1bank, clear pot, and say player one wins
    def p1WIN():
        winner.content.value = "Player One Wins"
        sum1 = int(pot.content.value)
        sum2 = int(bank1.content.value)
        sum3 = sum1 + sum2
        bank1.content.value = str(sum3)
        pot.content.value = "0"
        page.update()
        
    #function to add to pot to p2bank, clear pot, and say player one wins
    def p2WIN():
        winner.content.value = "Player Two Wins"
        sum1 = int(pot.content.value)
        sum2 = int(bank2.content.value)
        sum3 = sum1 + sum2
        bank2.content.value = str(sum3)
        pot.content.value = "0"
        page.update()

    #function to check for highcard 
    def highcard(p1pair, p2pair):
        p1MAX =  max(p1CARD[0][1], p1CARD[1][1])
        p2MAX =  max(p2CARD[0][1], p2CARD[1][1])
        
        ic(p1MAX)
        ic(p2MAX)

        p1MIN = min(p1CARD[0][1], p1CARD[1][1])
        p2MIN = min(p2CARD[0][1], p2CARD[1][1])

        ic(p1MIN)
        ic(p2MIN)
    

    
        if p1MAX == p2MAX:
            print("p1MAX == p2MAX:")
            if p1MIN > p2MIN:
                print("p1MIN > p2MIN:")
                print("player 1 highcard 1")
                p1WIN()
            else:
                print("p1MIN < p2MIN")
                print("player 2 highcard 2")
                p2WIN()
        elif p1MAX > p2MAX:
            print("p1MAX > p2MAX")
            print("player 1 highcard 3")
            p1WIN()
        else:
            print("p1MAX < p2MAX")
            print("player 2 highcard 4")
            p2WIN()
      
    #functions to check for pairs       
    def pair():
        
        #function to check for p1pair
        def p1pair():
            for i in river:
                if i[1] == p1CARD[0][1] or i[1] == p1CARD[1][1] or p1CARD[0][1] == p1CARD[1][1]:
                    return i 
            return None

        #function to check for p2pair    
        def p2pair():
            for i in river:
                if i[1] == p2CARD[0][1] or  i[1] == p2CARD[1][1] or p2CARD[0][1] == p2CARD[1][1]:    
                    return i 
            return None
                
        p1pair = p1pair()
        p2pair = p2pair()
        
        
        return p1pair, p2pair
           
    #function for when p1 bets
    def p1BET_BUTTON(e):
        sum1 = int(p1BET.value)
        sum2 = int(pot.content.value)
        sum3 = sum1 + sum2
        pot.content.value = str(sum3)
        sum4 = int(bank1.content.value)
        sum5 = sum4 - sum1
        bank1.content.value = str(sum5)
        page.update()
    
    #function for when p2 bets and to start checks to win
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


            (p1pair, p2pair) = pair() 
            if p1pair and p2pair:
                highcard(p1pair, p2pair)
            elif p1pair and not p2pair:
                print("p1 pair")
                p1WIN()
            elif not p1pair and p2pair:
                print("p2 pair ")
                p2WIN()
            elif not p1pair and not p2pair:
                print("no pair")
                highcard(p1pair, p2pair)


        page.update()
        
    #p1 and p2 bet buttons
    p1BET_BUTTON = build_button("BET", ft.colors.ORANGE, callbac=p1BET_BUTTON)
    p2BET_BUTTON = build_button("BET", ft.colors.ORANGE, callbac=p2BET_BUTTON)
    
    #layout
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

    #layout
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

    #layout
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

    #layout
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

    #layout
    river2 = ft.Container(
                content=ft.Row(
                    [
                        r4,
                        r5
                    ],
                alignment=ft.MainAxisAlignment.CENTER
                ),
            )

    #layout
    riverPOT = ft.Container(
                content=ft.Row(
                    [
                        pot,
                    ],
                alignment=ft.MainAxisAlignment.CENTER
                ),
            )

    #layouot
    winnerROW = ft.Container(
        content=ft.Row(
            [
                winner,
            ],
            alignment=ft.MainAxisAlignment.CENTER
            ),
        )

    #function to start game
    def start_button(e):
        #page.controls.pop()
        page.update()
        page.add(
            river3,
            river2,
            riverPOT,
            pColumns,
            winnerROW,
        )
    
    #function to restart game
    def restart_button(e):
        river.clear()
        p1CARD.clear()
        p2CARD.clear()
        playerhand()
        count_text.value = "0" 
        winner.content.value = ""
        r1.content.value = ""
        r2.content.value = ""
        r3.content.value = ""
        r4.content.value = ""
        r5.content.value = ""
        bank1.content.value = "100"
        bank2.content.value = "100"
        pot.content.value = "0"
        p1.content.value = p1CARD[0][0]
        p2.content.value = p1CARD[1][0]
        p3.content.value = p2CARD[0][0]
        p4.content.value = p2CARD[1][0]
        page.update()



    page.add(
        ft.FilledButton(
            "play", 
            on_click=start_button,
            style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30),
            ),
        
        ft.FilledButton(
            "reset",
            on_click=restart_button,
            style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30),
        )
        
    )

ft.app(target=app, view=ft.AppView.WEB_BROWSER)