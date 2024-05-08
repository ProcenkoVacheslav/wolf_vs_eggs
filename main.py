from players import *


class Main(Players):
    def __init__(self):
        super().__init__()
        self.player_rect = self.player_rect

    def main_going(self):

        while self._going:
            self.checking_exit()
            self.filling()
            self.bg_sound()

            self.score()

            self.moving()
            self.draw_player(self.player_rect.x, self.player_rect.y)

            self.draw_eggs()
            self.eggs_logic()

            self.end_game()

            self.updating()


if __name__ == "__main__":
    app = Main()
    app.main_going()
