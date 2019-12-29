import pygame


class Settings(object):
    def __init__(self):
        self.image = pygame.image.load("images/map.jpg")

        self.map_size = 3

        self.block_space = 5
        self.block_width = (self.image.get_rect().width - (self.map_size - 1) * self.block_space) // self.map_size
        self.block_height = (self.image.get_rect().height - (self.map_size - 1) * self.block_space) // self.map_size

        self.screen_size = ((self.block_width + self.block_space) * self.map_size + self.block_space,
                            (self.block_height + self.block_space) * self.map_size + self.block_space)
        self.background = (0, 0, 0)

        self.font_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.button_color = (0, 255, 0)
