from .constants import *


class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.cal_pos()

    def cal_pos(self):
        self.x = SQUARE * self.col + SQUARE//2 
        self.y = SQUARE * self.row  

    def make_king(self):
        self.king = True

    def draw_circle(self, a_turtle, size):
        '''
            Function -- draw_circle
                Draw a circle with a given radius.
            Parameters:
                a_turtle -- an instance of Turtle
                size -- the radius of the circle
            Returns:
                Nothing. Draws a circle in the graphics windo.
        '''

        a_turtle.pendown()
        a_turtle.begin_fill()
        a_turtle.circle(size)
        a_turtle.end_fill()
        a_turtle.penup()        

    def draw(self, turtle):
        pen = turtle.Turtle()  # This variable does the drawing.
        pen.penup()  # This allows the pen to be moved.
        pen.hideturtle()
        pen.color(self.color)
        corner = -board_size / 2 - 1
        pen.setposition(corner + self.x, corner + self.y)
        self.draw_circle(pen, SQUARE/2)

    def __repr__(self):
        return str(self.color) 

    def move(self, new_row, new_col):
        self.row = new_row
        self.col = new_col
        self.cal_pos()            

