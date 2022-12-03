import pygame


class GameLoop:
    def __init__(self, level, cell_size, display):
        self._level = level
        self._cell_size = cell_size
        self._display = display

    def start(self):
        while True:
            if self._events() is False:
                break

            self._draw_screen()

    def _events(self):  # pylint: disable=inconsistent-return-statements
        for event in pygame.event.get():
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
        self._level.all_sprites.draw(self._display)

        pygame.display.update()
