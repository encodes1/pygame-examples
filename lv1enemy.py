from images import get_image
import pygame
import random

class lv1enemy:
    x = 300
    y = 000
    MOVE_UP = pygame.K_UP
    MOVE_DOWN = pygame.K_DOWN
    MOVE_LEFT = pygame.K_LEFT
    MOVE_RIGHT =pygame.K_RIGHT
    movekeys = [MOVE_UP, MOVE_DOWN,MOVE_LEFT,MOVE_RIGHT] 
    actionkeys = []
    
    def __init__(self):

        pass

    def processAction(self):
        x = random.randrange(-3, +3) 
        y = random.randrange(-3, +10) 
        self.x = self.x+x
        self.y = self.y+y
        if(self.y) >600:
            self.y = 600
        


    def processMove(self, key):
        pass


    def render(self,screen):
        screen.blit(get_image('images/enemy1.png'), (self.x, self.y))

