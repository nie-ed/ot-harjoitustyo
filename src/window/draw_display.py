import pygame


class DrawDisplay:
    """Class for drawing updated display.
    """

    def __init__(self, display, level):
        """Class constructor, to update the display.

        Args:
            display: Display of game
            level (Level): Level, where sprites and movement.
        """
        self._display = display
        self._level = level

    def render(self):
        """Draws sprites on display and updates display.
        """
        self._level.all_sprites.draw(self._display)

        pygame.display.update()

    def end_screen(self, score, all_scores):#pylint: disable=too-many-statements
        """Draws end screen.s

        Args:
            score (Score): The score the player had at the end of the game.
            all_scores (list): List of scores and player usernames in the repository
        """

        self._display.fill((0, 0, 0))

        font = pygame.font.Font('freesansbold.ttf', 50)
        font2 = pygame.font.Font('freesansbold.ttf', 40)
        font3 = pygame.font.Font('freesansbold.ttf', 30)

        over_image = font.render('GAME OVER', True, (255, 140, 0))
        image = font2.render('Your Score:', True, 	(238, 232, 170))
        image2 = font3.render(str(score), True, (255, 255, 255))
        image3 = font2.render('High Scores:', True, (238, 232, 170))

        self._display.blit(over_image, (150, 50))
        self._display.blit(image, (100, 150))
        self._display.blit(image2, (400, 160))
        self._display.blit(image3, (100, 220))

        spot = 275
        place = 0

        for i in all_scores:
            place += 1
            if place > 11:
                break
            show_score = font3.render(str(i.score), True, (255, 255, 255))
            self._display.blit(show_score, (100, spot))
            spot += 35

        pygame.display.update()
