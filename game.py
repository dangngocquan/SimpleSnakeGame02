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
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if self.playerSnake.direction == None and self.playerSnake.lastDirection != None:
                        continue
                    if self.playerSnake.direction != "D" and self.playerSnake.checkNewHeadCoordinate("U"):
                        self.playerSnake.direction = "U"
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if self.playerSnake.direction == None and self.playerSnake.lastDirection != None:
                        continue
                    if self.playerSnake.direction != "U" and self.playerSnake.checkNewHeadCoordinate("D"):
                        self.playerSnake.direction = "D"
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if self.playerSnake.direction == None and self.playerSnake.lastDirection != None:
                        continue
                    if self.playerSnake.direction != "R" and self.playerSnake.checkNewHeadCoordinate("L"):
                        self.playerSnake.direction = "L"
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if self.playerSnake.direction == None and self.playerSnake.lastDirection != None:
                        continue
                    if self.playerSnake.direction != "L" and self.playerSnake.checkNewHeadCoordinate("R"):
                        self.playerSnake.direction = "R"
                elif event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                    if self.playerSnake.direction == None:
                        self.playerSnake.direction = self.playerSnake.lastDirection
                    else:
                        self.playerSnake.direction = None
            
    def update(self):
        if self.countTicks % (screenSetting.FPS * 10000 // self.playerSnake.speed) == 0:
            self.playerSnake.update(self.foodManager.foodList)
            self.foodManager.update(self.playerSnake.snake)
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        for food in self.foodManager.foodList:
            self.screen.blit(food.picture, food.coordinate)
        for i in range(len(self.playerSnake.snake)-1, -1, -1):
            self.screen.blit(self.playerSnake.snake[i].picture, self.playerSnake.snake[i].coordinate)
        pygame.display.flip()
    
    
