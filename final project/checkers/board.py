import turtle
from checkers.constants import *
from checkers.piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.black_left = 12
        self.red_kings = self.black_kings = 0
        self.create_board()

    def draw_square(self, a_turtle, size):
        '''
            Function -- draw_square
                Draw a square of a given size.
            Parameters:
                a_turtle -- an instance of Turtle
                size -- the length of each side of the square
            Returns:
                Nothing. Draws a square in the graphics window.
        '''
        RIGHT_ANGLE = 90
        a_turtle.pendown()
        a_turtle.begin_fill()
        for i in range(4):
            a_turtle.forward(size)
            a_turtle.left(RIGHT_ANGLE)
        a_turtle.end_fill()
        a_turtle.penup()

    def draw_board(self, turtle):
        #Create the UI window. This should be the width of the board plus 
        turtle.setup(window_size, window_size)
        #Set the drawing canvas size. The should be actual board size
        turtle.screensize(board_size, board_size)
        turtle.bgcolor("white")  # The window's background color
        turtle.tracer(0, 0)  # makes the drawing appear immediately

        pen = turtle.Turtle()  # This variable does the drawing.
        pen.penup()  # This allows the pen to be moved.
        pen.hideturtle()  # This gets rid of the triangle cursor.

        pen.color("black", "white")  # The first parameter is the outline color
        corner = -board_size / 2 - 1
        pen.setposition(corner, corner)
        self.draw_square(pen, board_size)
        pen.color("black", SQUARE_COLORS[0])   
        for j in range(NUM_SQUARES):
            for i in range(NUM_SQUARES): 
                if i % 2 != j % 2:
                    pen.color("black", SQUARE_COLORS[0])    
                    pen.setposition(corner + SQUARE * i, corner + SQUARE * j) 
                    self.draw_square(pen, SQUARE)

    def create_board(self):
        for row in range(NUM_SQUARES):
            self.board.append([])
            for col in range(NUM_SQUARES): 
                if col % 2 != row % 2:
                    if row < 3:
                        self.board[row].append(Piece(row, col, "black"))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, "red"))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, turtle):
        self.draw_board(turtle)
        for row in range(NUM_SQUARES):
            for col in range(NUM_SQUARES):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(turtle)

    def move(self, piece, row, col):
        #swap position in List in py
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col],self.board[piece.row][piece.col]
        piece.move(row, col)
        if row == 0 or row == NUM_SQUARES:
            piece.make_king()
            if piece.color == 'red':
                self.red_kings += 1
            else:
                self.black_kings += 1

    def get_piece(self, row, col):
        return self.board[row][col]                
        
    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row
        if piece.color == 'red' or piece.king:
            moves.update(self._traverse_left(row - 1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row-3, -1), -1, piece.color, right))        
        if piece.color == 'black' or piece.king:
            moves.update(self._traverse_left(row + 1, min(row+3, NUM_SQUARES), -1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row+3, NUM_SQUARES), -1, piece.color, right))
        return moves       
            
    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0 :  #out of boundrary
                break

            current = self.board.get_piece(r, left)
            if current == 0:
                if skipped and not last:
                    break
                elif skip_only:
                    pass
                else:
                    moves[{r, left}] = last

                if last:
                    if step == -1 :
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3,NUM_SQUARES) 
                    moves.update(self._traverse_left(r + step, ))    
            elif current.color == color:
                break
            else: 
                last = [current]                   
            left -=1

        pass

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        pass        