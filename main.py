from maze import Maze
from node import Node
from mazeDrawer import MazeDrawer
from colours import ColourConverter
import random

if __name__ == "__main__":
    size = 40
    maze = Maze(size, size)
    for node in maze:
        if random.randint(0, 1) == 0:
            node.state = 'wall'
        else:
            node.state = 'empty'
    maze[0, 0].state = 'start'
    maze[size - 1, size - 1].state = 'end'

    renderer = MazeDrawer(maze, [20, 20], 2)
    renderer.run()