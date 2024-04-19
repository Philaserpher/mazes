from node import Node

class Maze:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.nodes = [[0 for _ in range(width)] for _ in range(height)]
        self.__populate()
    
    def __populate(self):
        for i in range(self.height):
            for j in range(self.width):
                self.nodes[i][j] = Node(j, i)

    def __getitem__(self, key: int) -> Node:
        return self.nodes[key[0]][key[1]]
    
    def __setitem__(self, key: int, value: Node):
        self.nodes[key[0]][key[1]] = value

    def __iter__(self):
        return self.MazeIterator(self)

    class MazeIterator():
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
        assert self.width * self.height == sum([len(row) for row in self.nodes])
        return self.width * self.height
    
    def __str__(self):
        return f"Maze of size {self.width}x{self.height}"
    
    def __repr__(self):
        return f"Maze of size {self.width}x{self.height}"
    
    def click_event(self, x, y, button):
        current = self[y, x].state
        if current != 'wall' and current != 'empty':
            return
        if button == "left":
            self[y, x].state = 'wall'
        elif button == "middle":
            if current == 'empty':
                self[y, x].state = 'wall'
            elif current == 'wall':
                self[y, x].state = 'empty'
        elif button == "right":
            self[y, x].state = 'empty'

