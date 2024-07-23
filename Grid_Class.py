"""The Grid class manages a 20x10 grid for a Tetris game, handling grid initialization, checking cell status,
clearing and moving rows, resetting the grid, and drawing the grid on a Pygame screen.
"""
import pygame


class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = self.get_cell_colors()

    def get_cell_colors(self):
        dark_gray = (26, 31, 40)
        green = (47, 230, 23)
        red = (232, 18, 18)
        orange = (226, 116, 17)
        yellow = (237, 234, 4)
        purple = (166, 0, 247)
        cyan = (21, 204, 209)
        blue = (13, 64, 216)
        white = (255, 255, 255)
        dark_blue = (44, 44, 127)
        light_blue = (59, 85, 162)
        return [dark_gray, green, red, orange, yellow, purple, cyan, blue]

    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column * self.cell_size  +1, row * self.cell_size +1, self.cell_size-1,
                                        self.cell_size-1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)