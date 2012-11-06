import os
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
color = (255, 100, 0)
x = 30
y = 30
clock = pygame.time.Clock()
_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
		
	pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
	screen.fill((0, 0, 0))
	screen.blit(get_image('images/man.png'), (x, y))
        pygame.draw.rect(screen, color, pygame.Rect(0,398, 0, 10))
#        pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

        pygame.display.flip()
	clock.tick(120)
