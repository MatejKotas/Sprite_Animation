import pygame

class SpriteSheet:

    def __init__(self, imagePath):
        self.content = pygame.img.load(imagePath)
    def getImage(self, x, y, width, height):
        image = pygame.Surface([width, height])
        image.blip(self.content, (0, 0), (x, y, width, height))
        image.set_colorkey(image.get_at((0, 0)))
        return image