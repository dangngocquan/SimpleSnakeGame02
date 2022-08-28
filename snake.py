from food import Food
import source
from block import Block
import block
import screenSetting

class PlayerSnake:
    def __init__(self, snake=[Block(source=source.SNAKE_HEAD0)], head=[Block(source=source.SNAKE_HEAD0)], 
                 body=[], tail=[], direction=None, lastDirection=None, speed=20, score=0):
        self.snake = snake
        self.head = head
        self.body = body
        self.tail = tail
        self.direction = direction
        self.lastDirection = lastDirection
        self.speed = speed
        self.countTicks = 0
        self.score = score
        
    def snakeCoordinatesList(self):
        return [block.coordinate for block in self.snake]
    
    def newHeadCoordinate(self, direction="U"):
        coordinate = self.head[0].coordinate
        if direction == "U":
            coordinate = [self.head[0].coordinate[0], (self.head[0].coordinate[1] - block.side) % screenSetting.HEIGHT]
        elif direction == "D":
            coordinate = [self.head[0].coordinate[0], (self.head[0].coordinate[1] + block.side) % screenSetting.HEIGHT]
        elif direction == "R":
            coordinate = [(self.head[0].coordinate[0] + block.side) % screenSetting.WIDTH, self.head[0].coordinate[1]]
        elif direction == "L":
            coordinate = [(self.head[0].coordinate[0] - block.side) % screenSetting.WIDTH, self.head[0].coordinate[1]]
        return coordinate
            
    def checkNewHeadCoordinate(self, direction):
        if len(self.snake) == 1:
            return True
        coordinate = self.newHeadCoordinate(direction)
        return coordinate != self.snake[1].coordinate
    
    def snakeDeath(self):
        return self.head[0].coordinate in [self.snake[i].coordinate for i in range(1, len(self.snake))]
        
    def move(self):
        if self.direction == None:
            return None
        
        if self.direction != None:
            self.lastDirection = self.direction

        newCoordinateHead = self.newHeadCoordinate(self.direction)
            
        if len(self.snake) >= 2:
            for i in range(len(self.snake) - 1, 0, -1):
                self.snake[i].coordinate = self.snake[i-1].coordinate
        self.snake[0].coordinate = newCoordinateHead
        
        self.countTicks = (self.countTicks + 1) % len(source.SNAKE_HEAD)
        for i in range(0, len(self.snake)):
            if i == 0:
                self.snake[i].picture = source.SNAKE_HEAD[self.countTicks]
            elif i == len(self.snake) - 1:
                self.snake[i].picture = source.SNAKE_TAIL[self.countTicks]
            else:
                self.snake[i].picture = source.SNAKE_BODY[self.countTicks]

        self.head = self.snake[0:1]
        if len(self.snake) >= 2:
            self.tail = self.snake[len(self.snake)-1:len(self.snake)]
        if len(self.snake) >= 3:
            self.body = self.snake[1:-1]
        
    
    def eat(self, food=Food):
        if len(self.tail) == 0:
            self.tail.append(Block(source.SNAKE_TAIL, self.head[0].coordinate))
        else:
            self.body.append(Block(source.SNAKE_BODY, self.tail[0].coordinate))
        self.snake = self.head + self.body + self.tail
        self.score += self.speed
            
    def checkFood(self, foodList=[]):
        for food in foodList:
            if self.head[0].coordinate == food.coordinate:
                self.eat(food)
                foodList.remove(food)
                break
    
    def update(self, foodList=[]):
        self.checkFood(foodList)
        self.move()