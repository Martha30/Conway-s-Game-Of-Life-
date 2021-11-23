#Universidad del Valle de Guatemala
#Laurelinda Gómez 19501
#15/11/2021
import pygame
import random

class Life(object):
    def __init__(self, screen):
        _, _, self.width, self.height = screen.get_rect()
        self.screen = screen
#En base a lo que se realizó en la clase
    def clear(self):
        self.screen.fill(negro)

    def pixel(self, x, y, color):
        self.screen.set_at((x, y), color)

    def copy(self):
        self.prev_turn = self.screen.copy()
    
    def render(self):
        for x in range(self.width):
            for y in range(self.height):
                v = 0
                try:
                    if (self.prev_turn.get_at((x+1,y))[0] == 255):
                        v += 1
                except:
                    pass
                try:
                    if (self.prev_turn.get_at((x-1,y))[0] == 255):
                        v += 1
                except:
                    pass
                try:
                    if (self.prev_turn.get_at((x,y-1))[0] == 255):
                        v += 1
                except:
                    pass
                try:
                    if (self.prev_turn.get_at((x,y+1))[0] == 255):
                        v += 1
                except:
                    pass
                try:
                    if (self.prev_turn.get_at((x+1,y+1))[0] == 255):
                        v += 1
                except:
                    pass
                try:
                    if (self.prev_turn.get_at((x-1,y-1))[0] == 255):
                        v += 1
                except:
                    pass
                try:
                    if (self.prev_turn.get_at((x-1,y+1))[0] == 255):
                        v += 1
                except:
                    pass
                try:
                    if (self.prev_turn.get_at((x+1,y-1))[0] == 255):
                        v += 1
                except:
                    pass
                if (self.prev_turn.get_at((x,y))[0] == 255):
                    if v < 2:
                        self.pixel(x, y, negro)
                    if v == 2 or v == 3:
                        self.pixel(x, y, rojo)
                    if v > 3:
                        self.pixel(x, y, negro)
                if (self.prev_turn.get_at((x,y))[0] == 0):
                    if v == 3:
                        self.pixel(x, y, rojo)
  



pygame.init()
screen = pygame.display.set_mode((150, 150))
r = Life(screen)
rojo = (255, 255, 255)
negro = (0, 0, 0)
f = 20

for i in range(r.width * f ):
    x = random.randint(0, 150)
    y = random.randint(0, 150)
    r.pixel(x,y, rojo)


  