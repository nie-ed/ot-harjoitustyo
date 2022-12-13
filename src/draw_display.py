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