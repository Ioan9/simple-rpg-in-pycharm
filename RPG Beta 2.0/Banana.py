import pygame


class Banana(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/Banana.png')
        self.image = pygame.transform.scale(self.image, [150, 150])
        self.rect = pygame.Rect(950, 470, 150, 150)
