#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Entity import Entity
from code.PlayerShot import PlayerShot
from code.const import WIN_HEIGHT, ENTITY_SPEED, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name] # atraso no tiro para não sair tiros infinitos

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]  # center y subir o eixo y; subir é diminuir pq y x 00 é encima
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]  # center y descer no eixo y; descer é aumentar o y
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:  # center x ir para a esquerda é diminuir o eixo x
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:  # center x ir para a esquerda é aumentar o eixo x
            self.rect.centerx += ENTITY_SPEED[self.name]  # aqui eu posso usar para mudar de fase caso eu ande
            # ou caso eu derrote todos os iniimgos eu passo para o proximo level
        pass

    def shoot(self): # a classe de tiro que vai fazer o tiro sair não a entityfactory
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressd_key = pygame.key.get_pressed()
            if pressd_key[PLAYER_KEY_SHOOT[self.name]]:
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

