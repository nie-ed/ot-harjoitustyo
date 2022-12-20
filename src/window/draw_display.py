import pygame
from repositories.scores_repository import (
    score_repository as default_score_repository
)


class DrawDisplay:
    """Class for drawing updated display.
    """
    def __init__(self, display, level, score_repository = default_score_repository):
        """Class constructor, to update the display.

        Args:
            display: Display of game
            level (Level): Level, where sprites and movement.
        """
        self._display = display
        self._level = level
        self._score_repository = score_repository


    def render(self):
        """Draws sprites on display and updates display.
        """
        self._level.all_sprites.draw(self._display)

        pygame.display.update()


    def end_screen(self, score):
        self.score = score

        self._score_repository.create(self.score, "user")
        all = self._score_repository.find_all()

        self._display.fill((0,0,0))


        font = pygame.font.Font('freesansbold.ttf', 50)
        font2 = pygame.font.Font('freesansbold.ttf', 40)
        font3 = pygame.font.Font('freesansbold.ttf', 30)


        over_image = font.render('GAME OVER', True, (255,140,0))
        image = font2.render('Your Score:', True, 	(238,232,170))
        image2 = font3.render(str(self.score), True, (255,255,255))
        image3 = font2.render('High Scores:', True, (238,232,170))

        self._display.blit(over_image, (150,50))
        self._display.blit(image, (100,150))
        self._display.blit(image2, (450,155))
        self._display.blit(image3, (100,220))


        spot = 260

        for i in all:
            show_score = font3.render(str(i.score), True, (255,255,255))
            show_username = font3.render(str(i.username), True, (255,255,255))
            self._display.blit(show_score, (100,spot))
            self._display.blit(show_username, (400,spot))
            spot += 30

        pygame.display.update()
