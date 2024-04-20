import pygame
import sys
from colours import ColourConverter


class MazeDrawer:
    def __init__(
        self, maze, cell_size=[20, 20], line_thickness=1, solvers=[None], rate=[100, 10, 1, 0.5]
    ):
        self.maze = maze
        self.cell_size = cell_size
        self.line_thickness = line_thickness

        self.c2n = ColourConverter().get_num
        self.n2c = ColourConverter().get_colour

        pygame.init()
        self.rate = rate
        self.rate_index = 0
        self.current_rate = self.rate[self.rate_index]

        self.maze_width = maze.get_width()
        self.maze_height = maze.get_height()
        self.width = (
            self.maze_width * cell_size[0]
            + (self.maze_width + 1) * line_thickness
        )
        self.height = (
            self.maze_height * cell_size[1]
            + (self.maze_height + 1) * line_thickness
        )

        self.dragging = False
        self.old_node_coords = (None, None)
        self.button = None

        self.solvers = solvers

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill((0, 0, 0))
        self.clock = pygame.time.Clock()

    def draw(self):
        for y in range(self.maze_height):
            for x in range(self.maze_width):
                color = self.c2n(self.maze.get_state(x, y))
                cell_x = (
                    x * (self.cell_size[0] + self.line_thickness)
                    + self.line_thickness
                )
                cell_y = (
                    y * (self.cell_size[1] + self.line_thickness)
                    + self.line_thickness
                )
                pygame.draw.rect(
                    self.screen,
                    color,
                    (cell_x, cell_y, self.cell_size[0], self.cell_size[1]),
                )
        pygame.display.flip()

    def change_cell(self, pos, hold=True, button="left"):
        x, y = pos
        x = x // (self.cell_size[0] + self.line_thickness)
        y = y // (self.cell_size[1] + self.line_thickness)
        if (
            (x, y) == self.old_node_coords
            and hold == True
            and button == "middle"
        ):
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
                    self.change_cell(
                        pygame.mouse.get_pos(), hold=False, button=self.button
                    )
                if event.button == 2:
                    self.button = "middle"
                    self.dragging = True
                    self.change_cell(
                        pygame.mouse.get_pos(), hold=False, button=self.button
                    )
                if event.button == 3:
                    self.button = "right"
                    self.dragging = True
                    self.change_cell(
                        pygame.mouse.get_pos(), hold=False, button=self.button
                    )
            elif event.type == pygame.MOUSEBUTTONUP:
                self.dragging = False
            elif event.type == pygame.MOUSEMOTION and self.dragging:
                self.change_cell(
                    pygame.mouse.get_pos(), hold=True, button=self.button
                )
            elif event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_r or key == pygame.K_1:
                    self.maze.reset(keep_special=True)
                    self.draw()
                elif key == pygame.K_2:
                    self.maze.generate_random(keep_special=False)
                    self.draw()
                elif key == pygame.K_g or key == pygame.K_3:
                    self.maze.generate_random(keep_special=True)
                    self.draw()
                elif key == pygame.K_SPACE:
                    self.solvers[0].solve(self.maze, self.update)
                elif key == pygame.K_BACKSPACE:
                    self.rate_index = (self.rate_index + 1) % len(self.rate)
                    self.current_rate = self.rate[self.rate_index]

    def update(self):
        self.handle_events()
        self.draw()
        self.clock.tick(self.current_rate)

    def run(self):
        while True:
            self.update()
            self.clock.tick(60)
