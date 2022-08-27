import random
from block import Block
import block
import source
import screenSetting

maxFood = 10

def randomCoordinateNotExisting(snake=[], foodList=[]):
    coordinateExistingList = [block.coordinate for block in snake] + [food.coordinate for food in foodList]
    if len(coordinateExistingList) == block.maxBlock:
        return None
    coordinate = [block.side * random.randint(0, screenSetting.WIDTH // block.side - 1), 
                  block.side * random.randint(0, screenSetting.HEIGHT // block.side - 1)]
    while coordinate in coordinateExistingList:
        coordinate = [block.side * random.randint(0, screenSetting.WIDTH // block.side - 1), 
                        block.side * random.randint(0, screenSetting.HEIGHT // block.side - 1)]
    return coordinate

class Food(Block):
    def __init__(self, source, coordinate=[0, 0]):
        super().__init__(source, coordinate)
        
        
class FoodManager:
    def __init__(self):
        self.foodList = []
        
    def add(self, food):
        self.foodList.append(food)
                
    def remove(self, food):
        self.foodList.remove(food)
        
    def update(self, snake=[]):
        while len(self.foodList) < maxFood:
            coordinate = randomCoordinateNotExisting(snake, foodList=self.foodList)
            if coordinate == None:
                break
            else:
                self.add(Food(source.FOOD, coordinate))
        
