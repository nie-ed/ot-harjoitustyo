import pygame
from sprites.blocks import Blocks



class Level:
    def __init__(self, level_map, cell_size, created_blocks = {}):
        self.cell_size = cell_size
        self.cell = None
        self.blocks = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.current_block = None        

        self._initialize_sprites(level_map, created_blocks)

        if self.current_block == None:
            self._create_new_block()

    def _initialize_sprites(self, level_map, created_blocks):
        height = len(level_map)
        width = len(level_map[0])
        

        for y in range(height):
            for x in range(width):
                self.cell = level_map[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                if (x, y) in created_blocks:
                    static_block_color = created_blocks[(x, y)]
                    block = Blocks(normalized_x, normalized_y, static_block_color)
                    self.blocks.add(block)
                else:
                    block = Blocks(normalized_x, normalized_y, (20,20,20))
                    self.blocks.add(block)

        self.all_sprites.add(  
            self.blocks
        )

    def _create_new_block(self):
        piece = Blocks(0, 0, (0,0,0))
        self.blocks.add(piece)
        self.current_block = piece

        self.all_sprites.add(  
            self.blocks
        )

    def move_block(self, dx=0, dy=0):
        self.current_block.rect.move_ip(dx, dy) 





        