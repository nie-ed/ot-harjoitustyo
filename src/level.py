import pygame
from sprites.blocks import Blocks
from sprites.create_shape import CreateShapes


class Level:
    def __init__(self, level_map, cell_size, created_blocks):
        self.cell_size = cell_size
        self.cell = None
        self.static_blocks = pygame.sprite.Group()
        self.background = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.current_block = None
        self.all_current_blocks = pygame.sprite.Group()

        self.created_blocks = created_blocks
        self.level_map = level_map

        if self.current_block is None:
            self.current_block = CreateShapes(5, 5)

        self._initialize_sprites()



    def _initialize_sprites(self):
        height = len(self.level_map)
        width = len(self.level_map[0])


        for y in range(height):  # pylint: disable=invalid-name
            for x in range(width):  # pylint: disable=invalid-name
                self.cell = self.level_map[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                if (x, y) in self.current_block.indexes:
                    self.all_current_blocks.add(
                        Blocks(normalized_x, normalized_y, self.current_block.color))

                elif (x, y) in self.created_blocks:
                    static_block_color = self.created_blocks[(x, y)]
                    block = Blocks(normalized_x, normalized_y,
                                   static_block_color)
                    self.static_blocks.add(block)

                block = Blocks(normalized_x, normalized_y, (20, 20, 20))
                self.background.add(block)




        self.all_sprites.add(
            self.background,
            self.static_blocks,
            self.all_current_blocks
        )




    def move_block(self, d_x=0, d_y=0):
        colliding = []

        for block in self.all_current_blocks:
            colliding.append(self._block_can_move(block, d_x, d_y))

        if False not in colliding:
            for block in self.all_current_blocks:
                block.rect.move_ip(d_x, d_y)


    def rotate_block(self):
        self.current_block.rotation += 1


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
