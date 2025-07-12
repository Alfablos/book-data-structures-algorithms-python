"""Positional List implementation"""

from doubly_linked_list_DLL_07 import _DoublyLinkedListBase


class PositionalList(_DoublyLinkedListBase):
    class Position:
        def __init__(self, container, node: _DoublyLinkedListBase._Node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(self) is type(other) and self._node is other._node

        def __ne__(self, other):
            return not (self == other)


    def validate(self, pos: Position) -> _DoublyLinkedListBase._Node:
        if not isinstance(pos, self.Position):
            raise TypeError('Position is not of type PositionalList.Position.')

        if pos._container is not self:
            raise ValueError('Specified position does not belong to this list.')

        if pos._node._next is None:
            raise ValueError('Position is no longer valid.')

        return pos._node

    def _make_position(self, node: _DoublyLinkedListBase._Node) -> Position:
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)


    def first(self) -> Position:
        return self._make_position(self._header._next)

    def last(self) -> Position:
        return self._make_position(self._trailer._prev)

    def before(self, pos: Position) -> Position:
        node = self.validate(pos)
        return self._make_position(node._prev)

    def after(self, pos: Position) -> Position:
        node = self.validate(pos)
        return self._make_position(node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)


    # Override of the base class method
    def _insert_between(self, elem, previous, following) -> Position:
        node = super()._insert_between(elem, previous, following)
        return self._make_position(node)

    def add_first(self, elem) -> Position:
        return self._insert_between(elem, self._header, self._header._next)

    def add_last(self, elem) -> Position:
        return self._insert_between(elem, self._trailer._prev, self._trailer)

    def add_before(self, elem, pos) -> Position:
        node_at_pos = self.validate(pos)
        return self._insert_between(elem, node_at_pos._prev, node_at_pos)

    def add_after(self, elem, pos) -> Position:
        node_at_pos = self.validate(pos)
        return self._insert_between(elem, node_at_pos, node_at_pos._next)

    def delete(self, pos) -> _DoublyLinkedListBase._Node:
        node_at_pos = self.validate(pos)
        return self._delete_node(node_at_pos)

    def replace(self, elem, pos) -> _DoublyLinkedListBase._Node:
        node_from_pos = self.validate(pos)
        old = node_from_pos._element
        node_from_pos._element = elem
        return old


def insertion_sort(li: PositionalList):
    # Marker: right margin of the so far sorted sublist
    # Pivot: Marker + 1, the element to be placed
    # Walk: leftmost element with a value larger than the pivot

    if len(li) > 1:
        marker = li.first()
        while marker != li.last():
            pivot = li.after(marker)
            pivot_value = pivot.element()

            if pivot_value > marker.element():
                marker = pivot
            else:
                walk = marker
                while walk != li.first() and li.before(walk).element() > pivot_value:
                    walk = li.before(walk)
                li.delete(pivot)
                li.add_before(pivot_value, walk)


