import pygame
from enum import Enum
from settings import *

class DisplayPosition(Enum):
    TOPLEFT = 'topleft'
    TOPRIGHT = 'topright'
    BOTTOMLEFT = 'bottomlrft'
    BOTTOMRIGHT = 'bottomright'
    TOP = 'top'
    LEFT = 'left'
    RIGHT = 'right'
    BOTTOM = 'bottom'
    CENTER = 'center'

class UiText:
    def __init__(self, text: str = "", position = (0,0), color = None) -> None:
        self.text = text
        self.color = color
        self.textSize = 32
        self.position = position
        #
        self.font = self.initFont()
        self.objText = self.setObjectText()
        self.coordinates = self.getCoordinates(position) 

    def getCoordinates(self, position):
        position = TextPosition(self.objText, position)
        return position.getPosition()

    def initFont(self):
        return pygame.font.Font(None,self.textSize)

    def setObjectText(self):
        return self.font.render(self.text, False, self.getColor())

    def setText(self, text: str):
        self.text = text 

    def setFontSize(self, size: int):
        self.textSize = size
        self.font = self.initFont()
        self.objText = self.setObjectText()
        self.coordinates = self.getCoordinates(self.position) 

    def getColor(self):
        if self.color == None:
            return (0,0,0)
        return self.color

    def setColor(self, color):
        self.color = color

    def render(self, screen):
        # print(self.coordinates)
        self.objText = self.font.render(self.text, False, self.getColor())
        screen.blit(self.objText, self.coordinates)



class TextPosition:
    position: tuple = ()
    def __init__(self, text, position) -> None:
        self.text = text
        self.setPosition(position)

    def setPosition(self, position):
        if type(position) == DisplayPosition:
            if position == DisplayPosition.BOTTOMLEFT:
                self.position = (0, HEIGHT - self.text.get_height())
            if position == DisplayPosition.BOTTOMRIGHT:
                self.position = (WIDTH - self.text.get_width(), HEIGHT - self.text.get_height())
            if position == DisplayPosition.BOTTOM:
                self.position = (WIDTH/2 - self.text.get_width()/2, HEIGHT - self.text.get_height())
            if position == DisplayPosition.TOPLEFT:
                self.position = (0, 0)
            if position == DisplayPosition.TOPRIGHT:
                self.position = (WIDTH - self.text.get_width(),0)
            if position == DisplayPosition.TOP:
                self.position = (WIDTH/2 - self.text.get_width()/2, 0)
            if position == DisplayPosition.RIGHT:
                self.position = (WIDTH - self.text.get_width(),HEIGHT/2 - self.text.get_height()/2)
            if position == DisplayPosition.LEFT:
                self.position = (0,HEIGHT/2 - self.text.get_height()/2)
            if position == DisplayPosition.CENTER:
                self.position = (WIDTH/2 - self.text.get_width()/2, HEIGHT/2 - self.text.get_height()/2)

        if type(position) == type(()):
            # TODO: rule
            self.position = position
    
    def getPosition(self):
        return self.position