import pygame
import images
from mainCharactor import mainCharactor
from lv1enemy import lv1enemy

class SceneBase:
    def __init__(self):
        self.next = self
    
    def ProcessInput(self, events, pressed_keys):
        print("uh-oh, you didn't override this in the child class")

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene
    
    def Terminate(self):
        self.SwitchToScene(None)


def run_game(width, height, fps, starting_scene):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    active_scene = starting_scene

    while active_scene != None:
        pressed_keys = pygame.key.get_pressed()
        
        # Event filtering 
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True
            
            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)
        
        active_scene.ProcessInput(filtered_events, pressed_keys)
        active_scene.Update()
        active_scene.Render(screen)
        
        active_scene = active_scene.next
        
        pygame.display.flip()
        clock.tick(fps)

# The rest is code where you implement your game using the Scenes model 


class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter 
                self.SwitchToScene(Level1())
    
    def Update(self):
        pass
    
    def Render(self, screen):
        # For the sake of brevity, the title scene is a blank red screen 
        screen.fill((255, 0, 0))

class Level1(SceneBase):
    charactor = mainCharactor()
    enemies = []
    def __init__(self):
        self.enemies.append(lv1enemy())
        SceneBase.__init__(self)
        
    
    def ProcessInput(self, events, pressed_keys):
        self.charactor.processAction(pressed_keys)
        # for event in events:
        #     if event.type == pygame.KEYDOWN:
        #         self.charactor.processAction(event.key)
        for i in self.enemies:
            i.processAction()
            for x in self.chacarot.getBullets():
                i.hit(x.x, x.y)

        
    def Update(self):
        pass
    
    def Render(self, screen):
        ## render our charactor
        screen.fill((40, 100, 255))
        self.charactor.render(screen)
        for i in self.enemies:
            i.render(screen)


run_game(800, 700, 120, TitleScene())