import pygame
import block

# Player Snake
SNAKE_HEAD = pygame.image.load("./assets/images/playerSnake/head/head.png")
SNAKE_HEAD = pygame.transform.scale(SNAKE_HEAD, (block.side, block.side))

SNAKE_BODY = pygame.image.load("./assets/images/playerSnake/body/body.png")
SNAKE_BODY= pygame.transform.scale(SNAKE_BODY, (block.side, block.side))

SNAKE_TAIL = pygame.image.load("./assets/images/playerSnake/tail/tail.png")
SNAKE_TAIL = pygame.transform.scale(SNAKE_TAIL, (block.side, block.side))

# Food
FOOD = pygame.image.load("./assets/images/food/food.png")
FOOD = pygame.transform.scale(FOOD, (block.side, block.side))