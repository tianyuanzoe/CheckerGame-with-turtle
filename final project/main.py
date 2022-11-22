'''
cs5001
tian yuan
2022 fall
milestone 1

'''
import turtle
from checkers.constants import *
from checkers.board import Board
from checkers.game_state import GameState


game = GameState(turtle)
game.update()

def click_handler(x, y):
    #piece = board.get_piece(row, col)
    #print(row, col)
    #if piece != 0:
        #board.move(piece, 4, 3)
        #board.draw(turtle)
    row = int(y // (SQUARE) + NUM_SQUARES//2)
    col = int(x // (SQUARE) + NUM_SQUARES//2)
    piece = board.get_piece(row, col)
    board.move(piece, 4, 2)
    board.draw(turtle)
    

    #print(row,col)  


def main():
    #board = Board()
    #board.draw(turtle)
    #piece = board.get_piece(0, 1)
    #board.move(piece, 4, 3)
    #board.draw(turtle)

    # Click handling
    
    # This will call the click_handler
    screen = turtle.Screen()
    screen.onclick(click_handler)
    turtle.done()  # Stops the window from closing.


    


if __name__ == "__main__":
    main()
