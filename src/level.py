import pygame
from sprites.blocks import Blocks
from sprites.new_block import NewBlockAttributes
from sprites.create_shape import CreateShapes


class Level:
    def __init__(self, level_map, cell_size, created_blocks):
        self.cell_size = cell_size
        self.cell = None
        self.static_blocks = pygame.sprite.Group()
        self.background = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.current_block_attributes = None
        self.block_indexes = None
        self.current_block_created = pygame.sprite.Group()



        if self.current_block_attributes is None:
            self._create_new_block()
            self.block_indexes = CreateShapes(self.current_block_attributes)

        self._initialize_sprites(level_map, created_blocks)



    def _initialize_sprites(self, level_map, created_blocks):
        height = len(level_map)
        width = len(level_map[0])


        for y in range(height):  # pylint: disable=invalid-name
            for x in range(width):  # pylint: disable=invalid-name
                self.cell = level_map[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                if (x, y) in self.block_indexes.indexes:
                    block = Blocks(normalized_x, normalized_y, self.current_block_attributes.color)
                    self.current_block_created.add(block)

                elif (x, y) in created_blocks:
                    static_block_color = created_blocks[(x, y)]
                    block = Blocks(normalized_x, normalized_y,
                                   static_block_color)
                    self.static_blocks.add(block)
                else:
                    block = Blocks(normalized_x, normalized_y, (20, 20, 20))
                    self.background.add(block)




        self.all_sprites.add(
            self.current_block_created,
            self.static_blocks,
            self.background
        )

    def _create_new_block(self):
        self.current_block_attributes = NewBlockAttributes(5, 5)



    def move_block(self, d_x=0, d_y=0):
        for i in pygame.sprite.Group.sprites(self.current_block_created):
            i.rect.move(d_x, d_y)

    def rotate_block(self, i):
        self.current_block_created.rotation += i
