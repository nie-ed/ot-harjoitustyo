import pygame


class GameLoop:
    def __init__(self, level, draw_display, event_handler, cell_size, clock):
        self._level = level
        self._draw_display = draw_display
        self._event_handler = event_handler
        self._cell_size = cell_size
        self._clock = clock


    def start(self):
        while True:
            if self._events() is False:
                break

            current_time = self._clock.get_ticks()

            self._level.update(current_time)
            self._draw_screen()

            self._clock.tick(60)



    def _events(self):  # pylint: disable=inconsistent-return-statements
        for event in self._event_handler.get():
            if event.type == pygame.KEYDOWN:  # pylint: disable=no-member
                if event.key == pygame.K_LEFT:  # pylint: disable=no-member
                    self._level.move_block(d_x=-self._cell_size)
                if event.key == pygame.K_RIGHT:  # pylint: disable=no-member
                    self._level.move_block(d_x=+self._cell_size)
                if event.key == pygame.K_UP:  # pylint: disable=no-member
                    self._level.rotate_block()
                if event.key == pygame.K_DOWN:  # pylint: disable=no-member
                    self._level.move_block(d_y=+self._cell_size)
            elif event.type == pygame.QUIT:  # pylint: disable=no-member
                return False

    def _draw_screen(self):
        self._draw_display.render()
