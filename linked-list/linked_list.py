class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self._value = value
        self._next = succeeding
        self._previous = previous

    def value(self):
        return self._value

    def next(self):
        return self._next

    def previous(self):
        return self._previous


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    def head(self):
        return self._head

    def tail(self):
        return self._tail

    def __len__(self):
        length = 0
        node = self._tail
        while node:
            node = node.next()
            length += 1
        return length

    def push(self, value):
        node = Node(value)

        if self._head == None and self._tail == None:
            self._head = node
            self._tail = node
        else:
            self._head._next = node
            node._previous = self._head
            self._head = node

    def pop(self):
        node = self._head
        self._head = node.previous()
        if self._head:
            self._head._next = None
        if node.previous() == None:
            self._tail = None
        return node.value()

    def shift(self):
        node = self._tail
        self._tail = node.next()
        if self._tail:
            self._tail._previous = None
        return node.value()

    def unshift(self, value):
        node = Node(value)

        if self._head == None and self._tail == None:
            self._head = node
            self._tail = node
        else:
            self._tail._previous = node
            node._next = self._tail
            self._tail = node

    def __iter__(self):
        values = []
        node = self._tail
        while node:
            values.append(node.value())
            node = node.next()

        return iter(values)
