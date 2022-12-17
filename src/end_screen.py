import pygame


class EndScreen(pygame.sprite.Sprite):
    """Class to create one Block for a piece.

    Args:
        pygame (Sprite): Class for game objects.
    """
    def __init__(self, X=0, Y=0):# pylint: disable=invalid-name
        """Constructor for class. Creates a Block object, with specific parameters.

        Args:
            X (int): x coordinate of Block. Defaults to 0.
            Y (int): y coordinate of Block. Defaults to 0.
            color: Color of Block. Defaults to None.
        """
        super().__init__()
        
        self.image = pygame.Surface((10*30, 20*30))
        self.image.fill((0,0,0))

        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
