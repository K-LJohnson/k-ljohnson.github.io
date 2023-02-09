import numpy as np
import random
import turtle as t




def destroyer_h(x, y):
    """Draws the horizontal cruiser for battleship"""
    t.penup()
    t.speed('fastest')
    t.goto(x + 7, y + 45)
    t.color('gray')
    t.begin_fill()
    t.forward(75)
    t.right(18)
    t.forward(6.7)
    t.right(18)
    t.forward(6.7)
    t.right(18)
    t.forward(6.7)
    t.right(18)
    t.forward(6.7)
    t.right(18)
    t.forward(6.7)
    t.right(18)
    t.forward(6.7)
    t.right(18)
    t.forward(6.7)
    t.right(18)
    t.forward(6.7)
    t.right(18)
    t.forward(6.7)
    t.right(18)
    t.forward(6.7)
    t.forward(75)
    t.right(90)
    t.forward(42)
    t.end_fill()
    t.right(90)


def destroyer_v(x, y):
    """Draws the vertical destroyer for battleship"""
    t.speed('fastest')
    t.penup()
    t.goto(x + 5, y + 5)
    t.left(90)
    t.color('gray')
    t.begin_fill()
    t.forward(75)
    t.right(18)
    t.forward(6.7)
    t.right(18)
    t.forward(6.7)
    t.right(18)
    t.forward(6.7)
    t.right(18)
    t.forward(6.7)
    t.right(18)
    t.forward(6.7)
    t.right(18)
    t.forward(6.7)
    t.right(18)
    t.forward(6.7)
    t.right(18)
    t.forward(6.7)
    t.right(18)
    t.forward(6.7)
    t.right(18)
    t.forward(6.7)
    t.forward(75)
    t.right(90)
    t.forward(42)
    t.end_fill()
    t.right(180)

# Aircraft Carrier

def aircraft_horiz(x, y):
    """Draws a horizontal aircraft carrier"""
    t.speed('fastest')
    t.color('gray')
    t.fillcolor('gray')
    t.penup()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    t.forward(250)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(250)
    t.left(90)
    t.forward(50)
    t.end_fill()
    t.left(90)



def aircraft_vert(x, y):
    """Draws a vertical aircraft carrier"""
    t.speed('fastest')
    t.color('gray')
    t.fillcolor('gray')
    t.penup()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    t.left(90)
    t.forward(250)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(50)
    t.right(180)
    t.end_fill()




def battleship_horiz(x, y):
    """Draws a horizontal battleship"""
    t.speed('fastest')
    t.color('gray')
    t.fillcolor('gray')
    t.penup()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    t.forward(200)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(50)
    t.end_fill()
    t.left(90)



def battleship_vert(x, y):
    """Draws a vertical battleship"""
    t.speed('fastest')
    t.color('gray')
    t.fillcolor('gray')
    t.penup()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    t.left(90)
    t.forward(200)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(50)
    t.right(180)
    t.end_fill()


# Submarine

def submarine_h(x, y):
    """Draws a horizontal submarine"""
    t.penup()
    t.speed("fastest")
    t.goto(x + 120, y)
    t.speed(1)
    t.pendown()
    t.color('gray')
    t.begin_fill()
    t.left(45)
    t.forward(20)
    t.left(45)
    t.forward(16)
    t.left(45)
    t.forward(20)
    t.left(45)
    t.forward(85)
    t.left(45)
    t.forward(20)
    t.left(45)
    t.forward(16)
    t.left(45)
    t.forward(20)
    t.left(45)
    t.forward(85)
    t.end_fill()

def submarine_v(x, y):
    """Draws a vertical submarine"""
    t.penup()
    t.speed("fastest")
    t.goto(x + 50, y + 130)
    t.speed(1)
    t.pendown()
    t.color('gray')
    t.begin_fill()
    t.left(90)
    t.left(45)
    t.forward(20)
    t.left(45)
    t.forward(16)
    t.left(45)
    t.forward(20)
    t.left(45)
    t.forward(85)
    t.left(45)
    t.forward(20)
    t.left(45)
    t.forward(16)
    t.left(45)
    t.forward(20)
    t.left(45)
    t.forward(85)
    t.right(90)
    t.end_fill()

# Cruiser

def cruiser_v(x, y):
    """Draws a vertical destroyer"""
    t.penup()
    t.speed("fastest")
    t.goto(x + 50, y + 100)
    t.speed(1)
    t.pendown()
    t.color('gray')
    t.begin_fill()
    t.left(90)
    t.left(45)
    t.forward(20)
    t.left(45)
    t.forward(16)
    t.left(45)
    t.forward(20)
    t.left(45)
    t.forward(100)
    t.left(90)
    t.forward(45)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.end_fill()


def cruiser_h(x, y):
    """Draws a horizontal destroyer"""
    t.speed("fastest")
    t.penup()
    t.goto(x + 100, y + 3)
    t.speed(1)
    t.pendown()
    t.color('gray')
    t.begin_fill()
    t.left(45)
    t.forward(20)
    t.left(45)
    t.forward(16)
    t.left(45)
    t.forward(20)
    t.left(45)
    t.forward(100)
    t.left(90)
    t.forward(45)
    t.left(90)
    t.forward(100)
    t.end_fill()


def hit(x, y):
    """Indicates when a ship has taken a hit with a red square"""
    t.penup()
    t.speed('fastest')
    t.goto(x, y + 50)
    t.color('red')
    t.begin_fill()
    t.pendown()
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.end_fill()
    t.right(90)


def miss(x, y):
    """Indicates when a ship has been missed with a white square"""
    t.penup()
    t.speed('fastest')
    t.goto(x, y + 50)
    t.color('white')
    t.begin_fill()
    t.pendown()
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.end_fill()
    t.right(90)


# Board for the player's ships:

# Create the headers:

