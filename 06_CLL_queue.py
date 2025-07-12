"""Circular Queue implementation"""


class CircularQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, elem, next):
            self._element = elem
            self._next = next

    def __init__(self):
        # No head is set because the head is linked to the tail (head = tail.next) so there's no need to explicitly define it!
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise IndexError('Retrieving the first element of an empty queue.')

        head = self._tail._next
        return head._element

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Retrieving an element of an empty queue.')

        old_head = self._tail._next

        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = old_head._next

        self._size -= 1

        return old_head

    def enqueue(self, elem):
        new = self._Node(elem, None)

        if self.is_empty():
            new._next = new
        else:
            # new becomes the new tail
            new._next = self._tail._next
            self._tail._next = new
        self._tail = new

        self._size += 1



