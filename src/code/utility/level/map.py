import pygame
from settings import *
from utility.tile import Tile
from entity.player import Player
from entity.enemy import Enemy
from utility.support import *
from random import choice, randint

class Map:

    def __init__(self,groups,layouts_path) -> None:
        self.obstacle_sprites = pygame.sprite.Group()
        self.attackable_sprites = groups['attackable']
        self.visible_sprites = groups['visible']
        self.layouts_path = layouts_path
        self.player_coordinates = (0,0)
    
    def create_map(self):

        layouts = {
            'boundary': import_csv_layout('../map/' + self.layouts_path + '/map_FloorBlocks.csv'),
            'grass': import_csv_layout('../map/' + self.layouts_path + '/map_Grass.csv'),
            'object': import_csv_layout('../map/' + self.layouts_path + '/map_Objects.csv'),
            'entities': import_csv_layout('../map/' + self.layouts_path + '/map_Entities.csv')
        }
        self.graphics = {
            'grass': import_folder('../graphics/grass'),
            'objects': import_folder('../graphics/objects')
        }

        for style,layout in layouts.items():
            for row_index,row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col == '-1':
                        continue
                    x = col_index * TILESIZE
                    y = row_index * TILESIZE
                    if style == 'boundary':
                        self.initBoundary(
                            (x,y),
                            [self.obstacle_sprites]
                        )

                    if style == 'grass':
                        self.initGrass(
                            (x,y),
                            [self.visible_sprites,self.obstacle_sprites,self.attackable_sprites],
                        )

                    if style == 'object':
                        self.initObject(
                            (x,y),
                            [self.visible_sprites,self.obstacle_sprites],
                            int(col)
                        )

                    if style == 'entities':
                        self.initEntities(
                            (x,y),
                            [self.visible_sprites,self.attackable_sprites],
                            col
                        )
    
    def initBoundary(self,cootdinate: tuple[int], groups: list):
        Tile(cootdinate, groups, 'invisible')

    def initGrass(self,cootdinate: tuple[int], groups: list):
        random_grass_image = choice(self.graphics['grass'])
        Tile(
            cootdinate,
            groups,
            'grass',
            random_grass_image)

    def initObject(self,cootdinate: tuple[int], groups: list, col: int):
        surf = self.graphics['objects'][int(col)]
        Tile(cootdinate, groups, 'object', surf)

    def initEntities(self,cootdinate: tuple[int], groups: list, col: int):
        if col == '394':
            self.player_coordinates = cootdinate
        else:
            if col == '390': monster_name = 'bamboo'
            elif col == '391': monster_name = 'spirit'
            elif col == '392': monster_name ='raccoon'
            else: monster_name = 'squid'
            Enemy(
                monster_name,
                cootdinate,
                groups,
                self.obstacle_sprites,
                self.visible_sprites,
                )