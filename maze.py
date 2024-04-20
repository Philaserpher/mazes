from node import Node
import random


class Maze:
    def __init__(self, width: int, height: int, random_density: int = 0.3):
        self.width = width
        self.height = height
        self.nodes = [[0 for _ in range(width)] for _ in range(height)]
        self.start = [None, None]
        self.end = [None, None]
        self.__populate()
        self.random_density = random_density

    def __populate(self):
        for i in range(self.height):
            for j in range(self.width):
                self.nodes[i][j] = Node(i, j)
        self.set_state(0, 0, "start")
        self.set_state(self.width - 1, self.height - 1, "end")

    def __getitem__(self, key: int) -> Node:
        return self.nodes[key[1]][key[0]]

    def __setitem__(self, key: int, value: Node):
        self.nodes[key[1]][key[0]] = value

    def __iter__(self):
        return self.MazeIterator(self)

    class MazeIterator:
        def __init__(self, maze):
            self.maze = maze
            self.x = 0
            self.y = 0

        def __next__(self):
            if self.y == self.maze.height:
                raise StopIteration
            node = self.maze.nodes[self.y][self.x]
            self.x += 1
            if self.x == self.maze.width:
                self.x = 0
                self.y += 1
            return node

    def __bool__(self):
        return any(self.nodes)

    def __len__(self):
        assert self.width * self.height == sum(
            [len(row) for row in self.nodes]
        )
        return self.width * self.height

    def __str__(self):
        return f"Maze of size {self.width}x{self.height}"

    def __repr__(self):
        return f"Maze of size {self.width}x{self.height}"

    def set_state(self, x, y, state):
        if self[x, y].is_special():
            if self[x, y].is_start():
                self.start = [None, None]
            elif self[x, y].is_end():
                self.end = [None, None]
        self[x, y].set_state(state)
        if state == "start":
            self.start = [x, y]
        elif state == "end":
            self.end = [x, y]

    def get_state(self, x, y):
        return self[x, y].state

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def click_event(self, row, col, button):
        current = self[row, col].state

        if button == "left":
            if self.start == [None, None]:
                self.set_state(row, col, "start")
            elif self.end == [None, None]:
                self.set_state(row, col, "end")
            else:
                self.set_state(row, col, "wall")
        elif button == "middle":
            if current == "empty":
                self.set_state(row, col, "wall")
            elif current == "wall":
                self.set_state(row, col, "empty")
        elif button == "right":
            self.set_state(row, col, "empty")

    def generate_random(self, keep_special=True):
        self.reset(keep_special=keep_special)
        for node in self:
            if random.random() < self.random_density:
                node.set_state("wall")
        if keep_special:
            if self.start == [None, None] or self.end == [None, None]:
                self.set_state(0, 0, "start")
                self.set_state(self.width - 1, self.height - 1, "end")
            else:
                self.set_state(self.start[0], self.start[1], "start")
                self.set_state(self.end[0], self.end[1], "end")
        else:
            self.start = [None, None]
            self.end = [None, None]

    def reset(self, keep_special=True):
        for node in self:
            node.set_state("empty")
        if keep_special:
            if self.start == [None, None] or self.end == [None, None]:
                self.start = [0, 0]
                self.end = [self.width - 1, self.height - 1]
            self[self.start].set_state("start")
            self[self.end].set_state("end")
        else:
            self.start = [None, None]
            self.end = [None, None]

    def reset_visited(self):
        for node in self:
            node.set_d(float("inf"))
            if node.state == "visited" or node.state == "visiting" or node.state == "path":
                node.set_state("empty")
