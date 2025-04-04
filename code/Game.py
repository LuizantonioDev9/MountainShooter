#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Level import Level
from code.Menu import Menu
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT)) # inicializa a janela p/ display


    def run(self):
        while True: # loop para a janela ficar rodando
            menu = Menu(self.window) # o menu vai pegar o tamanho do window
            menu_return = menu.run() # rodar o menu

            if menu_return in [MENU_OPTION[0],MENU_OPTION[1],MENU_OPTION[2]]:
                player_score = [0, 0] # [Player1, Player2] manter o score para o outro level
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)

            elif menu_return == MENU_OPTION[4]:
                quit()
            else:
                pass




