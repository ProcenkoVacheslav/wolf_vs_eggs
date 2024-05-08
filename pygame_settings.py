import pygame as pg

pg.init()

font = pg.font.SysFont('arial', 30)
font_finish = pg.font.SysFont('arial', 60)

finish_text = font_finish.render('Игра окончена', True, (255, 0, 0))

bg_img = pg.image.load('img/bg.jpg')
egg_img = pg.image.load('img/egg.png')
player_img = pg.image.load('img/capibara.png')
