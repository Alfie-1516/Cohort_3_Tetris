"""The Grid class manages a 20x10 grid for a Tetris game, handling grid initialization, checking cell status,
clearing and moving rows, resetting the grid, and drawing the grid on a Pygame screen.
"""
import pygame
from Colors_Class import Colors


class Grid:
    def __init__(self):
        # Initialize grid dimensions and cell size
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        # Initialize a 2D grid with zeros
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]

        # Get colors for cells from Colors class
        self.colors = Colors.get_cell_colors()

    # Print the grid to console (for debugging)
    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")
            print()


    def is_inside(self, row, column):
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False

    # Draw the grid on the screen
    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                # Define rectangle for each cell to draw
                cell_rect = pygame.Rect(column * self.cell_size  +1, row * self.cell_size +1, self.cell_size -1,
                                        self.cell_size -1)
                # Draw the cell with corresponding color
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)