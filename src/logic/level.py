import pygame
from sprites.blocks import Blocks
from shape.shape_indexes import ShapeIndexes
from shape.get_shape import GetShape
from window.map import Map

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
        self.end_screen = None
        self.score = 0
        self.window = Map()
        self.does_end= False

      

        self.created_blocks = []
        self.level_map = level_map

        self._initialize_background()

        

    def _initialize_background(self):
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
            self.background
        )


        self._initialize_shape()


    def _initialize_shape(self):
        """Creates payable tetris piece and adds it to the correct sprite group. 
        """

        if self.current_block_shape is None:
            self.current_block_shape = GetShape()

        if self.current_block is None:
            self.current_block = ShapeIndexes(5, 5, self.current_block_shape.shape)

        for i in self.current_block.indexes: # pylint: disable=invalid-name
            normalized_x = i[0] * self.cell_size
            normalized_y = i[1] * self.cell_size

            if self.current_block_shape.index == 2:
                block = Blocks(normalized_x, normalized_y-self.cell_size*3, self.current_block_shape.color)
                self.all_current_blocks.add(block)

            elif self.current_block_shape.index == 3 or self.current_block_shape.index == 1 or self.current_block_shape.index == 0:
                block = Blocks(normalized_x, normalized_y-self.cell_size*4, self.current_block_shape.color)
                self.all_current_blocks.add(block)


            else:
                block=Blocks(normalized_x, normalized_y-self.cell_size*3, self.current_block_shape.color)
                self.all_current_blocks.add(block)


        for block in self.all_current_blocks:
            collisions =pygame.sprite.spritecollide(block, self.static_blocks, False)
        is_ok = not collisions
        
        if is_ok is False:
            self.does_end= True            
 

        else:        
            self.all_sprites.add(
                self.all_current_blocks
            )
          
    def end(self):
        para = [self.does_end, self.score]
        return para


    def update(self, current_time):
        """Moves currently used piece down according to clock ticks.

        Args:
            current_time (Clock): Milliseconds since the start of the game.
        """
        if self.should_move(current_time):
            self.move_block(d_y=+self.cell_size)
            self.current_block_previous_move_time = current_time
        self.clear_row()


    def should_move(self, current_time):
        """Checks if a certain amount of time has passed

        Args:
            current_time (Clock): Milliseconds since the start of the game.

        Returns:
            Boolean: True, if a certain amount of time or more has passed, False if not.
        """
        return current_time - self.current_block_previous_move_time >= 500


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
        self.clear_row()       






    def rotate_block(self):
        self.rotation +=1
        if self.rotation == 4:
            self.rotation = 0
 
        i = 0
        n = 0
        for block in self.all_current_blocks:
            if n == 0:
                self.current_block = ShapeIndexes(block.rect.x/30, block.rect.y/30, self.current_block_shape.shape, self.rotation)
                break
            n += 1

        for block in self.all_current_blocks:
            if self.current_block_shape.index == 0: #toimii
                block.rect.x = self.cell_size * (self.current_block.indexes[i][0])
                block.rect.y = self.cell_size * (self.current_block.indexes[i][1]+3)
            elif self.current_block_shape.index == 1:
                block.rect.x = self.cell_size * (self.current_block.indexes[i][0])
                block.rect.y = self.cell_size * (self.current_block.indexes[i][1]+3)
            elif self.current_block_shape.index == 2:#toimii
                block.rect.x = self.cell_size * (self.current_block.indexes[i][0]+1)
                block.rect.y = self.cell_size * (self.current_block.indexes[i][1]+4)
            elif self.current_block_shape.index == 4:#toimii
                if self.rotation == 3:
                    block.rect.x = self.cell_size * (self.current_block.indexes[i][0]+2)
                    block.rect.y = self.cell_size * (self.current_block.indexes[i][1]+3)
                else:
                    block.rect.x = self.cell_size * (self.current_block.indexes[i][0])
                    block.rect.y = self.cell_size * (self.current_block.indexes[i][1]+3)
            elif self.current_block_shape.index == 5:
                block.rect.x = self.cell_size * (self.current_block.indexes[i][0])
                block.rect.y = self.cell_size * (self.current_block.indexes[i][1]+4)
            elif self.current_block_shape.index == 6:#toimii
                if self.rotation == 3:
                    block.rect.x = self.cell_size * (self.current_block.indexes[i][0]+1)
                    block.rect.y = self.cell_size * (self.current_block.indexes[i][1]+3)
                else:
                    block.rect.x = self.cell_size * (self.current_block.indexes[i][0])
                    block.rect.y = self.cell_size * (self.current_block.indexes[i][1]+3)
            i += 1

        









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

        if d_y > 0:
            for i in self.static_blocks:
                if block.rect.topleft == i.rect.topleft and block.rect.topright == i.rect.topright:
                    self.turn_static = True
        block.rect.move_ip(-d_x, -d_y)

        return can_move





    def clear_row(self):
        many=0
        
        for i in range((len(self.level_map)+1), 0, -1):
            for static in self.static_blocks:
                if static.rect.y == i*self.cell_size:
                    many+=1
            
            if many == len(self.level_map[0]):                
                self.score += 10
                self.window.window_text(self.score)

                for static in self.static_blocks:
                    if static.rect.y == i*self.cell_size:
                        self.static_blocks.remove(static)
                        self.static_blocks.update()
  
  
                for static in self.static_blocks:

                    if static.rect.y < i*self.cell_size:
                        static.rect.y += self.cell_size

                self.all_sprites.empty()
                self.all_sprites.add(
                    self.background,
                    self.static_blocks,
                    self.all_current_blocks
                )  
            many = 0        



       