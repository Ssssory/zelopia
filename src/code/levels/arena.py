import pygame
from entity.player import Player
from utility.level.camera import Camera
from utility.level.map import Map
from state import State

class Arena:
    def __init__(self, state: State) -> None:

        # get the display surface 
        self.display_surface = pygame.display.get_surface()
        self.game_paused = False
        
        self.visible_sprites = Camera()

        self.attackable_sprites = state.getSpriteGroup('attackable')

        self.level_name = 'level'

        map = Map({
            'visible': self.visible_sprites
            },
            self.level_name)

        map.create_map()

        # creating the floor
        self.visible_sprites.floor_surf = pygame.image.load('../graphics/tilemap/ground.png').convert()
        self.visible_sprites.floor_rect = self.visible_sprites.floor_surf.get_rect(topleft = (0,0))

        self.player = Player(
            map.player_coordinates,
            [map.visible_sprites]
            )

    def run(self):
        self.visible_sprites.custom_draw(self.player)
		
        if not self.game_paused:
            self.visible_sprites.update()
            self.visible_sprites.enemy_update(self.player)
