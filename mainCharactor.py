from images import get_image
import pygame

class mainCharactor:
    x = 300
    y = 600
    MOVE_UP = pygame.K_UP
    MOVE_DOWN = pygame.K_DOWN
    MOVE_LEFT = pygame.K_LEFT
    MOVE_RIGHT =pygame.K_RIGHT
    movekeys = [MOVE_UP, MOVE_DOWN,MOVE_LEFT,MOVE_RIGHT] 
    actionkeys = []
    
    def __init__(self):

        pass

    def processAction(self,key):
        if key[self.MOVE_UP] :
            self.processMove(key)

        if key[self.MOVE_DOWN] :
            self.processMove(key)

        if key[self.MOVE_LEFT] :
            self.processMove(key)

        if key[self.MOVE_RIGHT] :
            self.processMove(key)

        if key[pygame.K_SPACE]:
            self.shoot(key)
        # if key[pygame.K_UP]: self.charactor.processAction(pygame.K_UP)
        # if pressed_keys[pygame.K_DOWN]:  self.charactor.processAction(pygame.K_DOWN)
        # if pressed_keys[pygame.K_LEFT]:  self.charactor.processAction(pygame.K_LEFT)
        # if pressed_keys[pygame.K_RIGHT]: self.charactor.processAction(pygame.K_RIGHT)
        if(key in self.movekeys):
            self.processMove(key)   

        # if(key in self.actionkeys):
        #     return      

    def shoot(self,key):
        print "here"

    def processMove(self, key):
        if key[self.MOVE_UP]  : self.y -= 3
        if key[self.MOVE_DOWN]: self.y += 3
        if key[self.MOVE_LEFT]: self.x -= 3
        if key[self.MOVE_RIGHT]: self.x += 3
        return


    def render(self,screen):
        screen.blit(get_image('images/ship.png'), (self.x, self.y))

