from images import get_image
import pygame
import random

class lv1enemy:
    x = 300
    y = 000
    killed = False
    bullets = {}
    def __init__(self):

        pass

    def processAction(self):
        if self.killed == False:
            x = +1
            y = random.randrange(-3, +10) 
            self.x = self.x+x
            self.y = self.y+y
            if(self.y) >600:
                self.kill()

    def kill(self):
        self.killed = True


    def processMove(self, key):
        pass


    def render(self,screen):
        if self.killed == False :
            screen.blit(get_image('images/enemy1.png'), (self.x, self.y))

