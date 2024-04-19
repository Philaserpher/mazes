import pygame
import sys
from colours import ColourConverter

class MazeDrawer:
    def __init__(self, maze, cell_size=[20, 20], line_thickness = 1):
        self.maze = maze
        self.cell_size = cell_size
        self.line_thickness = line_thickness

        self.c2n = ColourConverter().get_num
        self.n2c = ColourConverter().get_colour

        pygame.init()
        width = maze.width * cell_size[0] + (maze.width + 1) * line_thickness
        height = maze.height * cell_size[1] + (maze.height + 1) * line_thickness

        self.dragging = False
        self.old_node_coords = (None, None)
        self.button = None

        self.screen = pygame.display.set_mode((width, height))
        self.screen.fill((0, 0, 0))
        self.clock = pygame.time.Clock()

    def draw(self):
        for y in range(self.maze.height):
            for x in range(self.maze.width):
                color = self.c2n(self.maze[y, x].state)
                cell_x = x * (self.cell_size[0] + self.line_thickness) + self.line_thickness
                cell_y = y * (self.cell_size[1] + self.line_thickness) + self.line_thickness
                pygame.draw.rect(self.screen, color, (cell_x, cell_y, self.cell_size[0], self.cell_size[1]))
        pygame.display.flip()

    def change_cell(self, pos, hold=True, button="left"):
        x, y = pos
        x = x // (self.cell_size[0] + self.line_thickness)
        y = y // (self.cell_size[1] + self.line_thickness)
        if (x, y) == self.old_node_coords and hold == True and button == "middle":
            return
        self.old_node_coords = (x, y)
        self.maze.click_event(x, y, button)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.button = "left"
                    self.dragging = True
                    self.change_cell(pygame.mouse.get_pos(), hold=False, button=self.button)
                if event.button == 2:
                    self.button = "middle"
                    self.dragging = True
                    self.change_cell(pygame.mouse.get_pos(), hold=False, button=self.button)
                if event.button == 3:
                    self.button = "right"
                    self.dragging = True
                    self.change_cell(pygame.mouse.get_pos(), hold=False, button=self.button)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.dragging = False
            elif event.type == pygame.MOUSEMOTION and self.dragging:
                self.change_cell(pygame.mouse.get_pos(), hold=True, button=self.button)
                

    def update(self):
        self.handle_events()
        self.draw()
        self.clock.tick(1000)        

    def run(self):
        while True:
            self.update()
            self.clock.tick(60)
