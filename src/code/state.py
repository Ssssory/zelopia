import pygame
from utility.singleton import Singleton

class State(metaclass=Singleton):
    def __init__(self) -> None:
        # sprite groups
        self.obstacle_sprites = pygame.sprite.Group()

        # attack sprites
        self.current_attack = None
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()
        self.name = ''

    def getSpriteGroup(self, name: str):
        if name == 'obstacle':
            return self.obstacle_sprites
        if name == 'attack':
            return self.attack_sprites
        if name == 'attackable':
            return self.attackable_sprites
        