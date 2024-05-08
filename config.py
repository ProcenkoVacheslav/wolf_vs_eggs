from pygame_settings import *
from settings import *

import pygame as pg


class Config:
    def __init__(self):
        self._app = pg.display.set_mode((WIDTH, HEIGHT))
        self._clock = pg.time.Clock()
        self._bottom = pg.Rect(0, HEIGHT, WIDTH, 5)
        self._going = True
        self._score = 0
        self._max_score = self.get_record()
        self._moving = True
        self._end_game = False
        self._eggs = []
        self._event = ''

    @staticmethod
    def get_record():
        try:
            with open('files/records.txt', 'r') as file:
                return int(file.readline()[:-1])
        except FileNotFoundError:
            with open('files/records.txt', 'w') as file:
                file.write(f'0\n')
                return 0

    @staticmethod
    def save_max_score(max_score):
        with open('files/records.txt', 'w') as file:
            file.write(f'{max_score}\n')

    def checking_exit(self):
        for self._event in pg.event.get():
            if self._event.type == pg.QUIT:
                if self._score > self._max_score:
                    self._max_score = self._score
                    self.save_max_score(self._max_score)
                self._going = False

    def filling(self):
        self._app.blit(bg_img, (0, 0))
        pg.draw.rect(self._app, (255, 255, 0), self._bottom)

    def updating(self):
        self._clock.tick(FPS)
        pg.display.update()
