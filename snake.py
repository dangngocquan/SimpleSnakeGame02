from food import Food
import source
from block import Block
import block
import screenSetting

class PlayerSnake:
    def __init__(self, snake=[Block(source=source.SNAKE_HEAD)], head=[Block(source=source.SNAKE_HEAD)], 
                 body=[], tail=[], direction=None, lastDirection=None, speed=20):
        self.snake = snake
        self.head = head
        self.body = body
        self.tail = tail
        self.direction = direction
        self.lastDirection = lastDirection
        self.speed = speed
        
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
        coordinate = self.newHeadCoordinate(direction)
        return not (coordinate in self.snakeCoordinatesList())    
    
    def snakeDeath(self, direction):
        pass
        
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
            
    def checkFood(self, foodList=[]):
        for food in foodList:
            if self.head[0].coordinate == food.coordinate:
                self.eat(food)
                foodList.remove(food)
                break
    
    def update(self, foodList=[]):
        self.checkFood(foodList)
        self.move()