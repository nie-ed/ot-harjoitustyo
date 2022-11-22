import unittest
from level import Level

LEVEL_MAP_1 = [[0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0]]

CELL_SIZE = 30
created_blocks = {(1,1):(255, 0, 0), (1,2): (0,255,255), (1,3): (0,255,255)}



class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level_1 = Level(LEVEL_MAP_1, CELL_SIZE)


    def test_block_can_move(self):
        block = self.level_1.current_block

        self.assertEqual(block.rect.x, 0)
        self.assertEqual(block.rect.y, 0)


        self.level_1.move_block(dy=-CELL_SIZE)
        self.assertEqual(block.rect.y, -CELL_SIZE)
        self.assertEqual(block.rect.x, 0)


        self.level_1.move_block(dx=-CELL_SIZE)
        self.assertEqual(block.rect.x, -CELL_SIZE)
        self.assertEqual(block.rect.y, -CELL_SIZE)

