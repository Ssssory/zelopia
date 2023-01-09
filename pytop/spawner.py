import pygame
import random
from object import ObjectOM
from settings import *

class Spavner:
    # container: list
    def __init__(self, screen):
        self.screen = screen
        self.container = []
        self.lines = []
    
    def invoke(self):
        if len(self.container) >= 2:
            return
        box = ObjectOM(self.screen)
        self.randomColor(box)
        box.setLines(self.lines)
        box.linePosition(self.randomLine(box))
        self.container.append(box)

    def setLines(self, lines):
        self.lines = lines

    def getLines(self):
        if len(self.lines) == 0:
            print('empty lines')
            raise RuntimeError('no lines coordinates. invoke setLines() method from Spavner!')
        return self.lines

    def draw(self):
        for i in self.container:
            if i.alive:
                i.moveDown()
                i.draw()
            else:
                pygame.event.post(pygame.event.Event(add_score))
                self.container.remove(i)

    def collisions(self, alien):
        for i in self.container:
            is_crash = i.checkCollision(alien)
            if is_crash:
                return True

    def randomColor(self, box):
        rand = random.randint(0,2)
        if rand == 0:
            box.setRed()
        if rand == 1:
            box.setYellow()
        if rand == 2:
            box.setBlue()

    def randomLine(self, box: ObjectOM):
        rand = random.choice(self.getLines())
        exist = self.getLineCar(rand)
        if exist:
            return self.randomLine(box)
        return rand
    
    def getLineCar(self, line):
        exist = False
        for i in self.container:
            if i.x == line - i.width/2:
                exist = True
        return exist

    def getObjectCount(self):
        return len(self.container)