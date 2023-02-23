import pygame

class Spritesheet:
    def __init__(self, path, size) -> None:
        self.spritesheet = pygame.image.load(path).convert()
        self.size = size
        self.tileWidth = self.size[0]
        self.tileHeight = self.size[1]
        self.width = 0
        self.height = 0
        self.inRaw = 0
        self.max = self.__getTileCount()

    def getTile(self, index):
        x, y = self.__getTileCoordinate(index)
        tile = pygame.Surface(self.size)
        tile.blit(self.spritesheet,(0, 0), (x, y, self.tileWidth, self.tileHeight))
        return tile
    
    def __getTileCoordinate(self, index):
        if index < 0 or index > self.max:
            raise ValueError("Tile number not found.")
        raw = index // self.inRaw
        column = index % self.inRaw
        return column * self.tileWidth, raw * self.tileHeight
    
    def __getTileCount(self):
        width = self.spritesheet.get_rect().w
        height = self.spritesheet.get_rect().h
        if width % self.tileWidth != 0 or height % self.tileHeight != 0:
            raise ValueError("Image size is not a multiple of the tile size.")
        self.inRaw = width // self.tileWidth
        return (width // self.tileWidth) *  (height // self.tileHeight)