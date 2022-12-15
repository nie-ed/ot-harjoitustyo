import pygame
from sprites.blocks import Blocks
from shape.shape_indexes import ShapeIndexes
from shape.get_shape import GetShape
from movement.rotate_block import RotateBlock

class Level:
    """Class, that creates sprites and handles block movement.

    Attributes:
        level_map = screen where the game is on, 2 dimensional grid  
        cell_size = The size of one cell in the level_map
    """
    def __init__(self, level_map, cell_size):
        """Constructor for the class, that initialises sprites and block info.

        Args:
            level_map = screen where the game is on, 2 dimensional grid  
            cell_size = The size of one cell in the level_map

        """
        self.cell_size = cell_size
        self.cell = None
        self.rotation = 0
        self.static_blocks = pygame.sprite.Group()
        self.background = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.current_block = None
        self.current_block_shape=None
        self.all_current_blocks = pygame.sprite.Group()
        self.current_block_previous_move_time = 0
        self.turn_static = False

        created_blocks = {}

        self.created_blocks = created_blocks
        self.level_map = level_map




        self._initialize_sprites()

    def _initialize_sprites(self):
        """Creates static and background sprites and adds them to correct sprite groups.
        """
        height = len(self.level_map)
        width = len(self.level_map[0])


        for y in range(height):  # pylint: disable=invalid-name
            for x in range(width):  # pylint: disable=invalid-name
                self.cell = self.level_map[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                block = Blocks(normalized_x, normalized_y, (20, 20, 20))
                self.background.add(block)


        self.all_sprites.add(
            self.background,
        )

        self._initialize_shape()


    def _initialize_shape(self):
        """Creates payable tetris piece and adds it to the correct sprite group. 
        """
        height = len(self.level_map)
        width = len(self.level_map[0])

        if self.current_block_shape is None:
            self.current_block_shape = GetShape()

        if self.current_block is None:
            self.current_block = ShapeIndexes(5, 5, self.current_block_shape.shape)



        for y in range(height):  # pylint: disable=invalid-name
            for x in range(width):  # pylint: disable=invalid-name
                self.cell = self.level_map[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                if self.current_block_shape.index == 2:
                    if (x, y) in self.current_block.indexes:
                        self.all_current_blocks.add(
                            Blocks(normalized_x, normalized_y-self.cell_size, self.current_block_shape.color))
                elif self.current_block_shape.index == 3 or self.current_block_shape.index == 1 or self.current_block_shape.index == 0:
                    if (x, y) in self.current_block.indexes:
                        self.all_current_blocks.add(
                            Blocks(normalized_x, normalized_y-self.cell_size*3, self.current_block_shape.color))
                else:
                    if (x, y) in self.current_block.indexes:
                        self.all_current_blocks.add(
                            Blocks(normalized_x, normalized_y-self.cell_size*2, self.current_block_shape.color))


        self.all_sprites.add(
            self.all_current_blocks
        )


    def update(self, current_time):
        """Moves currently used piece down according to clock ticks.

        Args:
            current_time (Clock): Milliseconds since the start of the game.
        """
        if self.should_move(current_time):
            self.move_block(d_y=+self.cell_size)
            self.current_block_previous_move_time = current_time
        self.clear_row()
        self.all_current_blocks.update()

    def should_move(self, current_time):
        """Checks if a certain amount of time has passed

        Args:
            current_time (Clock): Milliseconds since the start of the game.

        Returns:
            Boolean: True, if a certain amount of time or more has passed, False if not.
        """
        return current_time - self.current_block_previous_move_time >= 800


    def move_block(self, d_x=0, d_y=0):
        """Moves current piece, if possible.

        Args:
            d_x (int): How much piece should move to the x direction. Defaults to 0.
            d_y (int): How much piece should move to the y direction. Defaults to 0.
        """
        colliding = []

        for block in self.all_current_blocks:
            colliding.append(self._block_can_move(block, d_x, d_y))

        if False not in colliding:
            for block in self.all_current_blocks:
                block.rect.move_ip(d_x, d_y)

        if self.turn_static is True:
            for block in self.all_current_blocks:
                self.static_blocks.add(block)
            self.all_current_blocks.empty()
            self.current_block = None
            self.current_block_shape = None
            self.all_sprites.add(self.static_blocks)
            self.all_sprites.update()
            self.turn_static = False

            self._initialize_shape()

    def rotate_block():









    def _block_can_move(self, block, d_x=0, d_y=0):
        """Checks, if block can move in a certain direction, or if it collides.

        Args:
            block (Block): Block, that is trying to move.
            d_x (int):  How much piece should move to the x direction. Defaults to 0.
            d_y (int):  How much piece should move to the y direction. Defaults to 0.

        Returns:
            Boolean: True, if free space for block to move, False if block collides.
        """
        block.rect.move_ip(d_x, d_y)
        colliding_static_blocks = pygame.sprite.spritecollide(block, self.static_blocks, False)
        can_move = not colliding_static_blocks
        width = len(self.level_map[0])*self.cell_size
        height = len(self.level_map)*self.cell_size

        if block.rect.left < 0:
            can_move = False
        if block.rect.right > width:
            can_move = False
        if block.rect.bottom > height:
            can_move = False
            self.turn_static = True
        for i in self.static_blocks:
            if block.rect.topleft == i.rect.topleft and block.rect.topright == i.rect.topright:
                self.turn_static = True
        block.rect.move_ip(-d_x, -d_y)

        return can_move





    def clear_row(self):
        inc = 0
        
        for i in range(len(self.level_map)-1, -1, -1):
            row = self.level_map[i]
            if self.background not in row:
                inc +=1
                ind = i
                for j in range(len(row)):
                    try:
                        self.static_blocks.remove[(j+30,i+30)]
                    except:
                        continue

       