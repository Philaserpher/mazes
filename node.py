class Node:
    def __init__(self, x, y, state=None):
        self.x = x
        self.y = y
        self.d = float("inf")
        if state is None:
            self.state = "empty"
        else:
            self.state = state

    def __str__(self):
        return (
            f"Node at ({self.x}, {self.y}), state: {self.state}, d: {self.d}."
        )

    def __repr__(self):
        return (
            f"Node at ({self.x}, {self.y}), state: {self.state}, d: {self.d}."
        )

    def __lt__(self, other):
        return self.d < other.d

    def set_state(self, state):
        self.state = state

    def is_start(self):
        return self.state == "start"

    def is_end(self):
        return self.state == "end"

    def is_special(self):
        return self.is_start() or self.is_end()

    def get_d(self):
        return self.d

    def set_d(self, d):
        self.d = d
