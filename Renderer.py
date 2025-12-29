import numpy as np
import pygame
import sys
import math
from board import Connect4Board
from exeptions import BoardExceptions, GameOverException

class Renderer:
    def __init__(self):
        pygame.init()
        self.game = Game()
        self.board = self.game.get_board()

        self.player_1=Player("Player 1", 1, (12,196,239))
        self.player_2=Player("Computer", 2, (246,1,157))
        self.game_over=False
        self.turn=0

        self.square_size=100
        self.width = 7 * self.square_size
        self.height = (6 + 1) * self.square_size
        self.size = (self.width, self.height)
        self.radius= int(self.square_size/2-5)
        self.screen = pygame.display.set_mode(self.size)
        self.font = pygame.font.SysFont("Arial", 75)


        self.BLACK=(0, 0, 0)
        self.BLUE = (151,0,204)



    def draw_board(self):
        for c in range(7):
            for r in range(6):
                pygame.draw.rect(self.screen, self.BLUE, (c * self.square_size, r * self.square_size + self.square_size, self.square_size, self.square_size))
                pygame.draw.circle(self.screen, self.BLACK, (
                int(c * self.square_size + self.square_size / 2), int(r * self.square_size + self.square_size + self.square_size / 2)), self.radius)

        for c in range(7):
            for r in range(6):
                if self.board.get_piece(r, c) == self.player_1.piece:
                    pygame.draw.circle(self.screen, self.player_1.color, (
                    int(c * self.square_size + self.square_size / 2), self.height - int(r * self.square_size + self.square_size / 2)), self.radius)
                elif self.board.get_piece(r, c) == self.player_2.piece:
                    pygame.draw.circle(self.screen, self.player_2.color, (
                    int(c * self.square_size + self.square_size / 2), self.height - int(r * self.square_size + self.square_size / 2)), self.radius)
        pygame.display.update()

    def run(self):
        print(self.board)
        self.draw_board()
        pygame.display.update()

        while not self.game_over:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION and self.turn ==0:
                    pygame.draw.rect(self.screen, self.BLACK, (0, 0, self.width, self.square_size))
                    posx = event.pos[0]
                    if self.turn == 0:
                        pygame.draw.circle(self.screen, self.player_1.color, (posx, int(self.square_size / 2)), self.radius)
                    else:
                        pygame.draw.circle(self.screen, self.player_2.color, (posx, int(self.square_size / 2)), self.radius)
                pygame.display.update()
                if self.turn == 0:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.draw.rect(self.screen, self.BLACK, (0, 0, self.width, self.square_size))

                        #PLAYER 1 TURN

                        if self.turn == 0:
                            posx = event.pos[0]
                            col = int(posx // self.square_size)

                            try:
                                self.game.place_player_piece(self.player_1.piece, col)
                                self.turn = self.turn + 1
                                self.turn = self.turn % 2
                            except GameOverException as e:
                                label = self.font.render("Player 1 wins!!", 1, self.player_1.color)
                                self.screen.blit(label, (40, 10))
                                self.game_over = True

                            except BoardExceptions as e:
                                label = self.font.render(str(e), 1, self.player_1.color)
                                self.screen.blit(label, (40, 10))

                        print(self.board)
                        self.draw_board()


                        if self.game_over:
                            pygame.time.wait(3000)

                if self.turn == 1:
                    #PLAYER 2 TURN
                    try:
                        self.game.place_computer_piece(self.player_2.piece, self.player_1.piece)
                        self.turn = self.turn + 1
                        self.turn = self.turn % 2
                    except GameOverException as e:
                        label = self.font.render("Computer wins !!", 1, self.player_2.color)
                        self.screen.blit(label, (40, 10))
                        self.game_over = True

                    except BoardExceptions as e:
                        label = self.font.render(str(e), 1, self.player_1.color)
                        self.screen.blit(label, (40, 10))

                    pygame.time.wait(500)
                    print(self.board)
                    self.draw_board()


                    if self.game_over:
                        pygame.time.wait(3000)




if __name__ == "__main__":
    from game import Game
    from player import Player

    renderer = Renderer()
    renderer.run()