import pygame


class Functions(object):
    def __init__(self, settings, screen, display, button):
        self.settings = settings
        self.screen = screen
        self.display = display
        self.button = button

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (self.button.font_rect[0] < event.pos[0] < self.button.font_rect[0] + self.button.font_rect[2] and
                        self.button.font_rect[1] < event.pos[1] < self.button.font_rect[1] + self.button.font_rect[3]):
                    if not self.button.flag:
                        self.button.start_game()
                        return
                if not self.button.flag:
                    return
                if event.button == 1:
                    i = event.pos[1] // (self.settings.block_height + self.settings.block_space)
                    j = event.pos[0] // (self.settings.block_width + self.settings.block_space)
                    if (event.pos[1] > i * self.settings.block_height + (i + 1) * self.settings.block_space and
                            event.pos[0] > j * self.settings.block_width + (j + 1) * self.settings.block_space):
                        self.display.move(i, j)
                        self.button.check()
                elif event.button == 3:
                    self.display.map_flag = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                self.display.map_flag = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                self.display.reset_data()
                self.display.disrupt()
                self.button.start_game()
            elif event.type == pygame.USEREVENT:
                self.button.second += 1
                pygame.display.set_caption(self.button.time_format())

    def draw_screen(self):
        self.screen.fill(self.settings.background)
        self.display.draw()
        self.button.draw()
        pygame.display.flip()
