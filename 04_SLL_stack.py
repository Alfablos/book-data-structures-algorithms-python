"""Single Linked List Stack implementation"""


class LLStack:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, elem, next):
            self._element = elem
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, elem):
        self._head = self._Node(elem, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise IndexError('Attempting to fetch an element from an empty stack')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise IndexError('Attempting to fetch an element from an empty stack')
        result = self._head._element
        self._head = self._head._next
        self._size += 1
        return result









