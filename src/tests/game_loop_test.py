import unittest
import pygame

from logic.level import Level
from logic.game_loop import GameLoop


class StubClock:
    def tick(self, fps):
        pass

    def get_ticks(self):
        return 0


class StubEvent:
    def __init__(self, event_type, key=None):
        self.type = event_type
        self.key = key


class StubEventQueue:
    def __init__(self, events):
        self._events = events

    def get(self):
        return self._events


class StubRenderer:
    def render(self):
        pass


LEVEL_MAP_1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

CELL_SIZE = 30


class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.testing_level = Level(LEVEL_MAP_1, CELL_SIZE)

    def test_block_movement_left(self):
        blocks = self.testing_level.all_current_blocks

        for block in blocks:
            x = block.rect.x

            events = [
                StubEvent(pygame.KEYDOWN, pygame.K_LEFT), StubEvent(
                    pygame.QUIT),
            ]

            game_loop = GameLoop(
                self.testing_level,
                StubRenderer(),
                StubEventQueue(events),
                CELL_SIZE,
                StubClock()
            )

            game_loop.start()
            new_x = block.rect.x
            break

        self.assertEqual(new_x, x - CELL_SIZE)

    def test_block_movement_right(self):
        blocks = self.testing_level.all_current_blocks

        for block in blocks:
            x = block.rect.x

            events = [
                StubEvent(pygame.KEYDOWN, pygame.K_RIGHT), StubEvent(
                    pygame.QUIT),
            ]

            game_loop = GameLoop(
                self.testing_level,
                StubRenderer(),
                StubEventQueue(events),
                CELL_SIZE,
                StubClock()
            )

            game_loop.start()
            new_x = block.rect.x
            break

        self.assertEqual(new_x, x + CELL_SIZE)

    def test_block_movement_down(self):
        blocks = self.testing_level.all_current_blocks

        for block in blocks:
            y = block.rect.y

            events = [
                StubEvent(pygame.KEYDOWN, pygame.K_DOWN), StubEvent(
                    pygame.QUIT),
            ]

            game_loop = GameLoop(
                self.testing_level,
                StubRenderer(),
                StubEventQueue(events),
                CELL_SIZE,
                StubClock()
            )

            game_loop.start()
            new_y = block.rect.y
            break

        self.assertEqual(new_y, y + CELL_SIZE)
