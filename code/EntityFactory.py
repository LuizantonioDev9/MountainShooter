#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Player import Player
from code.Enemy import Enemy
from code.const import WIN_WIDTH, WIN_HEIGHT




class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg': #bg do level 1
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}',(0,0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10,WIN_HEIGHT / 2 - 30)) # onde o player vai começar na tela posição x e y
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))  # onde o player vai começar na tela posição x e y
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40 , WIN_HEIGHT - 40))) # gerando onde os inimigos vão começar
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40))) # tbm tem a altura que pode ser alterado no +40 ou - 40