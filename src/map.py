import pygame

class Map():
    """Class to create the screen for the game.
    """
    def __init__(self):
        """Creates grid and display wiht the grid mesurements.
        """
        self.LEVEL_MAP = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
                          
        self.CELL_SIZE = 30


        height = len(self.LEVEL_MAP)
        width = len(self.LEVEL_MAP[0])

        _display_height = height * self.CELL_SIZE
        _display_width = width * self.CELL_SIZE

        display = pygame.display.set_mode((600, 600))
        
        pygame.display.set_caption("Tetris")

        display.fill((0,0, 0))

        
        self.area = pygame.Surface((_display_width, _display_height))
        self.area.fill((25,25,25))

        self.area.blit(display, (50 ,50))

        pygame.font.init()

        font = pygame.font.Font('freesansbold.ttf', 30)
        image = font.render('Your Score', True, (127,255,212))
        image2 = font.render('Next Piece', True, (127,255,212))
        display.blit(image, (350,300))
        display.blit(image2, (350,50))

        self.display = display

       


    def end_screen(self):
        self.area = pygame.Surface((600,600))
        self.area.fill((0,0,0))

        self.display.blit(self.area, (0 ,0))

        font = pygame.font.Font('freesansbold.ttf', 50)
        image = font.render('Your Score', True, (127,255,212))
        image2 = font.render('High Scores', True, (127,255,212))
        self.area.blit(image, (350,300))
        self.area.blit(image2, (350,50))
