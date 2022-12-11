import pygame
from level import Level
from game_loop import GameLoop
from map import Map
from draw_display import DrawDisplay
from event import Event
from clock import Clock


def main():
    level_map = Map()

    level_area = level_map.LEVEL_MAP
    cell_size = level_map.CELL_SIZE
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
