"""The Game class manages the Tetris game's state, including the grid, blocks, current and next blocks, score,
sounds, and gameplay mechanics such as block movement, rotation, and collision detection."""

from Grid_Class import Grid
from Diff_Blocks import *
import random
import pygame
class Game:
    def __init__(self):
        # Initialize the game grid and blocks
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(),LBlock(),  OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.pause =  False
        self.score = 0
        # Load sound effects
        self.rotate_sound = pygame.mixer.Sound("Sounds/rotate.ogg")
        self.clear_sound = pygame.mixer.Sound("Sounds/clear.ogg")

        # Load and play background music
        pygame.mixer.music.load("Sounds/music.ogg")
        pygame.mixer.music.play(-1)

    # Update the game score based on lines cleared and move down points
    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        self.score += move_down_points

    # Get a random block from the list of blocks
    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(),LBlock(),  OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    # Move the current block left by one column
    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, 1)

    # Move the current block right by one column
    def move_right(self):
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, -1)

    # Move the current block down by one row
    def move_down(self):
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lock_block()

    # Lock the current block in place and check for full rows to clear
    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        if rows_cleared > 0:
            self.clear_sound.play()
            self.update_score(rows_cleared, 0)
        if self.block_fits() == False:
            self.game_over = True

    # Reset the game to its initial state
    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    # Check if the current block fits in its position on the grid
    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True

    # Rotate the current block with sound effect
    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotation()
        else:
            self.rotate_sound.play()

    # Check if the current block is inside the grid boundaries
    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True

    # Draw the game grid and the current block on the screen
    def draw(self, screen):
        self.grid.draw(screen)

        ###NOTE change offset to 200
        self.current_block.draw(screen, 200, 11 )
        if self.next_block.id == 3:
            self.next_block.draw(screen, 445, 86)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 445, 76)
        else:
            self.next_block.draw(screen, 460, 66)