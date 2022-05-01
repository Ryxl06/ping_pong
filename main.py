from pygame import *
from random import uniform
init()

V_mv = 500
H_mv = 500
mv = display.set_mode((V_mv,H_mv))
back = (123,213,312)
mv.fill(back)
clock = time.Clock(60)

class GameSprite(sprite.Sprite):
    def __init__(self, image, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(image), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y, self.speed = x, y, speed
        

    def reset(self):|
        mv.blit(self.image, (self.rect.x, self.rect.y))
RC1 = GameSprite('rc_py.png', 10, H_mv/2 - 53, 16, 106, 5)
RC2 = GameSprite('rc_py.png', V_mv-26, H_mv/2 - 53, 16, 106, 5)
game = True
while game:
    for e in pygame.event.get:
        if e.type == QUIT:
                game = False
    mv.fill(back)            
    RC1.reset()
    RC2.reset()
    display.update()
    clock.tick(60)
    