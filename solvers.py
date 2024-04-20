from maze import Maze
from minQueue import MinQueue


class Solver:

    def __init__(self):
        self.maze = None

    def solve(self):
        raise NotImplementedError(
            "Solve method must be implemented in subclass"
        )

    def get_draw_function(self, draw):
        if draw is None:
            return lambda: None
        return draw


class Dijkstra(Solver):

    def __init__(self):
        super().__init__()
        self.Q = MinQueue()

    def __reset(self, maze):
        self.Q = MinQueue()
        self.S = set()
        self.maze = maze

        self.height = self.maze.get_height()
        self.width = self.maze.get_width()

        self.start = self.maze.get_start()
        self.end = self.maze.get_end()

        self.__generate_Q()
        self.maze.reset_visited()
        self.maze[self.start[0], self.start[1]].set_d(0)

    def __generate_Q(self):
        self.Q.append(self.maze[self.start[0], self.start[1]])

    def solve(self, maze, draw=None):
        self.draw = self.get_draw_function(draw)
        self.__reset(maze)
        while self.Q:
            node_u = self.Q.pop()
            if node_u.is_end():
                self.draw_path(node_u)
                print("Dijkstra's algorithm complete")
                return
            self.S.add(node_u)
            v = self.__get_neighbours(node_u)
            for node_v in v:
                self.__relax(node_u, node_v)
                node_v.visit()
                if node_v not in self.Q:
                    self.Q.append(node_v)

            node_u.end_visit()
            self.draw()
        print("Dijkstra's algorithm could not find a solution")

    def __get_neighbours(self, node):
        neighbours = []
        y, x = node.x, node.y
        if x > 0 and self.maze[x - 1, y].state != "wall" and self.maze[x - 1, y] not in self.S:
            neighbours.append(self.maze[x - 1, y])
        if x < self.width - 1 and self.maze[x + 1, y].state != "wall" and self.maze[x + 1, y] not in self.S:
            neighbours.append(self.maze[x + 1, y])
        if y > 0 and self.maze[x, y - 1].state != "wall" and self.maze[x, y - 1] not in self.S:
            neighbours.append(self.maze[x, y - 1])
        if y < self.height - 1 and self.maze[x, y + 1].state != "wall" and self.maze[x, y + 1] not in self.S:
            neighbours.append(self.maze[x, y + 1])
        return neighbours
    
    def __relax(self, u, v):
        if v.get_d() > u.get_d() + 1:
            v.set_d(u.get_d() + 1)
            v.set_parent(u)

    def draw_path(self, node):
        node = node.parent
        while node.parent is not None:
            node.set_state("path")
            node = node.parent
            self.draw()
        node.set_state("start")
        self.draw()

