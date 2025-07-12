"""Implementation of the base class for doubly linked list based classes"""


class _DoublyLinkedListBase:
    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, elem, prev, next):
            self._element = elem
            self._prev = prev
            self._next = next

    def __init__(self):
        # Header and Trailer are sentinels, they don't carry any
        # element but facilitate inserting and deleting
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._next = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, elem, previous, following):
        new = self._Node(elem, previous, following)
        previous._next = new
        following._prev = new

        self._size += 1
        return new

    def _delete_node(self, node: _Node):
        """Delete a node returning its content"""
        previous = node._prev
        following = node._next
        element = node._element

        previous._next = following
        following._prev = previous

        # Damnatio memoriae for node
        node._prev = node._next = node._element = None

        self._size -= 1
        return element




