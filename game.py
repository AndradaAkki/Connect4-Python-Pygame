import random

from board import Connect4Board
from player import Player
from exeptions import GameOverException, AlreadyFullColumnExceptions


class Game:
    def __init__(self):
        self.__board = Connect4Board()


        self.game_over = False
    def get_board(self):
        return self.__board

    def place_player_piece(self, piece, col):
        if self.__board.is_valid_location(col):
            row= self.__board.get_next_open_row(col)
            self.__board.drop_piece(row, col, piece)
            if self.__board.won(piece):
                self.game_over = True
                raise GameOverException

    def get_best_move(self, piece, opp_piece):
        for col in range (7):
            if self.__board.is_valid_computer_location(col):
                row= self.__board.get_next_open_row(col)
                self.__board.drop_piece(row, col, piece)
                if self.__board.won(piece):
                    self.__board.remove_piece(row, col, piece)
                    return col
                self.__board.remove_piece(row, col, piece)

        for col in range (7):
            if self.__board.is_valid_computer_location(col):
                row= self.__board.get_next_open_row(col)
                self.__board.drop_piece(row, col, opp_piece)
                if self.__board.won(opp_piece):
                    self.__board.remove_piece(row, col, opp_piece)
                    return col
                self.__board.remove_piece(row, col, opp_piece)

        valid_column=self.__board.get_available_col()
        col=random.randint(0,len(valid_column)-1)
        col=valid_column[col]
        return col



    def place_computer_piece(self, piece, opp_piece):

        col= self.get_best_move(piece, opp_piece)
        if self.__board.is_valid_location(col):
            row = self.__board.get_next_open_row(col)
            self.__board.drop_piece(row, col, piece)
            if self.__board.won(piece):
                self.game_over = True
                raise GameOverException

    def get_piece(self, row, col):
        return self.__board.get_piece(row, col)

    def get_board(self):
        return self.__board



