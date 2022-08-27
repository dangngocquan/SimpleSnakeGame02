import source
from block import Block
import block
import screenSetting

class PlayerSnake:
    def __init__(self, snake=[Block(source=source.SNAKE_HEAD)], head=[Block(source=source.SNAKE_HEAD)], 
                 body=[], tail=[], direction=None, lastDirection=None, speed=2):
        self.snake = snake
        self.head = head
        self.body = body
        self.tail = tail
        self.direction = direction
        self.lastDirection = lastDirection
        self.speed = speed
        
    def move(self):
        if self.direction == None:
            return None
        
        # Move snake head
        if self.direction != None:
            self.lastDirection = self.direction
        
        newCoordinateHead = []
        
        if self.direction == "U":
            newCoordinateHead = [self.head[0].coordinate[0], (self.head[0].coordinate[1] - block.side) % screenSetting.HEIGHT]
        elif self.direction == "D":
            newCoordinateHead = [self.head[0].coordinate[0], (self.head[0].coordinate[1] + block.side) % screenSetting.HEIGHT]
        elif self.direction == "R":
            newCoordinateHead = [(self.head[0].coordinate[0] + block.side) % screenSetting.WIDTH, self.head[0].coordinate[1]]
        elif self.direction == "L":
            newCoordinateHead = [(self.head[0].coordinate[0] - block.side) % screenSetting.WIDTH, self.head[0].coordinate[1]]
            
        if len(self.snake) >= 2:
            for i in range(len(self.snake) - 1, 0, -1):
                self.snake[i].coordinate = self.snake[i-1].coordinate
        self.snake[0].coordinate = newCoordinateHead
        self.head = self.snake[0:1]
        self.tail = self.snake[-1:0]
        
        if len(self.snake) >= 3:
            self.body = self.snake[1:-1]
        
    def update(self, foodList=[]):
        self.move()