import random


class Display(object):
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen

        self.place = self.map = self.origin_map = None
        self.reset_data()

        self.map_flag = False

    def reset_data(self):
        self.place = list()
        self.map = list()
        self.origin_map = list()
        width = self.settings.block_width + self.settings.block_space
        height = self.settings.block_height + self.settings.block_space
        for i in range(self.settings.map_size):
            self.place.append(list())
            self.map.append(list())
            self.origin_map.append(list())
            for j in range(self.settings.map_size):
                self.place[i].append((j * width + self.settings.block_space, i * height + self.settings.block_space))
                self.map[i].append((j * width, i * height, self.settings.block_width, self.settings.block_height))
                self.origin_map[i].append(self.map[i][j])
        self.map[-1][-1] = tuple()

    def draw(self):
        for i in range(self.settings.map_size):
            for j in range(self.settings.map_size):
                if self.map[i][j] == () and not self.map_flag:
                    continue
                self.screen.blit(self.settings.image, self.place[i][j],
                                 self.origin_map[i][j] if self.map_flag else self.map[i][j])

    def move(self, i, j):
        for m in range(len(self.map)):
            for n in range(len(self.map[i])):
                if self.map[m][n] == ():
                    if m == i:
                        move = 1 if j > n else -1
                        for l in range(n, j, move):
                            self.map[i][l], self.map[i][l + move] = self.map[i][l + move], self.map[i][l]
                    elif n == j:
                        move = 1 if i > m else -1
                        for l in range(m, i, move):
                            self.map[l][j], self.map[l + move][j] = self.map[l + move][j], self.map[l][j]
                    return

    def disrupt(self):
        i = j = space = None
        for m in range(len(self.map)):
            for n in range(len(self.map[m])):
                if self.map[m][n] == ():
                    space = [m, n]
        for _ in range(1000):
            flag = True
            while flag:
                i = random.randint(0, self.settings.map_size - 1)
                j = random.randint(0, self.settings.map_size - 1)
                if i == space[0] or j == space[1]:
                    space = [i, j]
                    flag = False
            self.move(i, j)
