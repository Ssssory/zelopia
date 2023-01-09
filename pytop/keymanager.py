from pygame.event import Event
from pygame.locals import *

class Keymanager:
    def event(self, ev: Event ):
        if ev.key == K_TAB:
            print('tab button')
        if ev.key == K_SPACE:
            print('tab spase')
