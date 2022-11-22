import pygame


class GameLoop:
    def __init__(self, level, cell_size, display):
        self._level = level
        self._cell_size = cell_size
        self._display = display

    def start(self):
        while True:
            if self._handle_events() == False:
                break

            self._draw_screen()


    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._level.move_block(dx=-self._cell_size)
                if event.key == pygame.K_RIGHT:
                    self._level.move_block(dx=self._cell_size)
                if event.key == pygame.K_UP:
                    self._level.move_block(dy=-self._cell_size)
                if event.key == pygame.K_DOWN:
                    self._level.move_block(dy=self._cell_size)
            elif event.type == pygame.QUIT:
                return False

    def _draw_screen(self):
        self._level.all_sprites.draw(self._display)

        pygame.display.update()