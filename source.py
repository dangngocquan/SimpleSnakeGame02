import pygame
import block

# Player Snake
SNAKE_HEAD = pygame.image.load("./assets/images/playerSnake/head/head.png")
SNAKE_HEAD = pygame.transform.scale(SNAKE_HEAD, (block.side, block.side))

# Food
FOOD = pygame.image.load("./assets/images/food/food.png")
FOOD = pygame.transform.scale(FOOD, (block.side, block.side))