import pygame
from entity.player import Player
from utility.level.camera import Camera
from utility.level.map import Map
from state import State

from random import choice, randint

class Arena:
    def __init__(self, state: State) -> None:

        # get the display surface 
        self.display_surface = pygame.display.get_surface()
        self.game_paused = False
        
        self.visible_sprites = Camera()

        self.attackable_sprites = state.getSpriteGroup('attackable')
        self.attack_sprites     = state.getSpriteGroup('attack')

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

    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.spritecollide(attack_sprite,self.attackable_sprites,False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        if target_sprite.sprite_type == 'grass':
                            pos = target_sprite.rect.center
                            offset = pygame.math.Vector2(0,75)
                            for leaf in range(randint(3,6)):
                                self.player.animation_player.create_grass_particles(pos - offset,[self.visible_sprites])
                            target_sprite.kill()
                        else:
                            target_sprite.get_damage(self.player,attack_sprite.sprite_type)

    def run(self):
        self.visible_sprites.custom_draw(self.player)
		
        if not self.game_paused:
            self.visible_sprites.update()
            self.visible_sprites.enemy_update(self.player)
            self.player_attack_logic()