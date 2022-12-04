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
        self.testing_level = Level(testing_level, testin_cell, created_blocks)

    def test_block_can_move(self):
        blocks = self.testing_level.all_current_blocks


        for block in blocks:
            y = block.rect.y
            x = block.rect.x
            break
        
        for block in blocks:

 
            self.testing_level.move_block(d_y =+30)
            self.assertEqual(block.rect.y, y + testin_cell)

            self.testing_level.move_block(d_x=-30)
            self.assertEqual(block.rect.x, x-30)
            self.assertEqual(block.rect.y, y + 30)
            break

    def test_block_cant_move_past_walls(self):
        blocks = self.testing_level.all_current_blocks
        
        for block in blocks:

            self.assertEqual(self.testing_level._block_can_move(block, d_x=-30), True)
            self.assertEqual(self.testing_level._block_can_move(block, d_x=-30), True)
            self.assertEqual(self.testing_level._block_can_move(block, d_x=-300), False)
            self.assertEqual(self.testing_level._block_can_move(block, d_x=300), False)
            break
