import pygame
import block

# Player Snake
SNAKE_HEAD0 = pygame.image.load("./assets/images/playerSnake/head/head0.png")
SNAKE_HEAD0 = pygame.transform.scale(SNAKE_HEAD0, (block.side, block.side))
SNAKE_HEAD1 = pygame.image.load("./assets/images/playerSnake/head/head1.png")
SNAKE_HEAD1 = pygame.transform.scale(SNAKE_HEAD1, (block.side, block.side))
SNAKE_HEAD2 = pygame.image.load("./assets/images/playerSnake/head/head2.png")
SNAKE_HEAD2 = pygame.transform.scale(SNAKE_HEAD2, (block.side, block.side))
SNAKE_HEAD3 = pygame.image.load("./assets/images/playerSnake/head/head3.png")
SNAKE_HEAD3 = pygame.transform.scale(SNAKE_HEAD3, (block.side, block.side))
SNAKE_HEAD4 = pygame.image.load("./assets/images/playerSnake/head/head4.png")
SNAKE_HEAD4 = pygame.transform.scale(SNAKE_HEAD4, (block.side, block.side))
SNAKE_HEAD5 = pygame.image.load("./assets/images/playerSnake/head/head5.png")
SNAKE_HEAD5 = pygame.transform.scale(SNAKE_HEAD5, (block.side, block.side))
SNAKE_HEAD = [SNAKE_HEAD0, SNAKE_HEAD1, SNAKE_HEAD2, SNAKE_HEAD3, SNAKE_HEAD4, SNAKE_HEAD5]

SNAKE_BODY0 = pygame.image.load("./assets/images/playerSnake/body/body0.png")
SNAKE_BODY0 = pygame.transform.scale(SNAKE_BODY0, (block.side, block.side))
SNAKE_BODY1 = pygame.image.load("./assets/images/playerSnake/body/body1.png")
SNAKE_BODY1 = pygame.transform.scale(SNAKE_BODY1, (block.side, block.side))
SNAKE_BODY2 = pygame.image.load("./assets/images/playerSnake/body/body2.png")
SNAKE_BODY2 = pygame.transform.scale(SNAKE_BODY2, (block.side, block.side))
SNAKE_BODY3 = pygame.image.load("./assets/images/playerSnake/body/body3.png")
SNAKE_BODY3 = pygame.transform.scale(SNAKE_BODY3, (block.side, block.side))
SNAKE_BODY4 = pygame.image.load("./assets/images/playerSnake/body/body4.png")
SNAKE_BODY4 = pygame.transform.scale(SNAKE_BODY4, (block.side, block.side))
SNAKE_BODY5 = pygame.image.load("./assets/images/playerSnake/body/body5.png")
SNAKE_BODY5 = pygame.transform.scale(SNAKE_BODY5, (block.side, block.side))
SNAKE_BODY = [SNAKE_BODY0, SNAKE_BODY1, SNAKE_BODY2, SNAKE_BODY3, SNAKE_BODY4, SNAKE_BODY5]

SNAKE_TAIL0 = pygame.image.load("./assets/images/playerSnake/tail/tail0.png")
SNAKE_TAIL0 = pygame.transform.scale(SNAKE_TAIL0, (block.side, block.side))
SNAKE_TAIL1 = pygame.image.load("./assets/images/playerSnake/tail/tail1.png")
SNAKE_TAIL1 = pygame.transform.scale(SNAKE_TAIL1, (block.side, block.side))
SNAKE_TAIL2 = pygame.image.load("./assets/images/playerSnake/tail/tail2.png")
SNAKE_TAIL2 = pygame.transform.scale(SNAKE_TAIL2, (block.side, block.side))
SNAKE_TAIL3 = pygame.image.load("./assets/images/playerSnake/tail/tail3.png")
SNAKE_TAIL3 = pygame.transform.scale(SNAKE_TAIL3, (block.side, block.side))
SNAKE_TAIL4 = pygame.image.load("./assets/images/playerSnake/tail/tail4.png")
SNAKE_TAIL4 = pygame.transform.scale(SNAKE_TAIL4, (block.side, block.side))
SNAKE_TAIL5 = pygame.image.load("./assets/images/playerSnake/tail/tail5.png")
SNAKE_TAIL5 = pygame.transform.scale(SNAKE_TAIL5, (block.side, block.side))
SNAKE_TAIL = [SNAKE_TAIL0, SNAKE_TAIL1, SNAKE_TAIL2, SNAKE_TAIL3, SNAKE_TAIL4, SNAKE_TAIL5]

# Food
FOOD = pygame.image.load("./assets/images/food/food.png")
FOOD = pygame.transform.scale(FOOD, (block.side, block.side))