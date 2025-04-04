#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame.display
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code import Entity
from code.Enemy import Enemy
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player
from code.const import C_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, C_GREEN, C_CYAN, EVENT_TIMEOUT, \
    TIMEOUT_STEP, TIMEOUT_LEVEL


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str,player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode  # antigo menu_return
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg')) # add na lista de entidades o bg
        player = EntityFactory.get_entity('Player1') # adiciona um player e o score
        player.score = player_score[0] # score do player 1
        self.entity_list.append(player) # append do player
        if game_mode in [MENU_OPTION[1],MENU_OPTION[2]]:
            player = EntityFactory.get_entity('Player2')  # adiciona um player e o score
            player.score = player_score[1]  # score do player 1
            self.entity_list.append(player)  # append do player
        pygame.time.set_timer(EVENT_ENEMY,SPAWN_TIME) # geração do evento enemy, para gerar a cada 2 seg
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP) #100MS CONDIÇÃO DE VITORIA


    def run(self,player_score: list[int]):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)  # desenha a img na tela
                ent.move()
                if isinstance(ent, (Player, Enemy)): # verificação de tiro
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                    if ent.name == 'Player1':
                        self.level_text(14, f'Player 1 - Health:{ent.health} / Score: {ent.score}' , C_GREEN, (10, 25))
                    if ent.name == 'Player2':
                        self.level_text(14, f'Player 2 - Health:{ent.health} / Score: {ent.score}', C_CYAN, (10, 45))
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # checa se o jogo quit para fechar
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY: # checa o spanw de inimigo
                    choice = random.choice(('Enemy1','Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice)) # add ele na lista de entidades
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0: # se chegar a zero ele retorna para o game.py e inicia o level 2
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score
                        return True

                # procurar o jogador para da gameover
                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True # se achar o jogo continua

                if not found_player: # se não achar gameover
                    return False

            # printed text HUD
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', C_WHITE, (10, 5))  # tempo de duração da fase
            self.level_text(14, f'fps: {clock.get_fps() :.0f}', C_WHITE, (10, WIN_HEIGHT - 35))  # fps em tempo real
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))  # quantas entidades na tela
            pygame.display.flip()

            #Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list) # toda a colisão vai ser feita no mediator, aqui so chamamos o metodo
            EntityMediator.verify_health(entity_list=self.entity_list)
        pass


    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
