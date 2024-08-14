"""This code sets up a Tetris game using Pygame, initializing necessary modules, fonts, and display elements."""

import sys
import pygame
from Game_Class import Game
from Colors_Class import Colors

pygame.init()

title_font = pygame.font.Font(None, 30)
score_surface = title_font.render("Score", True, Colors.white)
high_surface = title_font.render("Highest Score", True, Colors.white)
next_surface = title_font.render("Next Brick", True, Colors.white)
controls_surface = title_font.render("Controls", True, Colors.white)
level_surface = title_font.render("Level", True, Colors.white)
game_over_surface = title_font.render("GAME OVER!!!", True, Colors.red)
pause_surface = title_font.render("Paused!!!", True, Colors.white)

score_rect = pygame.Rect(19, 5, 170, 80)
high_score = pygame.Rect(19, 97, 170, 80)
next_rect = pygame.Rect(510, 5, 170, 180)
grid_rect = pygame.Rect(192, 5, 315, 610)
controls_rect = pygame.Rect(19, 435, 170, 180)
level_rect = pygame.Rect(510, 435, 170, 180)

screen = pygame.display.set_mode((700, 620))
pygame.display.set_caption("Tetris Game")

clock = pygame.time.Clock()

game = Game()
bg_image = pygame.image.load("image-asset.png").convert()
controls_img = pygame.image.load("controls.png").convert()
controls_blitz_img = pygame.transform.scale(controls_img, (150, 160))


GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False and game.pause == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False and game.pause == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False and game.pause == False:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and game.game_over == False and game.pause == False:
                game.rotate()
            if event.key == pygame.K_SPACE:
                game.pause = not game.pause
            if event.key == pygame.K_p:
                if game.is_music_paused:
                    game.play_music()
                else:
                    game.pause_music()
        if event.type == GAME_UPDATE and game.game_over == False and game.pause == False:
            game.move_down()

    # Drawing the pygame canvas
    score_value_surface = title_font.render(str(game.score), True, Colors.white)
    high_score_value_surface = title_font.render(str(game.get_highest_score()), True, Colors.white)
    screen.fill(Colors.dark_blue)

    screen.blit(bg_image, (0, 0))


    pygame.draw.rect(screen, Colors.dark_gray, score_rect)
    pygame.draw.rect(screen, Colors.dark_gray, high_score)
    pygame.draw.rect(screen, Colors.dark_gray, next_rect)
    pygame.draw.rect(screen, Colors.dark_gray, grid_rect)
    pygame.draw.rect(screen, Colors.dark_gray, controls_rect)
    pygame.draw.rect(screen, Colors.dark_gray, level_rect)

    pygame.draw.rect(screen, Colors.light_blue, grid_rect)
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 6, 0)
    pygame.draw.rect(screen, Colors.light_blue, high_score, 6, 0)
    pygame.draw.rect(screen, Colors.light_blue, controls_rect, 6, 0)
    pygame.draw.rect(screen, Colors.light_blue, level_rect, 6, 0)
    screen.blit(score_value_surface,
                score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery + 15))
    screen.blit(high_score_value_surface,
                high_score_value_surface.get_rect(centerx=high_score.centerx, centery=high_score.centery + 15))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 6, 0)

    screen.blit(controls_blitz_img, (29,445), )
    screen.blit(score_surface, (75, 13, 50, 50))
    screen.blit(high_surface, (40, 105, 50, 50))
    screen.blit(next_surface, (545, 13, 50, 50))
    screen.blit(controls_surface, (60, 450, 50, 50))
    screen.blit(level_surface, (570, 450, 50, 50))
    if game.game_over == True:
        screen.blit(game_over_surface, (530, 300, 50, 50))
        # file = open("highscore.txt", "r")
        with open("highscore.txt", "r") as file:
            content = file.read()
            content = int(content)
            test_score = int(game.score)

        if content < test_score:
            with open("highscore.txt", "w") as file:
                file.write(str(game.score))
            print(game.score)
    if game.pause == True:
        screen.blit(pause_surface, (530, 300, 50, 50))
    game.draw(screen)
    pygame.display.update()
    clock.tick(60)
