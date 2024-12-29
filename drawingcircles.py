import pygame
pygame.init()

WIDTH = 600
HEIGHT = 800

position = (400,400)
radius = 50
width = 2




screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill((255,255,255))

class Circle():
    
    def __init__(self,color,position,radius,width):
        self.color = color
        self.position = position
        self.radius = radius
        self.width = width
        self.screen = screen
    
    def draw(self):
        pygame.draw.circle(self.screen,self.color,self.position,self.radius,self.width)
    
    def grow(self,r):
        self.radius = self.radius + r
        pygame.draw.circle(self.screen,self.color,self.position,self.radius,self.width)

pygame.draw.circle(screen, "Red", position, radius, width)
pygame.display.update()


blueCircle = Circle("Blue", position, radius + 75, 0)
redCircle = Circle("Red", position, radius + 50, 0)
yellowCircle = Circle("Yellow", position, radius + 25, 5)
greenCircle = Circle("Green", position, 25, 0)

while True:
    for event in pygame.event.get():
        if (event.type == pygame.MOUSEBUTTONDOWN):
            blueCircle.draw()
            redCircle.draw()
            yellowCircle.draw()
            greenCircle.draw()
        elif (event.type == pygame.MOUSEBUTTONUP):
            blueCircle.grow(25)
            redCircle.grow(25)
            yellowCircle.grow(25)
            greenCircle.grow(25)
        elif (event.type == pygame.MOUSEMOTION):
            pos = pygame.mouse.get_pos()
            blackCircle = Circle("Black", pos, 15, 5)
            blackCircle.draw()
        elif (event.type == pygame.QUIT):
            pygame.quit()
    pygame.display.update()















