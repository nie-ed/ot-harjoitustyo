import pygame


class Event:
    """Class for handling event queue.
    """

    def get(self):
        """Gets the next event on the queue.

        Returns:
            Event to be handled.
        """
        return pygame.event.get()
