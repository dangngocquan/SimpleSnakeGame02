import source
from block import Block
import block
import screenSetting

# class PlayerSnakeHead:
#     def __init__(self):
#         self.picture



class PlayerSnake:
    def __init__(self, length=1, snake=[Block(source=source.SNAKE_HEAD)], head=[Block(source=source.SNAKE_HEAD)], 
                 body=[], tail=[], direction=None, lastDirection=None, speed=31):
        self.length = length
        self.snake = snake
        self.head = head
        self.body = body
        self.tail = tail
        self.moving = False
        self.stopping = True
        self.direction = direction
        self.lastDirection = lastDirection
        self.speed = speed
        
    def update(self):
        if self.direction != None:
            self.lastDirection = self.direction
        
        if self.direction == "U":
            self.head[0].coordinate[1] = (self.head[0].coordinate[1] - block.side) % screenSetting.HEIGHT
        elif self.direction == "D":
            self.head[0].coordinate[1] = (self.head[0].coordinate[1] + block.side) % screenSetting.HEIGHT
        elif self.direction == "R":
            self.head[0].coordinate[0] = (self.head[0].coordinate[0] + block.side) % screenSetting.WIDTH
        elif self.direction == "L":
            self.head[0].coordinate[0] = (self.head[0].coordinate[0] - block.side) % screenSetting.WIDTH
        
        if len(self.snake) > 1:
            for i in range(len(self.snake)-1, 0, -1):
                self.snake[i].coordinate = self.snake[i-1].coordinate
            self.tail = self.snake[-1: 0]
        if len(self.snake) >= 3:
            self.body = self.snake[1:-1]
            
        self.snake = self.head + self.body + self.tail