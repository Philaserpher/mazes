from maze import Maze
from node import Node
from mazeDrawer import MazeDrawer
from solvers import Dijkstra

if __name__ == "__main__":
    size = 20
    maze = Maze(size, size, random_density=0.3)

    dijkstra_solver = Dijkstra()
    solvers = [dijkstra_solver]

    renderer = MazeDrawer(
        maze, cell_size=[20, 20], line_thickness=2, solvers=solvers, rate=[1000, 40, 10, 1]
    )

    renderer.run()
