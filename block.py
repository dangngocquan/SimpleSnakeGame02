import screenSetting

side = 25

class Block:
    def __init__(self, source, coordinate=[side * screenSetting.WIDTH//side//2, side * screenSetting.HEIGHT//side//2]):
        self.picture = source
        self.coordinate = coordinate
    
    def setPicture(self, source):
        self.picture = source
        
        
