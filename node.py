class Node:
    def __init__(self, x, y,state=None):
        self.x = x
        self.y = y
        if state is None:
            self.state = 'empty'
        else:
            self.state = state
        

    def __str__(self):
        return f"Node at ({self.x}, {self.y}), state: {self.state}"
    
    def __repr__(self):
        return f"Node at ({self.x}, {self.y}), state: {self.state}"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
