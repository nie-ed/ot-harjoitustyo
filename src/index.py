import pygame
from logic.level import Level
from logic.game_loop import GameLoop
from logic.event import Event
from logic.clock import Clock
from window.map import Map
from window.draw_display import DrawDisplay


def main():
    """Initializes game. Starts game.
    """
    level_map = Map()

    level_area = level_map.level_map
    cell_size = level_map.cell_size
    display = level_map.display

    clock = Clock()
    level = Level(level_area, cell_size)
    events = Event()
    draw_display = DrawDisplay(display, level)
    game_loop = GameLoop(level, draw_display, events, cell_size, clock)

    pygame.init()  # pylint: disable=no-member
    game_loop.start()


if __name__ == "__main__":
    main()
