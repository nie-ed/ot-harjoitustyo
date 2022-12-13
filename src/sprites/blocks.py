import pygame


class Blocks(pygame.sprite.Sprite):
    """Class to create one Block for a piece.

    Args:
        pygame (Sprite): Class for game objects.
    """
    def __init__(self, X=0, Y=0, color=None):# pylint: disable=invalid-name
        """Constructor for class. Creates a Block object, with specific parameters.

        Args:
            X (int): x coordinate of Block. Defaults to 0.
            Y (int): y coordinate of Block. Defaults to 0.
            color: Color of Block. Defaults to None.
        """
        super().__init__()
        
        self.image = pygame.Surface((29, 29))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = X
        self.rect.y = Y
