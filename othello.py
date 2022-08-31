# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 23:53:13 2022

@author: rijuj
"""

import pygame
import ui
import player
import board
from config import BLACK, WHITE, HUMAN
import log
import time
import numpy as np

logger = log.setup_custom_logger('root')


class Othello:
    """this is the main class to run"""

    def __init__(self):
        """ Show options screen and start game modules"""
        # start
        self.gui = ui.Gui()
        self.board = board.Board()
        self.gui.show_menu(self.start)
        self.epsilon = 1.0          # exploration probability at start
        self.epsilon_min = 0.01     # minimum exploration probability
        self.epsilon_decay = 0.0005  # exponential decay rate for exploration prob
        self.counter = 0
        

    def start(self, *args):
        """this set of code was manipulated to make the program run AIvsAI, AIvsHuman, AIvsRandomPlayer and AIvsMinimax"""
        player1, player2, self.epoch = args
        logger.info('Settings: player 1: %s, player 2: %s, level: %s ', player1, player2, self.epoch)
        if player1 == HUMAN:
            self.now_playing = player.Human(self.gui, BLACK)
        else:
            self.now_playing = player.Computer(BLACK)
        if player2 == HUMAN:
            self.other_player = player.Human(self.gui, WHITE)
        else:
            self.other_player = player.Computer(WHITE)

        self.gui.show_game()
        self.gui.update(self.board.board, 2, 2, self.now_playing.color)

    def run(self):
        clock = pygame.time.Clock()
        start_time = time.time()
        
        while self.counter<self.epoch:
            self.board = board.Board()
            self.gui.show_game()
            while True:
                clock.tick(60)
                """Check if game has ended"""
                if self.board.game_ended():
                    whites, blacks, empty = self.board.count_stones()
                    if whites > blacks:
                        winner = WHITE
                        if self.now_playing.get_color() == WHITE:
                            self.now_playing.win()
                            self.other_player.lose()
                        else:
                            self.now_playing.lose()
                            self.other_player.win()
                    elif blacks > whites:
                        winner = BLACK
                        if self.now_playing.get_color() == BLACK:
                            self.now_playing.win()
                            self.other_player.lose()
                        else:
                            self.now_playing.lose()
                            self.other_player.win()
                    else:
                        winner = None
                        self.now_playing.draw()
                        self.other_player.draw()
                    break
                self.now_playing.get_current_board(self.board)
                valid_moves = self.board.get_valid_moves(self.now_playing.color)
                if valid_moves != []:
                    """code for calling Minimax AI is different"""
                    if self.now_playing.get_color() == WHITE:
                        discardedFunc, self.board = self.now_playing.get_move()
                    else:
                        self.board = self.now_playing.get_move(self.epsilon)
                    whites, blacks, empty = self.board.count_stones()
                    self.gui.update(self.board.board, blacks, whites,
                                    self.now_playing.color)
                self.now_playing, self.other_player = self.other_player, self.now_playing
            self.gui.show_winner(winner)
            
            self.counter += 1
            """epsilon decay"""
            if self.epsilon > self.epsilon_min:
                self.epsilon *= (1-self.epsilon_decay)
            
            pygame.time.wait(1000)
            
            """Printing accumulated results every 100 episodes"""
            if self.counter % 100 == 0:
                print("Pass Completed: ", self.counter)
                print("Draw : ", self.now_playing.getDraw())
                print("1 is BLACK ", self.now_playing.get_color(), self.now_playing.getWin())
                print("2 is WHITE ", self.other_player.get_color(), self.other_player.getWin())
        """Printing final QTables"""
        print("--- %s seconds elapsed ---" % (time.time() - start_time))
        print("Pass Completed: ", self.counter)
        print("Draw : ", self.now_playing.getDraw())
        print("1 is BLACK ", self.now_playing.get_color(), self.now_playing.getWin())
        print("2 is WHITE ", self.other_player.get_color(), self.other_player.getWin())
        print(np.matrix(self.now_playing.qTable.get_qTable()))
        print(np.matrix(self.other_player.qTable.get_qTable()))

    def restart(self, showMenu):
        self.counter += 1
        self.board = board.Board()
        
        if showMenu == 'true':
            self.gui.show_menu(self.start)
        else:
            self.gui.show_game()
        self.run()


def main():
    game = Othello()
    game.run()


if __name__ == '__main__':
    main()
