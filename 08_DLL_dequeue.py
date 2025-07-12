""""LinkedDequeue implementation"""

from doubly_linked_list_DLL_07 import _DoublyLinkedListBase


class LinkedDequeue(_DoublyLinkedListBase):
    """Dequeue implementation using Doubly Linked Lists"""

    def first(self):
        """Returns the first element without removing it"""

        if self.is_empty():
            raise IndexError('Fetching the first element of an empty dequeue.')

        return self._header._next._element

    def last(self):
        """Returns the last element without removing it"""

        if self.is_empty():
            raise IndexError('Fetching the first element of an empty dequeue.')

    def insert_first(self, elem):
        self._insert_between(elem, self._header, self._header._next)

    def insert_last(self, elem):
        self._insert_between(elem, self._trailer._prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise IndexError('Deleting an element from an empty dequeue')

        self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise IndexError('Deleting an element from an empty dequeue')

        self._delete_node(self._trailer._prev)