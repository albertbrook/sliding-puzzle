import pygame


class Button(object):
    def __init__(self, settings, screen, display):
        self.settings = settings
        self.screen = screen
        self.display = display

        self.font_image = self.settings.font.render(" Play ", True, self.settings.font_color)
        self.font_rect = self.font_image.get_rect()
        self.font_rect.center = self.screen.get_rect().center

        self.flag = self.second = None

    def draw(self):
        if not self.flag:
            pygame.draw.rect(self.screen, self.settings.button_color, self.font_rect)
            self.screen.blit(self.font_image, self.font_rect)

    def start_game(self):
        self.flag = True
        self.second = 0
        pygame.display.set_caption(self.time_format())
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.display.disrupt()

    def game_over(self):
        self.flag = False
        pygame.time.set_timer(pygame.USEREVENT, 0)

    def check(self):
        for i in range(len(self.display.map)):
            for j in range(len(self.display.map[i])):
                if self.display.map[i][j] != () and self.display.map[i][j] != self.display.origin_map[i][j]:
                    return
        self.game_over()

    def time_format(self):
        return "%02d:%02d:%02d" % (self.second // 3600, self.second % 3600 // 60, self.second % 60)
