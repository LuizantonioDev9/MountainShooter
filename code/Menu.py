#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.const import WIN_WIDTH, COLOR_ORANGE, COLOR_WHITE, MENU_OPTION


class Menu:
    def __init__(self, window):
        self.window = window  # menu recebe a janela do game
        self.surf = pygame.image.load('./asset/MenuBg.png')  # vai carregar a imagem do bg
        self.rect = self.surf.get_rect(left=0, top=0)  # retangulo vazio onde a imagem vai começar

    def run(self):
        pygame.mixer_music.load('./asset/Menu.mp3')  # carregar a musica
        pygame.mixer_music.play(-1)  # fazer a musica tocar em loop

        while True:  # loop para carregar a imagem
            self.window.blit(source=self.surf,
                             dest=self.rect)  # da onde está surgindo o bg e para onde vai ser aplicado

            # Textos menu
            self.menu_text(80, "Mountain", COLOR_WHITE, ((WIN_WIDTH / 2), 70))
            self.menu_text(70, "Shooter", COLOR_WHITE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(30, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()  # inicia o display

            # checando todos os eventos
            for event in pygame.event.get():  # vai varrer todos os eventos do pygame.event
                if event.type == pygame.QUIT:  # caso o tipo do event seja QUIT, ou seja se eu fechar a janela
                    quit()  # o pygame vai fechar a janela

    # igual a imagem mais utilizamos o texto
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        # passamos a font e o tamanho que vamos querer via parametro
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)

        # convertemos a font para uma imagem
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()

        # e passamos essa imagem para o retangulo
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)

        # da origem para o destino
        self.window.blit(source=text_surf, dest=text_rect)
