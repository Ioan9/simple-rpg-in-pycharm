import pygame


class ferro(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/ferroP.png')
        self.image = pygame.transform.scale(self.image, [150, 150])
        self.rect = pygame.Rect(580, 500, 150, 150)
