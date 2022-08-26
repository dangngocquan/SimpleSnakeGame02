import pygame
import screenSetting
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screenSetting.WIDTH, screenSetting.HEIGHT))
        pygame.display.set_caption("Simple Snake")
        
        self.clock = pygame.time.Clock()
        
        self.running = True
        self.waiting = True
        self.lose = False
    
    def run(self):
        while self.running:
            self.clock.tick(screenSetting.FPS)
            self.event()
            self.update()
            self.draw()
    
    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.K_SPACE:
                self.waiting = True
            
    def update(self):
        pass
    
    def draw(self):
        image1 = pygame.image.load("./assets/images/background03.png")
        image1 = pygame.transform.scale(image1, (screenSetting.WIDTH/2, screenSetting.HEIGHT))
        image2 = pygame.image.load("./assets/images/background03.png")
        image2 = pygame.transform.scale(image2, (screenSetting.WIDTH/2, screenSetting.HEIGHT))
        self.screen.blit(image1, (0, 0))
        self.screen.blit(image2, (50, 0))
        pygame.display.flip()
    
    
