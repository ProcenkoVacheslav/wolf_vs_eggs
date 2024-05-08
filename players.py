from drawing import *
import random


class Players(Drawing):

    def __init__(self):
        super().__init__()
        self.player_rect = pg.Rect(WIDTH // 2 - 25, 500, PLAYER_SIZE, PLAYER_SIZE)

    def moving(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_w] and self.player_rect.y > HEIGHT - 200 and self._moving:
            self.player_rect.y -= SPEED
        if keys[pg.K_s] and self.player_rect.y < HEIGHT - PLAYER_SIZE and self._moving:
            self.player_rect.y += SPEED
        if keys[pg.K_a] and self.player_rect.x > 0 and self._moving:
            self.player_rect.x -= SPEED
        if keys[pg.K_d] and self.player_rect.x < WIDTH - PLAYER_SIZE and self._moving:
            self.player_rect.x += SPEED

        return self.player_rect

    def eggs_logic(self):
        if (not self._eggs or self._eggs[-1].y > 200) and not self._end_game:
            self._eggs.append(pg.Rect(random.randint(20, WIDTH - EGG_SIZE_X - 20), -EGG_SIZE_Y, EGG_SIZE_X, EGG_SIZE_Y))

        for egg in self._eggs:
            egg.y += EGG_SPEED

            if egg.colliderect(self._bottom):
                self._eggs.remove(egg)
                self._end_game = True
                self._moving = False
                self._eggs.clear()
                self.loose_sound()
                if self._score > self._max_score:
                    self._max_score = self._score
                    self.save_max_score(self._max_score)
                self._score = 0

            if egg.colliderect(self.player_rect):
                self._eggs.remove(egg)
                self._score += 1
                self.ball_sound()
