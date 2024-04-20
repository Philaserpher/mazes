from maze import Maze
from minQueue import MinQueue


class Solver:

    def __init__(self):
        self.maze = None

    def solve(self):
        raise NotImplementedError(
            "Solve method must be implemented in subclass"
        )


class Dijkstra(Solver):

    def __init__(self):
        super().__init__()
        self.Q = MinQueue()

    def __reset(self, maze):
        self.Q = MinQueue()
        self.S = {}
        self.maze = maze

        self.height = self.maze.get_height()
        self.width = self.maze.get_width()

        self.start = self.maze.get_start()
        self.end = self.maze.get_end()

        self.__generate_Q()

        self.maze[self.start[0], self.start[1]].set_d(0)

    def __generate_Q(self):
        for node in self.maze:
            self.Q.append(node)

    def solve(self, maze):
        self.__reset(maze)
        node_u = self.Q.pop()
