from code.Entity import Entity
from code.const import ENTITY_SPEED


class PlayerShot(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self,):
        self.rect.centerx += ENTITY_SPEED[self.name] # posição da onde o tiro vai sair, vem da direita para esquerda