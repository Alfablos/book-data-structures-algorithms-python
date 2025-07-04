"""Single Linked List Queue implementation"""


class LinkedQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, elem, next):
            self._element = elem
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise IndexError('Attempting to retrieve the first element of an empty queue')
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Attempting to retrieve an element from an empty queue')

        result = self.first()
        self._head = self._head._next
        self._size -= 1

        if self.is_empty():     # In case head and tail were the same
            self._tail = None

        return result


    def enqueue(self, elem):                # New elements at the end
        new = self._Node(elem, self._head)

        if self.is_empty():
            self._head = new
        else:
            self._tail = new

        self._tail = new                    # Anyway
        self._size += 1




