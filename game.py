import pygame
from food import FoodManager, Food
import screenSetting
import sys
from snake import PlayerSnake

class Game:
    def __init__(self, playerSnake=PlayerSnake(), foodManager=FoodManager(), score=0):
        pygame.init()
        self.screen = pygame.display.set_mode((screenSetting.WIDTH, screenSetting.HEIGHT))
        pygame.display.set_caption("Simple Snake")
        
        self.clock = pygame.time.Clock()
        self.countTicks = 0
        self.running = True
        self.waiting = True
        self.lose = False
        self.score = score
        self.playerSnake = playerSnake
        self.foodManager = foodManager
    
    def run(self):
        while self.running:
            self.clock.tick(screenSetting.FPS)
            self.event()
            for i in range(10000):
                self.countTicks = (self.countTicks + 1) % (screenSetting.FPS * 10000)
                self.update()
            self.draw()
    
    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if self.playerSnake.direction == None and self.playerSnake.lastDirection != None:
                        continue
                    if self.playerSnake.direction != "D":
                        self.playerSnake.direction = "U"
                elif event.key == pygame.K_DOWN:
                    if self.playerSnake.direction == None and self.playerSnake.lastDirection != None:
                        continue
                    if self.playerSnake.direction != "U":
                        self.playerSnake.direction = "D"
                elif event.key == pygame.K_LEFT:
                    if self.playerSnake.direction == None and self.playerSnake.lastDirection != None:
                        continue
                    if self.playerSnake.direction != "R":
                        self.playerSnake.direction = "L"
                elif event.key == pygame.K_RIGHT:
                    if self.playerSnake.direction == None and self.playerSnake.lastDirection != None:
                        continue
                    if self.playerSnake.direction != "L":
                        self.playerSnake.direction = "R"
                elif event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                    if self.playerSnake.direction == None:
                        self.playerSnake.direction = self.playerSnake.lastDirection
                    else:
                        self.playerSnake.direction = None
            
    def update(self):
        if self.countTicks % (screenSetting.FPS * 10000 // self.playerSnake.speed) == 0:
            self.playerSnake.update()
            self.foodManager.update(self.playerSnake.snake)
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        for block in self.playerSnake.snake:
            self.screen.blit(block.picture, block.coordinate)
        for food in self.foodManager.foodList:
            self.screen.blit(food.picture, food.coordinate)
        pygame.display.flip()
    
    
