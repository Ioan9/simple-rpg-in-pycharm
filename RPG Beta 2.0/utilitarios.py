import pygame


class exit1(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/exit.png')
        self.image = pygame.transform.scale(self.image, [50, 50])
        self.rect = pygame.Rect(1180, 10, 50, 50)

