import unittest
from logic.level import Level

testing_level = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]

testin_cell = 30



class TestLevel(unittest.TestCase):
    def setUp(self):
        self.testing_level = Level(testing_level, testin_cell)

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


    def test_block_moves_if_time_passed(self):
        blocks = self.testing_level.all_current_blocks
        self.testing_level.current_block_previous_move_time = 100
           
        for block in blocks:
            y = block.rect.y
            break

        for block in blocks:
            self.testing_level.update(1000)

            self.assertEqual(block.rect.y, y+30)
            break

    def test_block_does_not_move_if_time_not_passed(self):
        blocks = self.testing_level.all_current_blocks
        self.testing_level.current_block_previous_move_time = 900
           
        for block in blocks:
            y = block.rect.y
            break

        for block in blocks:
            self.testing_level.update(1000)

            self.assertEqual(block.rect.y, y)
            break



    def test_static_block_existence(self):
        self.testing_level.created_blocks = {(2,4): (255, 0, 0)}

        self.testing_level._initialize_shape()

        for block in self.testing_level.static_blocks:
            self.assertEqual(block.rect.x, 2*testin_cell)
            self.assertEqual(block.rect.y, 4*testin_cell)