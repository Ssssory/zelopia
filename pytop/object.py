import pygame
from color import *
from settings import *

class ObjectOM:
    def __init__(self, surface):
        self.width = 30
        self.height = 80
        self.x = 0
        self.y = 0 - self.height
        self.color = (0,0,0)
        self.surface = surface
        self.bordered = True

        self.speed = 3
        self.alive = True

        self.collision = None
    
    def setColor(self, color: tuple):
        self.color = color

    def setYellow(self):
        self.speed = 5
        self.setColor(BANANA)

    def setBlue(self):
        self.speed = 6
        self.setColor(BLUE)

    def setRed(self):
        self.speed = 4
        self.setColor(RED2)

    def setLines(self, lines):
        self.lines = lines
    
    def getGeometry(self):
        return (self.x, self.y, self.width, self.height)

    def moveDown(self):
        if self.y - 50 >= HEIGHT:
            self.alive = False
        else:
            self.y += self.speed    

    def move(self, direction: str):
        current = None
        for key, position in enumerate(self.lines):
            if position == self.x + (self.width/2):
                current = key
        if current == None:
            print('Error x position')
            return False

        if direction == 'left' and current == 0:
            return
        if direction == 'right' and current == len(self.lines) -1:
            return
        if direction == 'right':
            self.linePosition(self.lines[current + 1])
        if direction == 'left':
            self.linePosition(self.lines[current - 1])
    
    def playerInitPosition(self):
        self.x = self.lines[1] - (self.width/2)
        self.y = HEIGHT - (self.height + 15)

    def linePosition(self, positionX):
        if positionX in self.lines:
            self.x = positionX - self.width/2
        else:
            print(positionX)
            raise RuntimeError('wrong player position x coordinate')

    def checkCollision(self, alien):
        if self.collision == None:
            return False
        return self.collision.colliderect(alien)

    def draw(self):
        if self.alive:
            self.collision = pygame.draw.rect(self.surface, self.color, self.getGeometry())
            self.drawBorder()
            

    def drawBorder(self):
        if self.bordered:
                pygame.draw.lines(self.surface, BLACK, True, [
                        (self.x,self.y),
                        (self.x + self.width,self.y),
                        (self.x + self.width,self.y + self.height),
                        (self.x,self.y + self.height)
                    ],2)