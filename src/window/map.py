import pygame


class Map():
    """Class to create the screen for the game.
    """

    def __init__(self):
        """Creates grid and display with the grid mesurements.
        """
        self.level_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.cell_size = 30

        display = pygame.display.set_mode((600, 600))

        pygame.display.set_caption("Tetris")

        display.fill((0, 0, 0))

        self.display = display
        self.score = 0
        self.window_text(self.score)

    def window_text(self, score):
        """Creates the text on the screen.

        Args:
            score (Score): The amount of point the player ha currently.
        """
        self.score = score

        pygame.font.init()

        cover = pygame.Surface((300, 100))
        cover.fill((0, 0, 0))

        font = pygame.font.Font('freesansbold.ttf', 30)
        image = font.render('Your Score', True, (127, 255, 212))
        image2 = font.render('Next Piece', True, (127, 255, 212))
        image3 = font.render(str(self.score), True, (127, 255, 212))
        self.display.blit(cover, (340, 340))
        self.display.blit(image2, (350, 50))
        self.display.blit(image, (350, 300))
        self.display.blit(image3, (350, 350))
