# importing libraries
import pygame
import time
import random

snake_speed = 15

# Window size
windowX = 720
windowY = 480

# defining colors
black = pygame.Color(0, 0, 0)
gray = pygame.Color(35, 35, 35)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
headColor = pygame.Color(50, 190, 130)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Catch them apples')  # Title
game_window = pygame.display.set_mode((windowX, windowY))


gameBoardX = 15
gameBoardY = 10
gameBoard = [[0 for _ in range(gameBoardX)] for _ in range(gameBoardY)]

headX = int(gameBoardX/2)
headY = int(gameBoardY/2)

length = 2

gameBoard[headY][headX] = length

direction = "RIGHT"


boxWidth = int(windowX/gameBoardX)
boxHeight = int(windowY/gameBoardY)
boxSpaceX = int(boxWidth/20)
boxSpaceY = int(boxHeight/20)
def gameOver():
    global length
    my_font = pygame.font.SysFont('times new roman', 60)

    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render('Your Final Length was: ' + str(length), True, red)

    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()

    # setting position of the text
    game_over_rect.midtop = (windowX / 2, windowY / 4)

    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # after 2 seconds we will quit the program
    time.sleep(4)

    # deactivating pygame library
    pygame.quit()

    # quit the program
    quit()

def drawBox(x, y, color):
    pygame.draw.rect(game_window, color, pygame.Rect(x*boxWidth+boxSpaceX, y*boxHeight+boxSpaceY, boxWidth-boxSpaceX*2, boxHeight-boxSpaceY*2))

def drawSnake(gameArray):
    for rowIndex in range(gameBoardY):
        for colIndex in range(gameBoardX):
            if gameArray[rowIndex][colIndex] == -1:
                drawBox(colIndex, rowIndex, red)
            elif gameArray[rowIndex][colIndex] != 0:
                drawBox(colIndex, rowIndex, green)

    drawBox(headX, headY, headColor)

def AddApple():
    while True:
        row = random.randrange(0,gameBoardY)
        col = random.randrange(0, gameBoardX)

        if (gameBoard[row][col]) == 0:
            gameBoard[row][col] = -1
            break
def UpdateGameBoard(dir):
    global headX
    global headY
    global gameBoard
    global length
    if dir == "RIGHT":
        if (headX >= gameBoardX-1):
            gameOver()
        else:
            headX += 1
    if dir == "LEFT":
        if (headX <= 0):
            gameOver()
        else:
            headX -= 1
    if dir == "UP":
        if (headY <= 0):
            gameOver()
        else:
            headY -= 1
    if dir == "DOWN":
        if (headY >= gameBoardY-1):
            gameOver()
        else:
            headY += 1

    if gameBoard[headY][headX] == -1:
        length += 1
        AddApple()
    elif gameBoard[headY][headX] != 0:
        gameOver()
    else:
        for row in range(gameBoardY):
            for col in range(gameBoardX):
                print(gameBoard[row][col])
                if (gameBoard[row][col]) != 0 and (gameBoard[row][col]) != -1:
                    gameBoard[row][col] -= 1



    gameBoard[headY][headX] = length



# Main Function
AddApple()
game_window.fill(black)
for row in range(gameBoardY):
    for col in range(gameBoardX):
        drawBox(col, row, gray)
drawSnake(gameBoard)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = 'UP'
            if event.key == pygame.K_DOWN:
                direction = 'DOWN'
            if event.key == pygame.K_LEFT:
                direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                direction = 'RIGHT'

            UpdateGameBoard(direction)


            print(gameBoard)
            # Drawing the screen:
            game_window.fill(black)

            # Fill empty spaces
            for row in range(gameBoardY):
                for col in range(gameBoardX):
                    drawBox(col, row, gray)

            #drawBox(headX, headY, green)

            # Draw Snake
            drawSnake(gameBoard)


            pygame.display.update()

            print(direction)
