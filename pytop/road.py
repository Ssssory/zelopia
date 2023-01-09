import pygame
from settings import *
from enum import Enum

class RoadMarker(Enum):
    WIDTH = 10
    HEIGHT = 50

class Road:
    def __init__(self, screen, width: int = 400):
        self.screen = screen
        self.roadColor = (100, 100, 100)
        self.markerColor = (255, 200, 0)

        self.loopPosition = 0
        self.speed = 2

        self.height = HEIGHT
        self.leftMargin = 100
        self.topMargin = 0

        self.halfLineWidth = 45
        self.linesCount = 3
        self.setWidth(width)
        self.lines = []
        self.setLines(self.linesCount)


    def setLines(self, count: int):
        lineWidth = self.width / count
        halfLineWidth = lineWidth / 2
        self.halfLineWidth = round(halfLineWidth)
        for i in range(count):
            lineCenterX = self.leftMargin + self.halfLineWidth + (round(lineWidth) * i)
            self.lines.append(lineCenterX)

    def getLines(self):
        return self.lines

    def setWidth(self, width):
        if width < 300:
            self.width = 300
        elif width > 600:
            self.width = 600
        else:
            plaine = width - 10 - (10*self.linesCount)
            last = plaine % self.linesCount
            if last != 0:
                width -= last
            self.width = width
            
    
    def setRoadColor(self, color: tuple = None, marker_color: tuple = None):
        if color != None:
            self.roadColor = color
        if marker_color != None:
            self.markerColor = marker_color

    def appendSpeed(self):
        self.speed += 1

    def getRoadCoordinates(self):
        return (
            self.leftMargin,
            self.topMargin,
            self.width,
            self.height
        )

    def getBorders(self):
        return {
            "left": (self.leftMargin - 5, 0, RoadMarker.WIDTH.value, HEIGHT),
            "right": (self.leftMargin + self.width -5, 0, RoadMarker.WIDTH.value, HEIGHT),
        }

    def drawRoadBackground(self):
        borders = self.getBorders()
        pygame.draw.rect(self.screen, self.roadColor, self.getRoadCoordinates())
        pygame.draw.rect(self.screen, self.markerColor, borders["left"])
        pygame.draw.rect(self.screen, self.markerColor, borders["right"])

    def drawLinesOnRoad(self, y):
        for i in self.lines:
            if i == self.lines[-1]:
                continue
            pygame.draw.rect(self.screen,(255,255,255),(i+self.halfLineWidth - RoadMarker.WIDTH.value, y + self.loopPosition, RoadMarker.WIDTH.value, RoadMarker.HEIGHT.value))
            
    def render(self):
        self.drawRoadBackground()
        self.loopPosition += self.speed
        if self.loopPosition >= RoadMarker.HEIGHT.value * 2:
            self.loopPosition = 0
        for y in range(RoadMarker.HEIGHT.value * -2, HEIGHT, RoadMarker.HEIGHT.value *2):
            self.drawLinesOnRoad(y)

        # debug
        # for i in self.lines:
        #     pygame.draw.rect(self.screen,(255,255,255),(i,0,1,HEIGHT))
