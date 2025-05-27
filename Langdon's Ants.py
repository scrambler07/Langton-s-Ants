import pygame as pg
import sys
import random
import numpy as np
pg.init()

red = (255,0,0)
black = (0,0,0)
white = (200,200,200)
window_width = 1000
window_height = 700
block_size = 5

screen = pg.display.set_mode((window_width,window_height))
screen.fill(white)          
pg.display.set_caption("Langton's Ants")



class Cell:
    def __init__(self, x, y):
        self.x, self.y = x,y
        self.color = white
        self.pheromone = 0
        self.step = 5                   # tracks record of number of movements performed after pheromone deployment 

    def draw(self):
        rect = pg.Rect(block_size*self.x, block_size*self.y, block_size, block_size)
        pg.draw.rect(screen, self.color, rect)

    def update(self):
        if self.pheromone != 0:
            if self.step != 5 :
                self.step += 1
            else:
                self.pheromone = 0



class Ant:

    def __init__(self,id):
        self.x = random.randint(int(window_width/block_size* 0.35), int(window_width/block_size*0.65)-1)
        self.y = random.randint(int(window_height/block_size* 0.35), int(window_height/block_size*0.65)-1)
        self.direction = random.choice(['N','E','W','S'])
        self.direction_changes = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
        self.reverse_changes = {'N': 'W', 'E': 'N', 'S': 'E', 'W': 'S'}
        self.id = id     

        # Method 'id' is used to find the ant who deployed a particular pheromone                                                 


    def draw(self):
        rect = pg.Rect(block_size*self.x, block_size*self.y, block_size, block_size)
        pg.draw.rect(screen, red, rect)

    def normalMove(self):
        if cells[self.x][self.y].color == white:
            self.direction = self.direction_changes[self.direction]
        else:
            self.direction = self.reverse_changes[self.direction]

    def selfPheromone(self,k):
        #for pheromone decay
        p = 0.8 - 0.16*k  
        x  = np.random.choice([0,1],p = [p, 1-p])       # '1' for normal movement, '0' for pheromone-influenced movement
        if x:
            self.normalMove()

        
    def crossPheromone(self,k):
        p = 0.2 - 0.04*k
        x = np.random.choice([0,1],p = [p, 1-p])        # '1' for normal movement, '0' for pheromone-influenced movement        
        if x:
            self.normalMove()



    def walk(self):

        movements = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}
        if cells[self.x][self.y].pheromone == self.id:
            self.selfPheromone(cells[self.x][self.y].step)

        elif cells[self.x][self.y].pheromone != 0:
            self.crossPheromone(cells[self.x][self.y].step)
        
        else:
            self.normalMove()

        if cells[self.x][self.y].color == white:
            cells[self.x][self.y].color = black
        else:
            cells[self.x][self.y].color = white

        cells[self.x][self.y].pheromone = self.id
        cells[self.x][self.y].step = -1

        move = movements[self.direction]
        self.x += move[0]
        self.y += move[1]

    
#assigning position to cells
cells = []
for x in range(int(window_width/block_size)):
    cell_column = []
    for y in range(int(window_height/block_size)):
        cell_column.append(Cell(x, y))
    
    cells.append(cell_column)

#creating ant instances
#number of ants is scalable
ants = []
for i in range(1,3):
    ants.append(Ant(i))


while 1:

    #for closing when window close button is pressed
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()


    for ant in ants:
        ant.walk()

    #updating cell data and cell color
    for cell_column in cells:
        for cell in cell_column:
            cell.update()
            cell.draw()

    #updating ant position in simulation
    for ant in ants:
        ant.draw()

    pg.display.update()
