import pygame

class Clock:
    """Class to handel timed events.
    """
    def __init__(self):
        """Constructor of class. Creates a Clock object.
        """
        self._clock = pygame.time.Clock()

    def tick(self, fps):
        """Time from last call in milliseconds.

        Args:
            fps (framerate): Max amout of calls in one second.
        """
        self._clock.tick(fps)

    def get_ticks(self):
        """Return the amount of milliseconds since pygame.init() call.

        Returns:
            milliseconds: Miliseconds since start of game.
        """
        return pygame.time.get_ticks()