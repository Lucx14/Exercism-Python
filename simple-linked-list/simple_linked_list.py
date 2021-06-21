class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedList:
    def __init__(self, values=[]):
        self._head = None
        [self.push(val) for val in values]

    def __len__(self):
        length = 0
        node = self._head
        while node:
            node = node.next()
            length += 1
        return length

    def __iter__(self):
        values = []
        node = self._head
        while node:
            values.append(node.value())
            node = node.next()

        return iter(values)

    def head(self):
        if not self._head:
            raise EmptyListException()
        return self._head

    def push(self, value):
        node = Node(value)
        node._next = self._head
        self._head = node

    def pop(self):
        node = self.head()
        self._head = node.next()
        return node.value()

    def reversed(self):
        return reversed(list(self))


class EmptyListException(Exception):
    """Exception raised for an empty list"""

    def __init__(self, message="Error: List is empty"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"
