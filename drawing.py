from sounds import *


class Drawing(Sounds):

    def __init__(self):
        super().__init__()

        self._button = pg.Rect(BUTTON_POS_X, BUTTON_POS_Y, BUTTON_SIZE_X, BUTTON_SIZE_Y)
        self._button_rect = (BUTTON_POS_X, BUTTON_POS_Y, BUTTON_SIZE_X, BUTTON_SIZE_Y)
        self._button_color = (255, 255, 255)
        self.__init_button()

    def __init_button(self):
        self._cur_button_color = self._button_color
        self.retry_text = font_finish.render('Заново', True, self._cur_button_color)
        self.retry_text_pos_x = WIDTH // 2 - self.retry_text.get_width() // 2
        self.retry_text_pos_y = BUTTON_POS_Y - 2

    def __draw_button(self):
        mouse_pos = pg.mouse.get_pos()

        if self._button.collidepoint(mouse_pos):
            self._button_color = (0, 0, 0)
            self.__init_button()
        else:
            self._button_color = (255, 255, 255)
            self.__init_button()

        if self._event.type == pg.MOUSEBUTTONDOWN:
            if self._button.collidepoint(mouse_pos):
                self._end_game = False
                self._moving = True
                self.player_rect = pg.Rect(WIDTH // 2 - 25, 500, PLAYER_SIZE, PLAYER_SIZE)

        pg.draw.rect(self._app, self._cur_button_color, self._button_rect, 5)
        self._app.blit(self.retry_text, (self.retry_text_pos_x, self.retry_text_pos_y))

    def score(self):
        cur_text = font.render(f'Текущий счёт {self._score}', True, (255, 0, 0))
        max_text = font.render(f'Максимальный счёт {self._max_score}', True, (255, 0, 0))
        self._app.blit(cur_text, (10, 10))
        self._app.blit(max_text, (10, 50))

    def draw_player(self, pos_x, pos_y):
        self._app.blit(player_img, (pos_x, pos_y))

    def draw_eggs(self):
        for egg in self._eggs:
            self._app.blit(egg_img, (egg.x, egg.y))

    def end_game(self):
        if self._end_game:

            self._app.blit(finish_text,
                           ((WIDTH // 2 - finish_text.get_width() // 2),
                            (HEIGHT // 2 - finish_text.get_height() // 2)))

            self.__draw_button()
