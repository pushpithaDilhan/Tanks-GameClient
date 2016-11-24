import pygame
from groundcell import GroundCell
from brickcell import BrickCell
from watercell import WaterCell
from stonecell import StoneCell

#these are the size of a cell in pixels
CELL_WIDTH = 30
CELL_HEIGHT = 30
NUM_ROWS = 20
NUM_COLS = 20

class Board():
    def __init__(self):
        #when we construct, we define a data grid for our board 
        self.grid = [[0]*NUM_COLS for a in range(NUM_ROWS)]
        #here we define the Group variable
        self.cells = pygame.sprite.Group()
        
    #This method accepts a list of element cordinated (x,y) and type (0,-1,-2)
    #and apply them accordingly
    def set_terrain(self,coords,ttype):
        for cord in coords:
            self.grid[cord[0]][cord[1]] = ttype
    
    #this is the most important part
    def draw_board(self):
        #Loop everycell of the grid
        for i in range(NUM_ROWS):
            for j in range(NUM_COLS):
                #check the type of the cell
                if self.grid[i][j] == 0:
                    cell = GroundCell()
                elif self.grid[i][j] == -1:
                    cell = BrickCell()
                elif self.grid[i][j] == -2:
                    cell = StoneCell()
                elif self.grid[i][j] == -3:
                    cell = WaterCell()
                    
                
                #manually assign the x,y cordinates acording to our
                #width and height options
                x = j*CELL_WIDTH
                y = i*CELL_HEIGHT
                #also assign them to a rect, this is a requirement of a Sprite
                cell.rect = pygame.Rect(x,y,CELL_WIDTH,CELL_HEIGHT)
                #finally add it to the group we defined earlier
                self.cells.add(cell)
