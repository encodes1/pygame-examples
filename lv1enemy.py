from images import get_image
import pygame
import random

class lv1enemy:
    x = 300
    y = 000
    killed = False
    bullets = {}
    def __init__(self):
        self.image = get_image('images/enemy1.png')
        pass

    def processAction(self):
        if self.killed == False:
            x = +1
            y = random.randrange(0, 5) 
            self.x = self.x+x
            self.y = self.y+y
            if(self.y) >600:
                self.kill()

    def kill(self):
        self.killed = True


    def processMove(self, key):
        pass


    def hit(self, x,y):
        if self.x > (x-10) and self.x < (x+10):
            # if self.y > (y-10) and self.y  < (y+10):
                # print("here2")
            self.kill()

    def render(self,screen):
        if self.killed == False :
            screen.blit(self.image, (self.x, self.y))

