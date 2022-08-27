import pygame
import block

# Player Snake
HEAD = pygame.image.load("./assets/images/playerSnake/head/head.png")
HEAD = pygame.transform.scale(HEAD, (block.side, block.side))