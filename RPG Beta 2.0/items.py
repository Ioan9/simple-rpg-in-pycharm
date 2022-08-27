import pygame



class Menu(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/menu.png')
        self.image = pygame.transform.scale(self.image, [460, 300])
        self.rect = pygame.Rect(800,600 , 200, 200)

class mochila(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/mochilaP.png')
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(1080, 700, 100, 100)

class Craft(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/Craft.png')
        self.image = pygame.transform.scale(self.image, [100, 104])
        self.rect = pygame.Rect(970, 698, 100, 100)

class Enchada(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/enchada.png')
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(60, 80, 100, 100)
class Picareta(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/Picareta.png')
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(260, 80, 100, 100)