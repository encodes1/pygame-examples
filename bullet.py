class bullet:
    def __init__(self,x,y,speed):
        self.x = x
        self.y = y
        self.speed = speed

    def move(self):
        self.y = self.y - self.speed
