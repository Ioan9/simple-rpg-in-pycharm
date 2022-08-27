import pygame


class Madeira(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/madeira.png')
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(200, 540, 100, 100)
