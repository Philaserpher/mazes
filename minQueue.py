from node import Node


class MinQueue:
    def __init__(self):
        self.Q = []

    def __sort(self):
        self.Q.sort()

    def __enqueue(self, node: Node):
        self.Q.append(node)
        self.__sort()

    def __dequeue(self) -> Node:
        self.__sort()
        node = self.Q[0]
        self.Q = self.Q[1:]
        self.__sort()
        return node

    def __is_empty(self) -> bool:
        return len(self.Q) == 0

    def __getitem__(self, index: int) -> Node:
        self.__sort()
        return self.Q[index]

    def __setitem__(self, index: int, node: Node):
        self.Q[index] = node
        self.__sort()

    def __iter__(self) -> "QueueIterator":
        return self.QueueIterator(self.Q)

    class QueueIterator:
        def __init__(self, queue: list):
            self._queue = queue
            self._index = 0

        def __iter__(self):
            return self

        def __next__(self) -> Node:
            if self._index < len(self._queue):
                item = self._queue[self._index]
                self._index += 1
                return item
            else:
                raise StopIteration

    def append(self, item: Node):
        self.__enqueue(item)

    def pop(self) -> Node:
        return self.__dequeue()

    def __bool__(self) -> bool:
        return not self.__is_empty()

    def __len__(self) -> int:
        return len(self.Q)

    def __str__(self) -> str:
        return f"MinQueue with {len(self.Q)} items"

    def __repr__(self) -> str:
        return f"MinQueue with {len(self.Q)} items"

    def clear(self):
        self.Q = []

    def __contains__(self, item: Node) -> bool:
        return item in self.Q

    def get_all(self) -> list:
        return self.Q
