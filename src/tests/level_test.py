import unittest
from level import Level

testing_level = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]

testin_cell = 30
created_blocks = {(1, 1): (255, 0, 0), (1, 2): (
    0, 255, 255), (1, 3): (0, 255, 255)}


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.testing_level = Level(testing_level, testin_cell)

    def test_block_can_move(self):
        block = self.testing_level.current_block

        self.assertEqual(block.rect.x, 0)
        self.assertEqual(block.rect.y, 0)

        self.testing_level.move_block(dy=-30)
        self.assertEqual(block.rect.y, -30)
        self.assertEqual(block.rect.x, 0)

        self.testing_level.move_block(dx=-30)
        self.assertEqual(block.rect.x, -30)
        self.assertEqual(block.rect.y, -30)