def board():
    """This creates the battleship board."""
    t.hideturtle()
    t.bgcolor("cyan")
    t.color("black")
    t.speed("fastest")
    t.up()
    t.setpos(-650, 350)
    t.write("Your Ships", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-650, 300)
    t.write(" 1    2    3    4   5    6    7    8    9   10", True, align="left", font=("Arial", 30, "normal")) #the spacing changes for running turtle on Mac
    t.setpos(-680, 250)
    t.write("A", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-680, 200)
    t.write("B", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-680, 150)
    t.write("C", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-680, 100)
    t.write("D", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-680, 50)
    t.write("E", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-680, 0)
    t.write("F", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-680, -50)
    t.write("G", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-680, -100)
    t.write("H", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-680, -150)
    t.write("I", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-680, -200)
    t.write("J", True, align="left", font=("Arial", 30, "normal"))

    # Creates the boxes.
    i = 0
    j = 0
    y = t.pos()
    t.setpos(-650, 300)
    t.down()

    while j < 10:
        while i < 11:
            t.down()
            t.forward(50)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.goto(-650 + i*50, 300 - j*50)
            t.up()
            i += 1

        t.setpos(-650, 300 - j*50)
        j += 1
        i = 0


    # Build a second board.

    t.setpos(0, 350)
    t.write("Your Guesses", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(0, 300)
    t.write(" 1    2    3    4   5    6    7    8    9   10", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-35, 250)
    t.write("A", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-35, 200)
    t.write("B", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-35, 150)
    t.write("C", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-35, 100)
    t.write("D", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-35, 50)
    t.write("E", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-35, 0)
    t.write("F", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-35, -50)
    t.write("G ", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-35, -100)
    t.write("H", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-35, -150)
    t.write("I", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-35, -200)
    t.write("J", True, align="left", font=("Arial", 30, "normal"))

    # Creates the boxes.
    k = 0
    l = 0
    y = t.pos()
    t.setpos(0, 300)
    t.down()

    while k < 10:
        while l < 11:
            t.down()
            t.forward(50)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.goto(0 + l*50, 300 - k*50)
            t.up()
            l += 1

        t.setpos(0, 300 - k*50)
        k += 1
        l = 0

def board_playerships(name):
    """This creates the battleship board for each player to place their ships."""
    t.hideturtle()
    t.bgcolor("cyan")
    t.color("black")
    t.speed("fastest")
    t.up()
    t.setpos(-650, 350)
    t.write(name+"'s ships", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-650, 300)
    t.write(" 1    2    3    4   5    6    7    8    9   10", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-680, 250)
    t.write("A", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-680, 200)
    t.write("B", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-680, 150)
    t.write("C", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-680, 100)
    t.write("D", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-680, 50)
    t.write("E", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-680, 0)
    t.write("F", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-680, -50)
    t.write("G", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-680, -100)
    t.write("H", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-680, -150)
    t.write("I", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-680, -200)
    t.write("J", True, align="left", font=("Arial", 30, "normal"))

    # Creates the boxes.
    i = 0
    j = 0
    y = t.pos()
    t.setpos(-650, 300)
    t.down()

    while j < 10:
        while i < 11:
            t.down()
            t.forward(50)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.goto(-650 + i*50, 300 - j*50)
            t.up()
            i += 1

        t.setpos(-650, 300 - j*50)
        j += 1
        i = 0

def board_shots(name1, name2):
    """This creates the battleship boards for 2 players to see where they have hit the other"""
    t.hideturtle()
    t.bgcolor("cyan")
    t.color("black")
    t.speed("fastest")
    t.up()
    t.setpos(-650, 350)
    t.write(name1+"'s shots", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-650, 300)
    t.write(" 1    2    3    4   5    6    7    8    9   10", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-680, 250)
    t.write("A", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-680, 200)
    t.write("B", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-680, 150)
    t.write("C", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-680, 100)
    t.write("D", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-680, 50)
    t.write("E", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-680, 0)
    t.write("F", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-680, -50)
    t.write("G", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-680, -100)
    t.write("H", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-680, -150)
    t.write("I", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-680, -200)
    t.write("J", True, align="left", font=("Arial", 30, "normal"))

    # Creates the boxes.
    i = 0
    j = 0
    y = t.pos()
    t.setpos(-650, 300)
    t.down()

    while j < 10:
        while i < 11:
            t.down()
            t.forward(50)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.goto(-650 + i*50, 300 - j*50)
            t.up()
            i += 1

        t.setpos(-650, 300 - j*50)
        j += 1
        i = 0


    # Build a second board.

    t.setpos(0, 350)
    t.write(name2+"'s shots", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(0, 300)
    t.write(" 1    2    3    4   5    6    7    8    9   10", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-35, 250)
    t.write("A", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-35, 200)
    t.write("B", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-35, 150)
    t.write("C", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-35, 100)
    t.write("D", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-35, 50)
    t.write("E", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-35, 0)
    t.write("F", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-35, -50)
    t.write("G ", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-35, -100)
    t.write("H", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-35, -150)
    t.write("I", True, align="left", font=("Arial", 30, "normal"))
    t.setpos(-35, -200)
    t.write("J", True, align="left", font=("Arial", 30, "normal"))

    # Creates the boxes.
    k = 0
    l = 0
    y = t.pos()
    t.setpos(0, 300)
    t.down()

    while k < 10:
        while l < 11:
            t.down()
            t.forward(50)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.goto(0 + l*50, 300 - k*50)
            t.up()
            l += 1

        t.setpos(0, 300 - k*50)
        k += 1
        l = 0

print("Howdy! Welcome to Python Battleship!")

# Choose the opponent.

game_type = input("To play against the computer, enter 1. To play against another player, enter 2:")

while game_type != '1' and game_type != '2':
    if game_type != '1' or game_type != '2':
        print('\n', "Oops! Something went wrong. Please try again.")

    game_type = input("To play against the computer, enter 1. To play against another player, enter 2:")

    # For Playing with a Computer

if game_type == '1':
    player1 = input("Please enter your name:")
    player2 = 'Computer'
    print("All set! Let's go!")
    # Y Values
    col1 = [250, 200, 150, 100, 50, 0, -50, -100, -150, -200]
    col2 = [250, 200, 150, 100, 50, 0, -50, -100, -150, -200]
    col3 = [250, 200, 150, 100, 50, 0, -50, -100, -150, -200]
    col4 = [250, 200, 150, 100, 50, 0, -50, -100, -150, -200]
    col5 = [250, 200, 150, 100, 50, 0, -50, -100, -150, -200]
    col6 = [250, 200, 150, 100, 50, 0, -50, -100, -150, -200]
    col7 = [250, 200, 150, 100, 50, 0, -50, -100, -150, -200]
    col8 = [250, 200, 150, 100, 50, 0, -50, -100, -150, -200]
    col9 = [250, 200, 150, 100, 50, 0, -50, -100, -150, -200]
    col10 = [250, 200, 150, 100, 50, 0, -50, -100, -150, -200]
    col = [col1, col2, col3, col4, col5, col6, col7, col8, col9, col10]
    letter_val = 0
    print("Please wait. We are travelling to the Python Sea...")
    print("Make sure to maximize your turtle screen while the board is loading, you won't be able to do it later!")
    board()

    # Verifies user input.

    print("Time to place your ships! Make sure to enter your coordinates with lowercase letters and no spaces \n "
          "(Enter 'a1' to place a ship at square A1, do not enter the number first (1a) your game will end) \n "
          "* Please note that the box you enter will be occupied by the back left corner of the ship*")
    board_entity = []
    board2_entity = []
    for i in range(10):
        board2_entity.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    for i in range(10):
        board_entity.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    board_empty = []
    for i in range(10):
        board_empty.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


    def cdestroyer_placement(board_entity):
        """Code for the computer's destroyer placement. Used for hit registration."""
        destori = random.randint(0, 1)
        if destori == 0:
            row = random.randint(0, 9)
            column = random.randint(0, 8)
            board_entity[row][column] = 1
            board_entity[row][column + 1] = 1
        if destori == 1:
            row = random.randint(1, 9)
            column = random.randint(0, 9)
            board_entity[row][column] = 1
            board_entity[row - 1][column] = 1
        return (board_entity)



    board_entity = cdestroyer_placement(board_entity)


    def ccruiser_placement(board_entity):
        """Code for the computer's cruiser placement. Used for hit registration."""
        cruiserori = random.randint(0, 1)
        if cruiserori == 0:
            row = random.randint(0, 9)
            column = random.randint(0, 7)
            while True:
                if board_entity[row][column] or board_entity[row][column + 1] or board_entity[row][column + 2] == 1:
                    row = random.randint(0, 9)
                    column = random.randint(0, 7)
                else:
                    break
            board_entity[row][column] = 1
            board_entity[row][column + 1] = 1
            board_entity[row][column + 2] = 1
        if cruiserori == 1:
            row = random.randint(2, 9)
            column = random.randint(0, 9)
            while True:
                if board_entity[row][column] or board_entity[row - 1][column] or board_entity[row - 2][column] == 1:
                    row = random.randint(2, 9)
                    column = random.randint(0, 9)
                else:
                    break
            board_entity[row][column] = 1
            board_entity[row - 1][column] = 1
            board_entity[row - 2][column] = 1
        return (board_entity)


    board_entity = ccruiser_placement(board_entity)


    def csubmarine_placement(board_entity):
        """Code for the computer's submarine placement. Used for hit registration."""
        submarineori = random.randint(0, 1)
        if submarineori == 0:
            row = random.randint(0, 9)
            column = random.randint(0, 7)
            while True:
                if board_entity[row][column] or board_entity[row][column + 1] or board_entity[row][column + 2] == 1:
                    row = random.randint(0, 9)
                    column = random.randint(0, 7)
                else:
                    break
            board_entity[row][column] = 1
            board_entity[row][column + 1] = 1
            board_entity[row][column + 2] = 1
        if submarineori == 1:
            row = random.randint(2, 9)
            column = random.randint(0, 9)
            while True:
                if board_entity[row][column] or board_entity[row - 1][column] or board_entity[row - 2][column] == 1:
                    row = random.randint(2, 9)
                    column = random.randint(0, 9)
                else:
                    break
            board_entity[row][column] = 1
            board_entity[row - 1][column] = 1
            board_entity[row - 2][column] = 1
        return (board_entity)


    board_entity = csubmarine_placement(board_entity)


    def cbattleship_placement(board_entity):
        """Code for the computer's battleship placement. Used for hit registration."""
        battleshipori = random.randint(0, 1)
        if battleshipori == 0:
            row = random.randint(0, 9)
            column = random.randint(0, 6)
            while True:
                if board_entity[row][column] or board_entity[row][column + 1] or board_entity[row][column + 2] or \
                        board_entity[row][column + 3] == 1:
                    row = random.randint(0, 9)
                    column = random.randint(0, 6)
                else:
                    break
            board_entity[row][column] = 1
            board_entity[row][column + 1] = 1
            board_entity[row][column + 2] = 1
            board_entity[row][column + 3] = 1
        if battleshipori == 1:
            row = random.randint(3, 9)
            column = random.randint(0, 9)
            while True:
                if board_entity[row][column] or board_entity[row - 1][column] or board_entity[row - 2][column] or \
                        board_entity[row - 3][column] == 1:
                    row = random.randint(3, 9)
                    column = random.randint(0, 9)
                else:
                    break
            board_entity[row][column] = 1
            board_entity[row - 1][column] = 1
            board_entity[row - 2][column] = 1
            board_entity[row - 3][column] = 1
        return (board_entity)


    board_entity = cbattleship_placement(board_entity)


    def ccarrier_placement(board_entity):
        """Code for the computer's carrier placement. Used for hit registration."""
        carrierori = random.randint(0, 1)
        if carrierori == 0:
            row = random.randint(0, 9)
            column = random.randint(0, 5)
            while True:
                if board_entity[row][column] or board_entity[row][column + 1] or board_entity[row][column + 2] or \
                        board_entity[row][column + 3] or board_entity[row][column + 4] == 1:
                    row = random.randint(0, 9)
                    column = random.randint(0, 5)
                else:
                    break
            board_entity[row][column] = 1
            board_entity[row][column + 1] = 1
            board_entity[row][column + 2] = 1
            board_entity[row][column + 3] = 1
            board_entity[row][column + 4] = 1
        if carrierori == 1:
            row = random.randint(4, 9)
            column = random.randint(0, 9)
            while True:
                if board_entity[row][column] or board_entity[row - 1][column] or board_entity[row - 2][column] or \
                        board_entity[row - 3][column] or board_entity[row - 4][column] == 1:
                    row = random.randint(4, 9)
                    column = random.randint(0, 9)
                else:
                    break
            board_entity[row][column] = 1
            board_entity[row - 1][column] = 1
            board_entity[row - 2][column] = 1
            board_entity[row - 3][column] = 1
            board_entity[row - 4][column] = 1
        return (board_entity)


    board_entity = ccarrier_placement(board_entity)
    board = np.array(board_entity)


    ###############################################################################################################

    def rowc_converter(row, column):
        """Converts user input for letter rows to a number that the computer can use to call an x value"""
        if row == 'a':
            row = 0
        if row == 'b':
            row = 1
        if row == 'c':
            row = 2
        if row == 'd':
            row = 3
        if row == 'e':
            row = 4
        if row == 'f':
            row = 5
        if row == 'g':
            row = 6
        if row == 'h':
            row = 7
        if row == 'i':
            row = 8
        if row == 'j':
            row = 9
        column = int(column) - 1
        return (row, column)


    # places the destroyer

    def destroyer_placement(board2_entity):
        """Code function for the player's destroyer placement. Used in hit registration."""
        orientation = ''
        while orientation != 'v' and orientation != 'h':
            try:
                orientation = input(
                    "What orientation do you want the destroyer in? (type h for horizontal and v for vertical):")
                if orientation == 'h' or orientation == 'v':
                    break
                else:
                    orientation = 17/0
            except:
                print("Oops! Invalid input. Please try again.")

        # tests for placements that put ships out of bounds or overlaps with another ship- overlap test not needed for destroyer bc it is the first ship placed
        row = 0
        column = 9
        if orientation == 'h':
            while column == 9:
                try:
                    destpos = input("What box do you want to place the destroyer (2 spaces long) in?")
                    row = destpos[0]
                    if row == 'a' or row == 'b' or row == 'c' or row == 'd' or row == 'e' or row == 'f' or row == 'g' or row =='h' or row == 'i' or row == 'j':
                        column = destpos[1:]
                        row, column = rowc_converter(row, column)
                        board2_entity[row][column] = 1
                        board2_entity[row][column + 1] = 1
                        break

                    else:
                        row = 17 / 0
                        column = destpos[1:]
                        row, column = rowc_converter(row, column)
                        board2_entity[row][column] = 1
                        board2_entity[row][column + 1] = 1

                except:
                    print('Invalid starting location- check for out of bound placement or capitalization.')


        elif orientation == 'v':

            while row == 0:
                try:
                    destpos = input("What box do you want to place the destroyer (2 spaces long) in?")
                    row = destpos[0]
                    if row == 'a' or row == 'b' or row == 'c' or row == 'd' or row == 'e' or row == 'f' or row == 'g' or row =='h' or row == 'i' or row == 'j':
                        column = destpos[1:]
                        row, column = rowc_converter(row, column)
                        board2_entity[row][column] = 1
                        board2_entity[row -1][column] = 1
                        break

                    else:
                        row = 17 / 0
                        column = destpos[1:]
                        row, column = rowc_converter(row, column)
                        board2_entity[row][column] = 1
                        board2_entity[row - 1][column] = 1

                except:
                    print('Invalid starting location- check for out of bound placement or capitalization.')


        # Determines coordinates for ship placement.
        if column == 0:
            y = col1[row]
            x = -650
            t.update()
            t.penup()
            if orientation == "h":
                destroyer_h(x, y)

            elif orientation == "v":
                destroyer_v(x, y)


        elif column == 1:
            y = col2[row]
            x = -600
            t.update()
            t.penup()
            if orientation == "h":
                destroyer_h(x, y)

            elif orientation == "v":
                destroyer_v(x, y)


        elif column == 2:
            y = col3[row]
            x = -550
            t.update()
            t.penup()
            if orientation == "h":
                destroyer_h(x, y)

            elif orientation == "v":
                destroyer_v(x, y)

        elif column == 3:
            y = col4[row]
            x = -500
            t.update()
            t.penup()
            if orientation == "h":
                destroyer_h(x, y)

            elif orientation == "v":
                destroyer_v(x, y)


        elif column == 4:
            y = col5[row]
            x = -450
            t.update()
            t.penup()
            if orientation == "h":
                destroyer_h(x, y)

            elif orientation == "v":
                destroyer_v(x, y)


        elif column == 5:
            y = col6[row]
            x = -400
            t.update()
            t.penup()
            if orientation == "h":
                destroyer_h(x, y)

            elif orientation == "v":
                destroyer_v(x, y)


        elif column == 6:
            y = col7[row]
            x = -350
            t.update()
            t.penup()
            if orientation == "h":
                destroyer_h(x, y)

            elif orientation == "v":
                destroyer_v(x, y)


        elif column == 7:
            y = col8[row]
            x = -300
            t.update()
            t.penup()
            if orientation == "h":
                destroyer_h(x, y)

            elif orientation == "v":
                destroyer_v(x, y)

        elif column == 8:
            y = col9[row]
            x = -250
            t.update()
            t.penup()
            if orientation == "h":
                destroyer_h(x, y)

            elif orientation == "v":
                destroyer_v(x, y)


        elif column == 9:
            y = col10[row]
            x = -200
            t.update()
            t.penup()
            if orientation == "h":
                destroyer_h(x, y)

            elif orientation == "v":
                destroyer_v(x, y)
        return (board2_entity)


    board2_entity = destroyer_placement(board2_entity)


    def cruiser_placement(board2_entity):
        """Code for the computer's cruiser placement. Used for hit registration."""
        orientation = ''
        while orientation != 'v' and orientation != 'h':
            try:
                orientation = input(
                    "What orientation do you want the cruiser in? (type h for horizontal and v for vertical):")
                if orientation == 'h' or orientation == 'v':
                    break
                else:
                    orientation = 17 / 0
            except:
                print("Oops! Invalid input. Please try again.")

        row = 0
        column = 9
        # test for placements that put ships out of bounds
        if orientation == 'v':
            while row == 0 or row == 1:
                try:
                    cruiserpos = input("What box do you want to place the cruiser (3 spaces long) in?")

                    row = cruiserpos[0]
                    column = cruiserpos[1:]
                    row, column = rowc_converter(row, column) #cruiser begins including the test for overlapping ships
                    if row == 0 or row == 1 or board2_entity[row][column] == 1 or  board2_entity[row - 1][column] == 1 or board2_entity[row - 2][column] == 1:
                        row = row / 17  # force an error if there is already a ship placed in the box entered or its out of bounds
                        board2_entity[row][column] = 1
                        board2_entity[row - 1][column] = 1
                        board2_entity[row - 2][column] = 1
                    else:
                        row = row
                        board2_entity[row][column] = 1
                        board2_entity[row - 1][column] = 1
                        board2_entity[row - 2][column] = 1
                        break
                except:
                    print('Invalid starting location- check for overlap or out of bound placement.')
                    row = 0
        if orientation == 'h':
            while column == 9 or 8:
                try:
                    cruiserpos = input("What box do you want to place the cruiser (3 spaces long) in?")

                    row = cruiserpos[0]
                    column = cruiserpos[1:]
                    row, column = rowc_converter(row, column)
                    if board2_entity[row][column] == 1 or board2_entity[row][column + 1] == 1 or board2_entity[row][column + 2] == 1:
                        row = row / 17  # force an error if there is already a ship placed in the box entered
                        board2_entity[row][column] = 1
                        board2_entity[row][column + 1] = 1
                        board2_entity[row][column + 2] = 1
                    if column != 8 or column != 9:
                        board2_entity[row][column] = 1
                        board2_entity[row][column + 1] = 1
                        board2_entity[row][column + 2] = 1
                        break
                except:
                    print('Invalid starting location- check for overlap or out of bound placement.')




        if column == 0:
            y = col1[row]
            x = -650
            t.update()
            t.penup()
            if orientation == "h":
                cruiser_h(x, y)

            elif orientation == "v":
                cruiser_v(x, y)


        elif column == 1:
            y = col2[row]
            x = -600
            t.update()
            t.penup()
            if orientation == "h":
                cruiser_h(x, y)

            elif orientation == "v":
                cruiser_v(x, y)



        elif column == 2:
            y = col3[row]
            x = -550
            t.update()
            t.penup()
            if orientation == "h":
                cruiser_h(x, y)

            elif orientation == "v":
                cruiser_v(x, y)


        elif column == 3:
            y = col4[row]
            x = -500
            t.update()
            t.penup()
            if orientation == "h":
                cruiser_h(x, y)

            elif orientation == "v":
                cruiser_v(x, y)


        elif column == 4:
            y = col5[row]
            x = -450
            t.update()
            t.penup()
            if orientation == "h":
                cruiser_h(x, y)

            elif orientation == "v":
                cruiser_v(x, y)



        elif column == 5:
            y = col6[row]
            x = -400
            t.update()
            t.penup()
            if orientation == "h":
                cruiser_h(x, y)

            elif orientation == "v":
                cruiser_v(x, y)


        elif column == 6:
            y = col7[row]
            x = -350
            t.update()
            t.penup()
            if orientation == "h":
                cruiser_h(x, y)

            elif orientation == "v":
                cruiser_v(x, y)



        elif column == 7:
            y = col8[row]
            x = -300
            t.update()
            t.penup()
            if orientation == "h":
                cruiser_h(x, y)

            elif orientation == "v":
                cruiser_v(x, y)

        elif column == 8:
            y = col9[row]
            x = -250
            t.update()
            t.penup()
            if orientation == "h":
                cruiser_h(x, y)

            elif orientation == "v":
                cruiser_v(x, y)



        elif column == 9:
            y = col10[row]
            x = -200
            t.update()
            t.penup()
            if orientation == "h":
                cruiser_h(x, y)

            elif orientation == "v":
                cruiser_v(x, y)
        return (board2_entity)


    board2_entity = cruiser_placement(board2_entity)


    def submarine_placement(board2_entity):
        """Code for the computer's submarine placement. Used for hit registration."""
        orientation = ''
        while orientation != 'v' and orientation != 'h':
            try:
                orientation = input(
                    "What orientation do you want the submarine in? (type h for horizontal and v for vertical):")
                if orientation == 'h' or orientation == 'v':
                    break
                else:
                    orientation = 17 / 0
            except:
                print("Oops! Invalid input. Please try again.")

        # test for placements that put ships out of bounds
        row = 0
        column = 9
        if orientation == 'v':
            while row == 0 or row == 1:
                try:
                    submarinepos = input("What box do you want to place the submarine (3 spaces long) in?")

                    row = submarinepos[0]
                    column = submarinepos[1:]
                    row, column = rowc_converter(row, column)
                    if row == 0 or row == 1 or board2_entity[row][column] == 1 or board2_entity[row - 1][column] == 1 or board2_entity[row - 2][column] == 1:
                        row = row / 17  # force an error if there is already a ship placed in the box entered or its out of bounds
                        board2_entity[row][column] = 1
                        board2_entity[row - 1][column] = 1
                        board2_entity[row - 2][column] = 1
                    else:
                        row = row
                        board2_entity[row][column] = 1
                        board2_entity[row - 1][column] = 1
                        board2_entity[row - 2][column] = 1
                        break

                except:
                    print('Invalid starting location.')
                    row = 0
        if orientation == 'h':
            while column == 9 or 8:
                try:
                    cruiserpos = input("What box do you want to place the submarine (3 spaces long) in?")

                    row = cruiserpos[0]
                    column = cruiserpos[1:]
                    row, column = rowc_converter(row, column)
                    if board2_entity[row][column] == 1 or board2_entity[row][column + 1] == 1 or board2_entity[row][column + 2] == 1:
                        row = row / 17  # force an error if there is already a ship placed in the box entered
                        board2_entity[row][column] = 1
                        board2_entity[row][column + 1] = 1
                        board2_entity[row][column + 2] = 1
                    if column != 8 or column != 9:
                        board2_entity[row][column] = 1
                        board2_entity[row][column + 1] = 1
                        board2_entity[row][column + 2] = 1
                        break
                except:
                    print('Invalid starting location- check for overlap or out of bound placement.')




        if column == 0:
            y = col1[row]
            x = -650
            t.update()
            t.penup()
            if orientation == "h":
                submarine_h(x, y)

            elif orientation == "v":
                submarine_v(x, y)


        elif column == 1:
            y = col2[row]
            x = -600
            t.update()
            t.penup()
            if orientation == "h":
                submarine_h(x, y)

            elif orientation == "v":
                submarine_v(x, y)

        elif column == 2:
            y = col3[row]
            x = -550
            t.update()
            t.penup()
            if orientation == "h":
                submarine_h(x, y)

            elif orientation == "v":
                submarine_v(x, y)

        elif column == 3:
            y = col4[row]
            x = -500
            t.update()
            t.penup()
            if orientation == "h":
                submarine_h(x, y)

            elif orientation == "v":
                submarine_v(x, y)


        elif column == 4:
            y = col5[row]
            x = -450
            t.update()
            t.penup()
            if orientation == "h":
                submarine_h(x, y)

            elif orientation == "v":
                submarine_v(x, y)

        elif column == 5:
            y = col6[row]
            x = -400
            t.update()
            t.penup()
            if orientation == "h":
                submarine_h(x, y)

            elif orientation == "v":
                submarine_v(x, y)

        elif column == 6:
            y = col7[row]
            x = -350
            t.update()
            t.penup()
            if orientation == "h":
                submarine_h(x, y)

            elif orientation == "v":
                submarine_v(x, y)

        elif column == 7:
            y = col8[row]
            x = -300
            t.update()
            t.penup()
            if orientation == "h":
                submarine_h(x, y)

            elif orientation == "v":
                submarine_v(x, y)

        elif column == 8:
            y = col9[row]
            x = -250
            t.update()
            t.penup()
            if orientation == "h":
                submarine_h(x, y)

            elif orientation == "v":
                submarine_v(x, y)


        elif column == 9:
            y = col10[row]
            x = -200
            t.update()
            t.penup()
            if orientation == "h":
                submarine_h(x, y)

            elif orientation == "v":
                submarine_v(x, y)
        return (board2_entity)


    board2_entity = submarine_placement(board2_entity)


    def battleship_placement(board2_entity):
        """Code for the computer's battleship placement. Used for hit registration."""
        orientation = ''
        while orientation != 'v' and orientation != 'h':
            try:
                orientation = input(
                    "What orientation do you want the battleship in? (type h for horizontal and v for vertical):")
                if orientation == 'h' or orientation == 'v':
                    break
                else:
                    orientation = 17 / 0
            except:
                print("Oops! Invalid input. Please try again.")
        # test for placements that put ships out of bounds
        row = 0
        column = 9
        if orientation == 'v':
            while row == 0 or row == 1 or row == 2:
                try:
                    battleshippos = input(
                        "What box do you want to place the battleship (4 spaces long) in?")

                    row = battleshippos[0]
                    column = battleshippos[1:]
                    row, column = rowc_converter(row, column)
                    if row == 0 or row == 1 or row == 2 or board2_entity[row][column] == 1 or board2_entity[row - 1][column] == 1 or  board2_entity[row - 2][column] == 1 or board2_entity[row - 3][column] == 1 :
                        row = row / 17  # force an error if there is already a ship placed in the box entered or its out of bounds
                        board2_entity[row][column] = 1
                        board2_entity[row - 1][column] = 1
                        board2_entity[row - 2][column] = 1
                        board2_entity[row - 3][column] = 1
                    else:
                        row = row
                        board2_entity[row][column] = 1
                        board2_entity[row - 1][column] = 1
                        board2_entity[row - 2][column] = 1
                        board2_entity[row - 3][column] = 1
                        break
                except:
                    print('Invalid starting location- check for overlap or out of bound placement.')
                    row = 0
        if orientation == 'h':
            while column == 9 or 8 or 7:
                try:
                    battleshippos = input(
                        "What box do you want to place the battleship (4 spaces long) in?")

                    row = battleshippos[0]
                    column = battleshippos[1:]
                    row, column = rowc_converter(row, column)
                    if board2_entity[row][column] == 1 or board2_entity[row][column + 1] == 1 or board2_entity[row][column + 2] == 1 or board2_entity[row][column + 3] == 1:
                        row = row / 17  # force an error if there is already a ship placed in the box entered
                        board2_entity[row][column] = 1
                        board2_entity[row][column + 1] = 1
                        board2_entity[row][column + 2] = 1
                        board2_entity[row][column + 3] = 1
                    if column != 7 or 8 or 9:
                        board2_entity[row][column] = 1
                        board2_entity[row][column + 1] = 1
                        board2_entity[row][column + 2] = 1
                        board2_entity[row][column + 3] = 1
                        break
                except:
                    print('Invalid starting location- check for overlap or out of bound placement.')




        if column == 0:
            y = col1[row]
            x = -650
            t.update()
            t.penup()
            if orientation == "h":
                battleship_horiz(x, y)

            elif orientation == "v":
                battleship_vert(x, y)


        elif column == 1:
            y = col2[row]
            x = -600
            t.update()
            t.penup()
            if orientation == "h":
                battleship_horiz(x, y)

            elif orientation == "v":
                battleship_vert(x, y)

        elif column == 2:
            y = col3[row]
            x = -550
            t.update()
            t.penup()
            if orientation == "h":
                battleship_horiz(x, y)

            elif orientation == "v":
                battleship_vert(x, y)

        elif column == 3:
            y = col4[row]
            x = -500
            t.update()
            t.penup()
            if orientation == "h":
                battleship_horiz(x, y)

            elif orientation == "v":
                battleship_vert(x, y)


        elif column == 4:
            y = col5[row]
            x = -450
            t.update()
            t.penup()
            if orientation == "h":
                battleship_horiz(x, y)

            elif orientation == "v":
                battleship_vert(x, y)

        elif column == 5:
            y = col6[row]
            x = -400
            t.update()
            t.penup()
            if orientation == "h":
                battleship_horiz(x, y)

            elif orientation == "v":
                battleship_vert(x, y)

        elif column == 6:
            y = col7[row]
            x = -350
            t.update()
            t.penup()
            if orientation == "h":
                battleship_horiz(x, y)

            elif orientation == "v":
                battleship_vert(x, y)

        elif column == 7:
            y = col8[row]
            x = -300
            t.update()
            t.penup()
            if orientation == "h":
                battleship_horiz(x, y)

            elif orientation == "v":
                battleship_vert(x, y)

        elif column == 8:
            y = col9[row]
            x = -250
            t.update()
            t.penup()
            if orientation == "h":
                battleship_horiz(x, y)

            elif orientation == "v":
                battleship_vert(x, y)


        elif column == 9:
            y = col10[row]
            x = -200
            t.update()
            t.penup()
            if orientation == "h":
                battleship_horiz(x, y)

            elif orientation == "v":
                battleship_vert(x, y)
        return (board2_entity)


    board2_entity = battleship_placement(board2_entity)


    def carrier_placement(board2_entity):
        """Code for the computer's carrier placement. Used for hit registration."""
        orientation = ''
        while orientation != 'v' and orientation != 'h':
            try:
                orientation = input(
                    "What orientation do you want the aircraft carrier in? (type h for horizontal and v for vertical):")
                if orientation == 'h' or orientation == 'v':
                    break
                else:
                    orientation = 17 / 0
            except:
                print("Oops! Invalid input. Please try again.")

        #test for placements that put ships out of bounds
        row = 0
        column = 9
        if orientation == 'v':
            while row == 0 or row == 1 or row == 2 or row == 3:
                try:
                    carrierpos = input(
                        "What box do you want to place the carrier (5 spaces long) in?")

                    row = carrierpos[0]
                    column = carrierpos[1:]
                    row, column = rowc_converter(row, column)
                    if row == 0 or row == 1 or row == 2 or row == 3 or board2_entity[row][column] == 1 or board2_entity[row - 1][column] == 1 or board2_entity[row - 2][column] == 1 or board2_entity[row - 3][column] == 1 or board2_entity[row - 4][column] == 1:
                        row = row / 17  # force an error if there is already a ship placed in the box entered or if its out of bounds
                        board2_entity[row][column] = 1
                        board2_entity[row - 1][column] = 1
                        board2_entity[row - 2][column] = 1
                        board2_entity[row - 3][column] = 1
                        board2_entity[row - 4][column] = 1
                    else:
                        row = row
                        board2_entity[row][column] = 1
                        board2_entity[row - 1][column] = 1
                        board2_entity[row - 2][column] = 1
                        board2_entity[row - 3][column] = 1
                        board2_entity[row - 4][column] = 1
                        break
                except:
                    print('Invalid starting location- check for overlap or out of bound placement.')
                    row = 0
        if orientation == 'h':
            while column == 9 or 8 or 7 or 6:
                try:
                    carrierpos = input(
                        "What box do you want to place the carrier (5 spaces long) in?")

                    row = carrierpos[0]
                    column = carrierpos[1:]
                    row, column = rowc_converter(row, column)
                    if board2_entity[row][column] == 1 or board2_entity[row][column + 1] == 1 or board2_entity[row][column + 2] == 1 or  board2_entity[row][column + 3] == 1 or board2_entity[row][column + 4] == 1:
                        row = row / 17  # force an error if there is already a ship placed in the box entered
                        board2_entity[row][column] = 1
                        board2_entity[row][column + 1] = 1
                        board2_entity[row][column + 2] = 1
                        board2_entity[row][column + 3] = 1
                        board2_entity[row][column + 4] = 1
                    if column != 9 or 8 or 7 or 6:
                        board2_entity[row][column] = 1
                        board2_entity[row][column + 1] = 1
                        board2_entity[row][column + 2] = 1
                        board2_entity[row][column + 3] = 1
                        board2_entity[row][column + 4] = 1
                        break
                except:
                    print('Invalid starting location- check for overlap or out of bound placement.')






        if column == 0:
            y = col1[row]
            x = -650
            t.update()
            t.penup()
            if orientation == "h":
                aircraft_horiz(x, y)

            elif orientation == "v":
                aircraft_vert(x, y)


        elif column == 1:
            y = col2[row]
            x = -600
            t.update()
            t.penup()
            if orientation == "h":
                aircraft_horiz(x, y)

            elif orientation == "v":
                aircraft_vert(x, y)

        elif column == 2:
            y = col3[row]
            x = -550
            t.update()
            t.penup()
            if orientation == "h":
                aircraft_horiz(x, y)

            elif orientation == "v":
                aircraft_vert(x, y)

        elif column == 3:
            y = col4[row]
            x = -500
            t.update()
            t.penup()
            if orientation == "h":
                aircraft_horiz(x, y)

            elif orientation == "v":
                aircraft_vert(x, y)


        elif column == 4:
            y = col5[row]
            x = -450
            t.update()
            t.penup()
            if orientation == "h":
                aircraft_horiz(x, y)

            elif orientation == "v":
                aircraft_vert(x, y)

        elif column == 5:
            y = col6[row]
            x = -400
            t.update()
            t.penup()
            if orientation == "h":
                aircraft_horiz(x, y)

            elif orientation == "v":
                aircraft_vert(x, y)

        elif column == 6:
            y = col7[row]
            x = -350
            t.update()
            t.penup()
            if orientation == "h":
                aircraft_horiz(x, y)

            elif orientation == "v":
                aircraft_vert(x, y)

        elif column == 7:
            y = col8[row]
            x = -300
            t.update()
            t.penup()
            if orientation == "h":
                aircraft_horiz(x, y)

            elif orientation == "v":
                aircraft_vert(x, y)

        elif column == 8:
            y = col9[row]
            x = -250
            t.update()
            t.penup()
            if orientation == "h":
                aircraft_horiz(x, y)

            elif orientation == "v":
                aircraft_vert(x, y)


        elif column == 9:
            y = col10[row]
            x = -200
            t.update()
            t.penup()
            if orientation == "h":
                aircraft_horiz(x, y)

            elif orientation == "v":
                aircraft_vert(x, y)
        return (board2_entity)


    board2_entity = carrier_placement(board2_entity)
    board = np.array(board2_entity)

    ###################################################################################################################
    shots = []
    turn = 0
    for i in range(10):
        shots.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    last_shot = 0
    while board2_entity != board_empty or board_entity != board_empty:
        fires = ''

        while fires != 'a':
            try:
                fires =  input("Location you want to fire: ")
                row = fires[0]
                if row == 'a' or row == 'b' or row == 'c' or row == 'd' or row == 'e' or row == 'f' or row == 'g' or row == 'h' or row == 'i' or row == 'j':
                    column = fires[1:]
                    row, column = rowc_converter(row, column)
                    break
                else:
                    row = 17 / 0
                    column = fires[1:]
                    row, column = rowc_converter(row, column)

            except:
                print('Invalid firing location- check for capitalization.')

        column = fires[1:]
        row, column = rowc_converter(row, column)
        if board_entity[row][column] == 1:
            print(player1, "Hit! 💥")
            if column == 0:
                y = col1[row]
                x = 0
                t.update()
                t.penup()
                hit(x, y)

            elif column == 1:
                y = col2[row]
                x = 50
                t.update()
                t.penup()
                hit(x, y)

            elif column == 2:
                y = col3[row]
                x = 100
                t.update()
                t.penup()
                hit(x, y)

            elif column == 3:
                y = col4[row]
                x = 150
                t.update()
                t.penup()
                hit(x, y)

            elif column == 4:
                y = col5[row]
                x = 200
                t.update()
                t.penup()
                hit(x, y)

            elif column == 5:
                y = col6[row]
                x = 250
                t.update()
                t.penup()
                hit(x, y)

            elif column == 6:
                y = col7[row]
                x = 300
                t.update()
                t.penup()
                hit(x, y)

            elif column == 7:
                y = col8[row]
                x = 350
                t.update()
                t.penup()
                hit(x, y)

            elif column == 8:
                y = col9[row]
                x = 400
                t.update()
                t.penup()
                hit(x, y)


            elif column == 9:
                y = col10[row]
                x = 450
                t.update()
                t.penup()
                hit(x, y)

            board_entity[row][column] = 0
        elif board_entity[row][column] == 0:
            print(player1, "Miss!")
            if column == 0:
                y = col1[row]
                x = 0
                t.update()
                t.penup()
                miss(x, y)

            elif column == 1:
                y = col2[row]
                x = 50
                t.update()
                t.penup()
                miss(x, y)

            elif column == 2:
                y = col3[row]
                x = 100
                t.update()
                t.penup()
                miss(x, y)

            elif column == 3:
                y = col4[row]
                x = 150
                t.update()
                t.penup()
                miss(x, y)

            elif column == 4:
                y = col5[row]
                x = 200
                t.update()
                t.penup()
                miss(x, y)

            elif column == 5:
                y = col6[row]
                x = 250
                t.update()
                t.penup()
                miss(x, y)

            elif column == 6:
                y = col7[row]
                x = 300
                t.update()
                t.penup()
                miss(x, y)

            elif column == 7:
                y = col8[row]
                x = 350
                t.update()
                t.penup()
                miss(x, y)

            elif column == 8:
                y = col9[row]
                x = 400
                t.update()
                t.penup()
                miss(x, y)


            elif column == 9:
                y = col10[row]
                x = 450
                t.update()
                t.penup()
                miss(x, y)
        board = np.array(board_entity)
    #CPU
        row = random.randint(0, 9)
        column = random.randint(0, 9)
        while True:
            if shots[row][column] == 1:
                row = random.randint(0, 9)
                column = random.randint(0, 9)
            else:
                break
        if shots[row][column] == 0:
            if last_shot == 1:
                if board2_entity[row][column] == 1:
                    print("CPU Hit 💥!")
                    if column == 0:
                        y = col1[row]
                        x = -650
                        t.update()
                        t.penup()
                        hit(x, y)

                    elif column == 1:
                        y = col2[row]
                        x = -600
                        t.update()
                        t.penup()
                        hit(x, y)

                    elif column == 2:
                        y = col3[row]
                        x = -550
                        t.update()
                        t.penup()
                        hit(x, y)

                    elif column == 3:
                        y = col4[row]
                        x = -500
                        t.update()
                        t.penup()
                        hit(x, y)

                    elif column == 4:
                        y = col5[row]
                        x = -450
                        t.update()
                        t.penup()
                        hit(x, y)

                    elif column == 5:
                        y = col6[row]
                        x = -400
                        t.update()
                        t.penup()
                        hit(x, y)

                    elif column == 6:
                        y = col7[row]
                        x = -350
                        t.update()
                        t.penup()
                        hit(x, y)

                    elif column == 7:
                        y = col8[row]
                        x = -300
                        t.update()
                        t.penup()
                        hit(x, y)

                    elif column == 8:
                        y = col9[row]
                        x = -250
                        t.update()
                        t.penup()
                        hit(x, y)


                    elif column == 9:
                        y = col10[row]
                        x = -200
                        t.update()
                        t.penup()
                        hit(x, y)
                    shots[row][column] = 1
                    last_shot = 1
                    last_row = row
                    last_column = column
                    board2_entity[row][column] = 0
                elif board2_entity[row][column] == 0:
                    print("CPU Miss!")
                    shots[row][column] = 1
                    last_shot = 0
            elif last_shot == 0:
                if board2_entity[row][column] == 1:
                    print("CPU Hit 💥!")
                    if column == 0:
                        y = col1[row]
                        x = -650
                        t.update()
                        t.penup()
                        hit(x, y)

                    elif column == 1:
                        y = col2[row]
                        x = -600
                        t.update()
                        t.penup()
                        hit(x, y)

                    elif column == 2:
                        y = col3[row]
                        x = -550
                        t.update()
                        t.penup()
                        hit(x, y)

                    elif column == 3:
                        y = col4[row]
                        x = -500
                        t.update()
                        t.penup()
                        hit(x, y)

                    elif column == 4:
                        y = col5[row]
                        x = -450
                        t.update()
                        t.penup()
                        hit(x, y)

                    elif column == 5:
                        y = col6[row]
                        x = -400
                        t.update()
                        t.penup()
                        hit(x, y)

                    elif column == 6:
                        y = col7[row]
                        x = -350
                        t.update()
                        t.penup()
                        hit(x, y)

                    elif column == 7:
                        y = col8[row]
                        x = -300
                        t.update()
                        t.penup()
                        hit(x, y)

                    elif column == 8:
                        y = col9[row]
                        x = -250
                        t.update()
                        t.penup()
                        hit(x, y)


                    elif column == 9:
                        y = col10[row]
                        x = -200
                        t.update()
                        t.penup()
                        hit(x, y)
                    shots[row][column] = 1
                    last_shot = 1
                    last_row = row
                    last_column = column
                    board2_entity[row][column] = 0
                elif board2_entity[row][column] == 0:
                    if random.randint(0, 3) == 0:
                        while True:
                            if board2_entity[row][column] == 0:
                                row = random.randint(0, 9)
                                column = random.randint(0, 9)
                            else:
                                break
                        print("CPU Hit 💥!")
                        if column == 0:
                            y = col1[row]
                            x = -650
                            t.update()
                            t.penup()
                            hit(x, y)

                        elif column == 1:
                            y = col2[row]
                            x = -600
                            t.update()
                            t.penup()
                            hit(x, y)

                        elif column == 2:
                            y = col3[row]
                            x = -550
                            t.update()
                            t.penup()
                            hit(x, y)

                        elif column == 3:
                            y = col4[row]
                            x = -500
                            t.update()
                            t.penup()
                            hit(x, y)

                        elif column == 4:
                            y = col5[row]
                            x = -450
                            t.update()
                            t.penup()
                            hit(x, y)

                        elif column == 5:
                            y = col6[row]
                            x = -400
                            t.update()
                            t.penup()
                            hit(x, y)

                        elif column == 6:
                            y = col7[row]
                            x = -350
                            t.update()
                            t.penup()
                            hit(x, y)

                        elif column == 7:
                            y = col8[row]
                            x = -300
                            t.update()
                            t.penup()
                            hit(x, y)

                        elif column == 8:
                            y = col9[row]
                            x = -250
                            t.update()
                            t.penup()
                            hit(x, y)


                        elif column == 9:
                            y = col10[row]
                            x = -200
                            t.update()
                            t.penup()
                            hit(x, y)
                        shots[row][column] = 1
                        last_shot = 1
                        last_row = row
                        last_column = column
                        board2_entity[row][column] = 0
                    else:
                        print("CPU Miss!")
                        shots[row][column] = 1
                        last_shot = 0
            board = np.array(board2_entity)
            board = np.array(shots)

        if board2_entity == board_empty:
            print("YOU LOSE!")
            break
        elif board_entity == board_empty:
            print(player1, "HAS WON!!!")
            break


if game_type == '2':
    player1 = input("Enter player 1's name:")
    player2 = input("Enter player 2's name:")
    print("All set! Let's go!")
    col1 = [250, 200, 150, 100, 50, 0, -50, -100, -150, -200]
    col2 = [250, 200, 150, 100, 50, 0, -50, -100, -150, -200]
    col3 = [250, 200, 150, 100, 50, 0, -50, -100, -150, -200]
    col4 = [250, 200, 150, 100, 50, 0, -50, -100, -150, -200]
    col5 = [250, 200, 150, 100, 50, 0, -50, -100, -150, -200]
    col6 = [250, 200, 150, 100, 50, 0, -50, -100, -150, -200]
    col7 = [250, 200, 150, 100, 50, 0, -50, -100, -150, -200]
    col8 = [250, 200, 150, 100, 50, 0, -50, -100, -150, -200]
    col9 = [250, 200, 150, 100, 50, 0, -50, -100, -150, -200]
    col10 = [250, 200, 150, 100, 50, 0, -50, -100, -150, -200]
    col = [col1, col2, col3, col4, col5, col6, col7, col8, col9, col10]
    letter_val = 0
    print("Please wait. We are travelling to",player1,"'s Python Sea...")
    print("Make sure to maximize your turtle screen while the board is loading, you won't be able to do it later!")
    board_playerships(player1)
    board_entity = []
    board2_entity = []
    for i in range(10):
        board_entity.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    for i in range(10):
        board2_entity.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    board_empty = []
    for i in range(10):
        board_empty.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    print("Time to place your ships! Make sure to enter your coordinates with lowercase letters and no spaces \n"
          "(Enter 'a1' to place a ship at square A1, do not enter the number first (1a) your game will end)\n "
          "*Please note that the box you enter will be occupied by the back left corner of the ship*")
    print("Player one, enter in your ships")


    def rowc_converter(row, column):
        """Converts user input for letter rows to a number that the computer can use to call an x value (defined again bc previous was in an if statement)"""
        if row == 'a':
            row = 0
        if row == 'b':
            row = 1
        if row == 'c':
            row = 2
        if row == 'd':
            row = 3
        if row == 'e':
            row = 4
        if row == 'f':
            row = 5
        if row == 'g':
            row = 6
        if row == 'h':
            row = 7
        if row == 'i':
            row = 8
        if row == 'j':
            row = 9
        column = int(column) - 1
        return (row, column)


    def destroyer_placement(board2_entity):
        """Code function for the player's destroyer placement. Used in hit registration."""
        orientation = ''
        while orientation != 'v' and orientation != 'h':
            try:
                orientation = input(
                    "What orientation do you want the destroyer in? (type h for horizontal and v for vertical):")
                if orientation == 'h' or orientation == 'v':
                    break
                else:
                    orientation = 17 / 0
            except:
                print("Oops! Invalid input. Please try again.")

        # test for placements that put ships out of bounds
        row = 0
        column = 9
        if orientation == 'h':
            while column == 9:
                try:
                    destpos = input("What box do you want to place the destroyer (2 spaces long) in?")
                    row = destpos[0]
                    if row == 'a' or row == 'b' or row == 'c' or row == 'd' or row == 'e' or row == 'f' or row == 'g' or row =='h' or row == 'i' or row == 'j':
                        column = destpos[1:]
                        row, column = rowc_converter(row, column)
                        board2_entity[row][column] = 1
                        board2_entity[row][column + 1] = 1
                        break

                    else:
                        row = 17 / 0
                        column = destpos[1:]
                        row, column = rowc_converter(row, column)
                        board2_entity[row][column] = 1
                        board2_entity[row][column + 1] = 1

                except:
                    print('Invalid starting location- check for out of bound placement or capitalization.')


        elif orientation == 'v':

            while row == 0:
                try:
                    destpos = input("What box do you want to place the destroyer (2 spaces long) in?")
                    row = destpos[0]
                    if row == 'a' or row == 'b' or row == 'c' or row == 'd' or row == 'e' or row == 'f' or row == 'g' or row =='h' or row == 'i' or row == 'j':
                        column = destpos[1:]
                        row, column = rowc_converter(row, column)
                        board2_entity[row][column] = 1
                        board2_entity[row - 1][column] = 1
                        break

                    else:
                        row = 17 / 0
                        column = destpos[1:]
                        row, column = rowc_converter(row, column)
                        board2_entity[row][column] = 1
                        board2_entity[row - 1][column] = 1

                except:
                    print('Invalid starting location- check for out of bound placement or capitalization.')
        # Determines coordinates for ship placement.
        if column == 0:
            y = col1[row]
            x = -650
            t.update()
            t.penup()
            if orientation == "h":
                destroyer_h(x, y)

            elif orientation == "v":
                destroyer_v(x, y)


        elif column == 1:
            y = col2[row]
            x = -600
            t.update()
            t.penup()
            if orientation == "h":
                destroyer_h(x, y)

            elif orientation == "v":
                destroyer_v(x, y)


        elif column == 2:
            y = col3[row]
            x = -550
            t.update()
            t.penup()
            if orientation == "h":
                destroyer_h(x, y)

            elif orientation == "v":
                destroyer_v(x, y)

        elif column == 3:
            y = col4[row]
            x = -500
            t.update()
            t.penup()
            if orientation == "h":
                destroyer_h(x, y)

            elif orientation == "v":
                destroyer_v(x, y)


        elif column == 4:
            y = col5[row]
            x = -450
            t.update()
            t.penup()
            if orientation == "h":
                destroyer_h(x, y)

            elif orientation == "v":
                destroyer_v(x, y)


        elif column == 5:
            y = col6[row]
            x = -400
            t.update()
            t.penup()
            if orientation == "h":
                destroyer_h(x, y)

            elif orientation == "v":
                destroyer_v(x, y)


        elif column == 6:
            y = col7[row]
            x = -350
            t.update()
            t.penup()
            if orientation == "h":
                destroyer_h(x, y)

            elif orientation == "v":
                destroyer_v(x, y)


        elif column == 7:
            y = col8[row]
            x = -300
            t.update()
            t.penup()
            if orientation == "h":
                destroyer_h(x, y)

            elif orientation == "v":
                destroyer_v(x, y)

        elif column == 8:
            y = col9[row]
            x = -250
            t.update()
            t.penup()
            if orientation == "h":
                destroyer_h(x, y)

            elif orientation == "v":
                destroyer_v(x, y)


        elif column == 9:
            y = col10[row]
            x = -200
            t.update()
            t.penup()
            if orientation == "h":
                destroyer_h(x, y)

            elif orientation == "v":
                destroyer_v(x, y)
        return (board2_entity)



    def cruiser_placement(board2_entity):
        """Code for the computer's cruiser placement. Used for hit registration."""
        orientation = ''
        while orientation != 'v' and orientation != 'h':
            try:
                orientation = input(
                    "What orientation do you want the cruiser in? (type h for horizontal and v for vertical):")
                if orientation == 'h' or orientation == 'v':
                    break
                else:
                    orientation = 17 / 0
            except:
                print("Oops! Invalid input. Please try again.")


        row = 0
        column = 9
        # test for placements that put ships out of bounds or overlaps with another ship- overlap test not needed for destroyer bc it is the first ship placed
        if orientation == 'v':
            while row == 0 or row == 1:
                try:
                    cruiserpos = input(
                        "What box do you want to place the cruiser (3 spaces long) in?")

                    row = cruiserpos[0]
                    column = cruiserpos[1:]
                    row, column = rowc_converter(row, column)  #cruiser begins including the test for overlapping ships
                    if row == 0 or row == 1 or board2_entity[row][column] == 1 or board2_entity[row - 1][column] == 1 or board2_entity[row - 2][column] == 1:
                        row = row / 17  # force an error if there is already a ship placed in the box entered or if its out of bounds
                        board2_entity[row][column] = 1
                        board2_entity[row - 1][column] = 1
                        board2_entity[row - 2][column] = 1
                    else:
                        row = row
                        board2_entity[row][column] = 1
                        board2_entity[row - 1][column] = 1
                        board2_entity[row - 2][column] = 1
                        break
                except:
                    print('Invalid starting location- check for overlap or out of bound placement.')
                    row = 0
        if orientation == 'h':
            while column == 9 or 8:
                try:
                    cruiserpos = input(
                        "What box do you want to place the cruiser (3 spaces long) in?")

                    row = cruiserpos[0]
                    column = cruiserpos[1:]
                    row, column = rowc_converter(row, column)
                    if board2_entity[row][column] == 1 or board2_entity[row][column + 1] == 1 or  board2_entity[row][column + 2] == 1:
                        row = row / 17  # force an error if there is already a ship placed in the box entered
                        board2_entity[row][column] = 1
                        board2_entity[row][column + 1] = 1
                        board2_entity[row][column + 2] = 1
                    if column != 8 or 9:
                        board2_entity[row][column] = 1
                        board2_entity[row][column + 1] = 1
                        board2_entity[row][column + 2] = 1
                        break

                except:
                    print('Invalid starting location- check for overlap or out of bound placement.')




        if column == 0:
            y = col1[row]
            x = -650
            t.update()
            t.penup()
            if orientation == "h":
                cruiser_h(x, y)

            elif orientation == "v":
                cruiser_v(x, y)


        elif column == 1:
            y = col2[row]
            x = -600
            t.update()
            t.penup()
            if orientation == "h":
                cruiser_h(x, y)

            elif orientation == "v":
                cruiser_v(x, y)



        elif column == 2:
            y = col3[row]
            x = -550
            t.update()
            t.penup()
            if orientation == "h":
                cruiser_h(x, y)

            elif orientation == "v":
                cruiser_v(x, y)


        elif column == 3:
            y = col4[row]
            x = -500
            t.update()
            t.penup()
            if orientation == "h":
                cruiser_h(x, y)

            elif orientation == "v":
                cruiser_v(x, y)


        elif column == 4:
            y = col5[row]
            x = -450
            t.update()
            t.penup()
            if orientation == "h":
                cruiser_h(x, y)

            elif orientation == "v":
                cruiser_v(x, y)



        elif column == 5:
            y = col6[row]
            x = -400
            t.update()
            t.penup()
            if orientation == "h":
                cruiser_h(x, y)

            elif orientation == "v":
                cruiser_v(x, y)


        elif column == 6:
            y = col7[row]
            x = -350
            t.update()
            t.penup()
            if orientation == "h":
                cruiser_h(x, y)

            elif orientation == "v":
                cruiser_v(x, y)



        elif column == 7:
            y = col8[row]
            x = -300
            t.update()
            t.penup()
            if orientation == "h":
                cruiser_h(x, y)

            elif orientation == "v":
                cruiser_v(x, y)

        elif column == 8:
            y = col9[row]
            x = -250
            t.update()
            t.penup()
            if orientation == "h":
                cruiser_h(x, y)

            elif orientation == "v":
                cruiser_v(x, y)



        elif column == 9:
            y = col10[row]
            x = -200
            t.update()
            t.penup()
            if orientation == "h":
                cruiser_h(x, y)

            elif orientation == "v":
                cruiser_v(x, y)
        return (board2_entity)



    def submarine_placement(board2_entity):
        """Code for the computer's submarine placement. Used for hit registration."""
        orientation = ''
        while orientation != 'v' and orientation != 'h':
            try:
                orientation = input(
                    "What orientation do you want the submarine in? (type h for horizontal and v for vertical):")
                if orientation == 'h' or orientation == 'v':
                    break
                else:
                    orientation = 17 / 0
            except:
                print("Oops! Invalid input. Please try again.")


        row = 0
        column = 9
        # tests for placements that put ships out of bounds or overlaps with another ship
        if orientation == 'v':
            while row == 0 or row == 1:
                try:
                    submarinepos = input("What box do you want to place the submarine (3 spaces long) in?")

                    row = submarinepos[0]
                    column = submarinepos[1:]
                    row, column = rowc_converter(row, column)
                    if row == 0 or row == 1 or board2_entity[row][column] == 1 or  board2_entity[row - 1][column] == 1 or board2_entity[row - 2][column] == 1:
                        row = row / 17  # force an error if there is already a ship placed in the box entered or if its out of bounds
                        board2_entity[row][column] = 1
                        board2_entity[row - 1][column] = 1
                        board2_entity[row - 2][column] = 1
                    else:
                        row = row
                        board2_entity[row][column] = 1
                        board2_entity[row - 1][column] = 1
                        board2_entity[row - 2][column] = 1
                        break

                except:
                    print('Invalid starting location- check for overlap or out of bound placement.')
                    row = 0
        if orientation == 'h':
            while column == 9 or 8:
                try:
                    submarinepos = input("What box do you want to place the submarine (3 spaces long) in?")

                    row = submarinepos[0]
                    column = submarinepos[1:]
                    row, column = rowc_converter(row, column)
                    if board2_entity[row][column] == 1 or board2_entity[row][column + 1] == 1 or board2_entity[row][column + 2] == 1:
                        row = row / 17  # force an error if there is already a ship placed in the box entered
                        board2_entity[row][column] = 1
                        board2_entity[row][column + 1] = 1
                        board2_entity[row][column + 2] = 1
                    if column != 8 or 9:
                        board2_entity[row][column] = 1
                        board2_entity[row][column + 1] = 1
                        board2_entity[row][column + 2] = 1
                        break
                except:
                    print('Invalid starting location- check for overlap or out of bound placement.')


        if column == 0:
            y = col1[row]
            x = -650
            t.update()
            t.penup()
            if orientation == "h":
                submarine_h(x, y)

            elif orientation == "v":
                submarine_v(x, y)


        elif column == 1:
            y = col2[row]
            x = -600
            t.update()
            t.penup()
            if orientation == "h":
                submarine_h(x, y)

            elif orientation == "v":
                submarine_v(x, y)

        elif column == 2:
            y = col3[row]
            x = -550
            t.update()
            t.penup()
            if orientation == "h":
                submarine_h(x, y)

            elif orientation == "v":
                submarine_v(x, y)

        elif column == 3:
            y = col4[row]
            x = -500
            t.update()
            t.penup()
            if orientation == "h":
                submarine_h(x, y)

            elif orientation == "v":
                submarine_v(x, y)


        elif column == 4:
            y = col5[row]
            x = -450
            t.update()
            t.penup()
            if orientation == "h":
                submarine_h(x, y)

            elif orientation == "v":
                submarine_v(x, y)

        elif column == 5:
            y = col6[row]
            x = -400
            t.update()
            t.penup()
            if orientation == "h":
                submarine_h(x, y)

            elif orientation == "v":
                submarine_v(x, y)

        elif column == 6:
            y = col7[row]
            x = -350
            t.update()
            t.penup()
            if orientation == "h":
                submarine_h(x, y)

            elif orientation == "v":
                submarine_v(x, y)

        elif column == 7:
            y = col8[row]
            x = -300
            t.update()
            t.penup()
            if orientation == "h":
                submarine_h(x, y)

            elif orientation == "v":
                submarine_v(x, y)

        elif column == 8:
            y = col9[row]
            x = -250
            t.update()
            t.penup()
            if orientation == "h":
                submarine_h(x, y)

            elif orientation == "v":
                submarine_v(x, y)


        elif column == 9:
            y = col10[row]
            x = -200
            t.update()
            t.penup()
            if orientation == "h":
                submarine_h(x, y)

            elif orientation == "v":
                submarine_v(x, y)
        return (board2_entity)



    def battleship_placement(board2_entity):
        """Code for the computer's battleship placement. Used for hit registration."""
        orientation = ''
        while orientation != 'v' and orientation != 'h':
            try:
                orientation = input(
                    "What orientation do you want the battleship in? (type h for horizontal and v for vertical):")
                if orientation == 'h' or orientation == 'v':
                    break
                else:
                    orientation = 17 / 0
            except:
                print("Oops! Invalid input. Please try again.")
        # tests for placements that put ships out of bounds or overlaps with another ship
        row = 0
        column = 9
        if orientation == 'v':
            while row == 0 or row == 1 or row == 2:
                try:
                    battleshippos = input(
                        "What box do you want to place the battleship (4 spaces long) in?")

                    row = battleshippos[0]
                    column = battleshippos[1:]
                    row, column = rowc_converter(row, column)
                    if row == 0 or row == 1 or row == 2 or  board2_entity[row][column] == 1 or board2_entity[row - 1][column] == 1 or board2_entity[row - 2][column] == 1 or board2_entity[row - 3][column] == 1:
                        row = row / 17  # force an error if there is already a ship placed in the box entered or if its out of bounds
                        board2_entity[row][column] = 1
                        board2_entity[row - 1][column] = 1
                        board2_entity[row - 2][column] = 1
                        board2_entity[row - 3][column] = 1
                    else:
                        row = row
                        board2_entity[row][column] = 1
                        board2_entity[row - 1][column] = 1
                        board2_entity[row - 2][column] = 1
                        board2_entity[row - 3][column] = 1
                        break
                except:
                    print('Invalid starting location- check for overlap or out of bound placement.')
                    row = 0
        if orientation == 'h':
            while column == 9 or 8 or 7:
                try:
                    battleshippos = input(
                        "What box do you want to place the battleship (4 spaces long) in?")

                    row = battleshippos[0]
                    column = battleshippos[1:]
                    row, column = rowc_converter(row, column)
                    if board2_entity[row][column] == 1 or board2_entity[row][column + 1] == 1 or board2_entity[row][column + 2] == 1 or board2_entity[row][column + 3] == 1:
                        row = row / 17  # force an error if there is already a ship placed in the box entered
                        board2_entity[row][column] = 1
                        board2_entity[row][column + 1] = 1
                        board2_entity[row][column + 2] = 1
                        board2_entity[row][column + 3] = 1
                    if column != 7 or 8 or 9:
                        board2_entity[row][column] = 1
                        board2_entity[row][column + 1] = 1
                        board2_entity[row][column + 2] = 1
                        board2_entity[row][column + 3] = 1
                        break
                except:
                    print('Invalid starting location- check for overlap or out of bound placement.')




        if column == 0:
            y = col1[row]
            x = -650
            t.update()
            t.penup()
            if orientation == "h":
                battleship_horiz(x, y)

            elif orientation == "v":
                battleship_vert(x, y)


        elif column == 1:
            y = col2[row]
            x = -600
            t.update()
            t.penup()
            if orientation == "h":
                battleship_horiz(x, y)

            elif orientation == "v":
                battleship_vert(x, y)

        elif column == 2:
            y = col3[row]
            x = -550
            t.update()
            t.penup()
            if orientation == "h":
                battleship_horiz(x, y)

            elif orientation == "v":
                battleship_vert(x, y)

        elif column == 3:
            y = col4[row]
            x = -500
            t.update()
            t.penup()
            if orientation == "h":
                battleship_horiz(x, y)

            elif orientation == "v":
                battleship_vert(x, y)


        elif column == 4:
            y = col5[row]
            x = -450
            t.update()
            t.penup()
            if orientation == "h":
                battleship_horiz(x, y)

            elif orientation == "v":
                battleship_vert(x, y)

        elif column == 5:
            y = col6[row]
            x = -400
            t.update()
            t.penup()
            if orientation == "h":
                battleship_horiz(x, y)

            elif orientation == "v":
                battleship_vert(x, y)

        elif column == 6:
            y = col7[row]
            x = -350
            t.update()
            t.penup()
            if orientation == "h":
                battleship_horiz(x, y)

            elif orientation == "v":
                battleship_vert(x, y)

        elif column == 7:
            y = col8[row]
            x = -300
            t.update()
            t.penup()
            if orientation == "h":
                battleship_horiz(x, y)

            elif orientation == "v":
                battleship_vert(x, y)

        elif column == 8:
            y = col9[row]
            x = -250
            t.update()
            t.penup()
            if orientation == "h":
                battleship_horiz(x, y)

            elif orientation == "v":
                battleship_vert(x, y)


        elif column == 9:
            y = col10[row]
            x = -200
            t.update()
            t.penup()
            if orientation == "h":
                battleship_horiz(x, y)

            elif orientation == "v":
                battleship_vert(x, y)
        return (board2_entity)


    def carrier_placement(board2_entity):
        """Code for the computer's carrier placement. Used for hit registration."""
        orientation = ''
        while orientation != 'v' and orientation != 'h':
            try:
                orientation = input(
                    "What orientation do you want the aircraft carrier in? (type h for horizontal and v for vertical):")
                if orientation == 'h' or orientation == 'v':
                    break
                else:
                    orientation = 17 / 0
            except:
                print("Oops! Invalid input. Please try again.")

        #test for placements that put ships out of bounds
        row = 0
        column = 9
        if orientation == 'v':
            while row == 0 or row == 1 or row == 2 or row == 3:
                try:
                    carrierpos = input(
                        "What box do you want to place the carrier (5 spaces long) in?")

                    row = carrierpos[0]
                    column = carrierpos[1:]
                    row, column = rowc_converter(row, column)
                    if row == 0 or row == 1 or row == 2 or row == 3 or board2_entity[row][column] == 1 or board2_entity[row - 1][column] == 1 or board2_entity[row - 2][column] == 1 or board2_entity[row - 3][column] == 1 or board2_entity[row - 4][column] == 1:
                        row = row / 17  # force an error if there is already a ship placed in the box entered or if the ship is out of bounds
                        board2_entity[row][column] = 1
                        board2_entity[row - 1][column] = 1
                        board2_entity[row - 2][column] = 1
                        board2_entity[row - 3][column] = 1
                        board2_entity[row - 4][column] = 1
                    else:
                        row = row
                        board2_entity[row][column] = 1
                        board2_entity[row - 1][column] = 1
                        board2_entity[row - 2][column] = 1
                        board2_entity[row - 3][column] = 1
                        board2_entity[row - 4][column] = 1
                        break

                except:
                    print('Invalid starting location- check for overlap or out of bound placement.')
                    row = 0
        if orientation == 'h':
            while column == 9 or 8 or 7 or 6:
                try:
                    carrierpos = input(
                        "What box do you want to place the carrier (5 spaces long) in?")

                    row = carrierpos[0]
                    column = carrierpos[1:]
                    row, column = rowc_converter(row, column)
                    if board2_entity[row][column] == 1 or  board2_entity[row][column + 1] == 1 or board2_entity[row][column + 2] == 1 or board2_entity[row][column + 3] == 1 or board2_entity[row][column + 4] == 1:
                        row = row / 17  # force an error if there is already a ship placed in the box entered
                        board2_entity[row][column] = 1
                        board2_entity[row][column + 1] = 1
                        board2_entity[row][column + 2] = 1
                        board2_entity[row][column + 3] = 1
                        board2_entity[row][column + 4] = 1
                    if column != 9 or 8 or 7 or 6:
                        board2_entity[row][column] = 1
                        board2_entity[row][column + 1] = 1
                        board2_entity[row][column + 2] = 1
                        board2_entity[row][column + 3] = 1
                        board2_entity[row][column + 4] = 1
                        break
                except :
                    print('Invalid starting location- check for overlap or out of bound placement.')






        if column == 0:
            y = col1[row]
            x = -650
            t.update()
            t.penup()
            if orientation == "h":
                aircraft_horiz(x, y)

            elif orientation == "v":
                aircraft_vert(x, y)


        elif column == 1:
            y = col2[row]
            x = -600
            t.update()
            t.penup()
            if orientation == "h":
                aircraft_horiz(x, y)

            elif orientation == "v":
                aircraft_vert(x, y)

        elif column == 2:
            y = col3[row]
            x = -550
            t.update()
            t.penup()
            if orientation == "h":
                aircraft_horiz(x, y)

            elif orientation == "v":
                aircraft_vert(x, y)

        elif column == 3:
            y = col4[row]
            x = -500
            t.update()
            t.penup()
            if orientation == "h":
                aircraft_horiz(x, y)

            elif orientation == "v":
                aircraft_vert(x, y)


        elif column == 4:
            y = col5[row]
            x = -450
            t.update()
            t.penup()
            if orientation == "h":
                aircraft_horiz(x, y)

            elif orientation == "v":
                aircraft_vert(x, y)

        elif column == 5:
            y = col6[row]
            x = -400
            t.update()
            t.penup()
            if orientation == "h":
                aircraft_horiz(x, y)

            elif orientation == "v":
                aircraft_vert(x, y)

        elif column == 6:
            y = col7[row]
            x = -350
            t.update()
            t.penup()
            if orientation == "h":
                aircraft_horiz(x, y)

            elif orientation == "v":
                aircraft_vert(x, y)

        elif column == 7:
            y = col8[row]
            x = -300
            t.update()
            t.penup()
            if orientation == "h":
                aircraft_horiz(x, y)

            elif orientation == "v":
                aircraft_vert(x, y)

        elif column == 8:
            y = col9[row]
            x = -250
            t.update()
            t.penup()
            if orientation == "h":
                aircraft_horiz(x, y)

            elif orientation == "v":
                aircraft_vert(x, y)


        elif column == 9:
            y = col10[row]
            x = -200
            t.update()
            t.penup()
            if orientation == "h":
                aircraft_horiz(x, y)

            elif orientation == "v":
                aircraft_vert(x, y)
        return (board2_entity)



    board_entity = destroyer_placement(board_entity)
    board_entity = cruiser_placement(board_entity)
    board_entity = submarine_placement(board_entity)
    board_entity = battleship_placement(board_entity)
    board_entity = carrier_placement(board_entity)
    print("We are now traveling to",player2,"'s Python Sea...")
    print("Player 2 enter in your ships")
    t.clearscreen()
    board_playerships(player2)
    board2_entity = destroyer_placement(board2_entity)
    board2_entity = cruiser_placement(board2_entity)
    board2_entity = submarine_placement(board2_entity)
    board2_entity = battleship_placement(board2_entity)
    board2_entity = carrier_placement(board2_entity)
    print("Loading the shots board...")
    t.clearscreen()
    board_shots(player1, player2)

    while (board2_entity or board_entity) != board_empty:
        fires = ''

        while fires != 'a':
            try:
                fires = input('Location you want to fire on')
                row = fires[0]
                if row == 'a' or row == 'b' or row == 'c' or row == 'd' or row == 'e' or row == 'f' or row == 'g' or row == 'h' or row == 'i' or row == 'j':
                    column = fires[1:]
                    row, column = rowc_converter(row, column)
                    break
                else:
                    row = 17 / 0
                    column = fires[1:]
                    row, column = rowc_converter(row, column)

            except:
                print('Invalid firing location- check for capitalization.')
        if board2_entity[row][column] == 1:
            print(player1, "Hit! 💥")
            if column == 0:
                y = col1[row]
                x = -650
                t.update()
                t.penup()
                hit(x, y)

            elif column == 1:
                y = col2[row]
                x = -600
                t.update()
                t.penup()
                hit(x, y)

            elif column == 2:
                y = col3[row]
                x = -550
                t.update()
                t.penup()
                hit(x, y)

            elif column == 3:
                y = col4[row]
                x = -500
                t.update()
                t.penup()
                hit(x, y)

            elif column == 4:
                y = col5[row]
                x = -450
                t.update()
                t.penup()
                hit(x, y)

            elif column == 5:
                y = col6[row]
                x = -400
                t.update()
                t.penup()
                hit(x, y)

            elif column == 6:
                y = col7[row]
                x = -350
                t.update()
                t.penup()
                hit(x, y)

            elif column == 7:
                y = col8[row]
                x = -300
                t.update()
                t.penup()
                hit(x, y)

            elif column == 8:
                y = col9[row]
                x = -250
                t.update()
                t.penup()
                hit(x, y)


            elif column == 9:
                y = col10[row]
                x = -200
                t.update()
                t.penup()
                hit(x, y)

            board2_entity[row][column] = 0
        elif board2_entity[row][column] == 0:
            print(player1, "Miss!")
            if column == 0:
                y = col1[row]
                x = -650
                t.update()
                t.penup()
                miss(x, y)

            elif column == 1:
                y = col2[row]
                x = -600
                t.update()
                t.penup()
                miss(x, y)

            elif column == 2:
                y = col3[row]
                x = -550
                t.update()
                t.penup()
                miss(x, y)

            elif column == 3:
                y = col4[row]
                x = -500
                t.update()
                t.penup()
                miss(x, y)

            elif column == 4:
                y = col5[row]
                x = -450
                t.update()
                t.penup()
                miss(x, y)

            elif column == 5:
                y = col6[row]
                x = -400
                t.update()
                t.penup()
                miss(x, y)

            elif column == 6:
                y = col7[row]
                x = -350
                t.update()
                t.penup()
                miss(x, y)

            elif column == 7:
                y = col8[row]
                x = -300
                t.update()
                t.penup()
                miss(x, y)

            elif column == 8:
                y = col9[row]
                x = -250
                t.update()
                t.penup()
                miss(x, y)


            elif column == 9:
                y = col10[row]
                x = -200
                t.update()
                t.penup()
                miss(x, y)
        board = np.array(board2_entity)
        ##############################################################################################################
        fires = ''

        while fires != 'a':
            try:
                fires = input('Location you want to fire:')
                row = fires[0]
                if row == 'a' or row == 'b' or row == 'c' or row == 'd' or row == 'e' or row == 'f' or row == 'g' or row == 'h' or row == 'i' or row == 'j':
                    column = fires[1:]
                    row, column = rowc_converter(row, column)
                    break
                else:
                    row = 17 / 0
                    column = fires[1:]
                    row, column = rowc_converter(row, column)

            except:
                print('Invalid firing location- check for capitalization.')
        if board_entity[row][column] == 1:
            print(player2, "Hit! 💥")

            if column == 0:
                y = col1[row]
                x = 0
                t.update()
                t.penup()
                hit(x, y)

            elif column == 1:
                y = col2[row]
                x = 50
                t.update()
                t.penup()
                hit(x, y)

            elif column == 2:
                y = col3[row]
                x = 100
                t.update()
                t.penup()
                hit(x, y)

            elif column == 3:
                y = col4[row]
                x = 150
                t.update()
                t.penup()
                hit(x, y)

            elif column == 4:
                y = col5[row]
                x = 200
                t.update()
                t.penup()
                hit(x, y)

            elif column == 5:
                y = col6[row]
                x = 250
                t.update()
                t.penup()
                hit(x, y)

            elif column == 6:
                y = col7[row]
                x = 300
                t.update()
                t.penup()
                hit(x, y)

            elif column == 7:
                y = col8[row]
                x = 350
                t.update()
                t.penup()
                hit(x, y)

            elif column == 8:
                y = col9[row]
                x = 400
                t.update()
                t.penup()
                hit(x, y)


            elif column == 9:
                y = col10[row]
                x = 450
                t.update()
                t.penup()
                hit(x, y)
                board_entity[row][column] = 0
        elif board_entity[row][column] == 0:
            print(player2, "Miss!")
            if column == 0:
                y = col1[row]
                x = 0
                t.update()
                t.penup()
                miss(x, y)

            elif column == 1:
                y = col2[row]
                x = 50
                t.update()
                t.penup()
                miss(x, y)

            elif column == 2:
                y = col3[row]
                x = 100
                t.update()
                t.penup()
                miss(x, y)

            elif column == 3:
                y = col4[row]
                x = 150
                t.update()
                t.penup()
                miss(x, y)

            elif column == 4:
                y = col5[row]
                x = 200
                t.update()
                t.penup()
                miss(x, y)

            elif column == 5:
                y = col6[row]
                x = 250
                t.update()
                t.penup()
                miss(x, y)

            elif column == 6:
                y = col7[row]
                x = 300
                t.update()
                t.penup()
                miss(x, y)

            elif column == 7:
                y = col8[row]
                x = 350
                t.update()
                t.penup()
                miss(x, y)

            elif column == 8:
                y = col9[row]
                x = 400
                t.update()
                t.penup()
                miss(x, y)


            elif column == 9:
                y = col10[row]
                x = 450
                t.update()
                t.penup()
                miss(x, y)
        board = np.array(board_entity)


        #print who has won
        if board2_entity == board_empty:
            print(player1,"HAS WON!!!")
            break

        elif board_entity == board_empty:
            print(player2,"HAS WON!!!")
            break
print("To play again, reload the game by pressing the green arrow to the left of your console.")
print("To exit, close your turtle window.")


