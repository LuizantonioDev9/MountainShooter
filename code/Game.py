#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Menu import Menu
from code.const import WIN_WIDTH, WIN_HEIGHT


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT)) # inicializa a janela p/ display


    def run(self):

        while True: # loop para a janela ficar rodando
            menu = Menu(self.window) # o menu vai pegar o tamanho do window
            menu.run() # rodar o menu

            pass



