import pygame
from sprites.blocks import Blocks
from shape.shape_indexes import ShapeIndexes
from shape.get_shape import GetShape


class Level:
    def __init__(self, level_map, cell_size):
        self.cell_size = cell_size
        self.cell = None
        self.x = 5
        self.y = 5
        self.rotation = 0
        self.static_blocks = pygame.sprite.Group()
        self.background = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.current_block = None
        self.current_block_shape=None
        self.all_current_blocks = pygame.sprite.Group()
        self.current_block_previous_move_time = 0

        created_blocks = {(2, 4): (255, 0, 0), (8, 6): (
        0, 255, 255), (8, 7): (0, 255, 255)}

        self.created_blocks = created_blocks
        self.level_map = level_map

        if self.current_block_shape is None:
            self.current_block_shape = GetShape()


        self._initialize_sprites()

    def _initialize_sprites(self):
        height = len(self.level_map)
        width = len(self.level_map[0])


        for y in range(height):  # pylint: disable=invalid-name
            for x in range(width):  # pylint: disable=invalid-name
                self.cell = self.level_map[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size


                if (x, y) in self.created_blocks:
                    static_block_color = self.created_blocks[(x, y)]
                    block = Blocks(normalized_x, normalized_y,
                                   static_block_color)
                    self.static_blocks.add(block)

                block = Blocks(normalized_x, normalized_y, (20, 20, 20))
                self.background.add(block)


        self.all_sprites.add(
            self.background,
            self.static_blocks,
        )

        self._initialize_shape()


    def _initialize_shape(self):
        height = len(self.level_map)
        width = len(self.level_map[0])

        if self.current_block is None:
            self.current_block = ShapeIndexes(self.x, self.y, self.current_block_shape.shape)



        for y in range(height):  # pylint: disable=invalid-name
            for x in range(width):  # pylint: disable=invalid-name
                self.cell = self.level_map[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size


                if (x, y) in self.current_block.indexes:
                    self.all_current_blocks.add(
                        Blocks(normalized_x, normalized_y, self.current_block_shape.color))



        self.all_sprites.add(
            self.all_current_blocks
        )


    def update(self, current_time):
        if self.should_move(current_time):
            self.move_block(d_y=+self.cell_size)
            self.current_block_previous_move_time = current_time
        self.all_current_blocks.update()

    def should_move(self, current_time):
        return current_time - self.current_block_previous_move_time >= 800


    def move_block(self, d_x=0, d_y=0):
        colliding = []

        for block in self.all_current_blocks:
            colliding.append(self._block_can_move(block, d_x, d_y))

        if False not in colliding:
            for block in self.all_current_blocks:
                block.rect.move_ip(d_x, d_y)
        self.x = d_x
        self.y = d_y




    def _block_can_move(self, block, d_x=0, d_y=0):
        block.rect.move_ip(d_x, d_y)
        colliding_static_blocks = pygame.sprite.spritecollide(block, self.static_blocks, False)
        can_move = not colliding_static_blocks
        width = len(self.level_map[0])*self.cell_size

        if block.rect.left < 0:
            can_move = False
        if block.rect.right > width:
            can_move = False
        block.rect.move_ip(-d_x, -d_y)

        return can_move


    def rotate_block(self):
        self.rotation += 1
 
        i = 0
        n = 0
        for block in self.all_current_blocks:
            if n == 0:
                self.current_block = ShapeIndexes(block.rect.x/30, block.rect.y/30, self.current_block_shape.shape, self.rotation)
                break
            n += 1

        for block in self.all_current_blocks:
            block.rect.x = self.cell_size * (self.current_block.indexes[i][0]+1)
            block.rect.y = self.cell_size * (self.current_block.indexes[i][1]+4)
            i += 1

