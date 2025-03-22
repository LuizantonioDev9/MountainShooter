#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from code.Entity import Entity
from code.const import WIN_WIDTH, ENTITY_SPEED


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)


    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name] # velocidade do backgroud
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
