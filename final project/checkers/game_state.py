from .constants import *
from .board import Board


class GameState:
    def __init__(self, turtle):
        self.selected = None
        self.board = Board()
        self.turn = 'red'
        self.valid_moves = {}
        self.turtle = turtle

    def update(self):
        self.board.draw(self.turtle)

    def reset(self):
        self.selected = None
        self.board = Board()
        self.turn = 'red'
        self.valid_moves = {}

    def select(self, row, col):
        if(self.selected):  #if not none
            result = self._move(row, col)
            if not result:  # not valid select,select again
                self.selected = None
                self.select(row, col)
        else:        
            piece = self.board.get_piece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                return True
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            self.change_turn()
        else:
            return False
        return True

    def change_turn(self):
        if self.turn == 'red':
            self.turn = 'black'
        else:
            self.turn = 'red'
