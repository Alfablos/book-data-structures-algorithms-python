"""Array Queue implementation"""

class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * self.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        """Return but not remove the first element"""
        if self.is_empty():
            raise IndexError('Trying to fetch the first element of an empty queue')

        return self._data[self._front]

    def dequeue(self):
        """Retrieve the first element removing it from the queue"""
        if self.is_empty():
            raise IndexError('Trying to fetch elements from an empty queue')

        result = self._data[self._front]
        self._data[self._front] = None

        # Shift
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1

        return result

    def _resize(self, new_length):
        old_data = self._data
        old_front_index = self._front

        # Allocate
        self._data = [None] * new_length

        # Resize will affect the underlying array size,
        # not the data that's stored
        for k in range(self._size):
            # Transfer data: the future array will start from the beginning,
            # but there's no guarantee that the old one does.
            # This is due to the fact that this is a circular array structure
            self._data[k] = old_data[old_front_index]
            # like word wrapping % makes sure that, in case of "overflow" we restart
            # counting from 0
            old_front_index = (old_front_index + 1) % len(old_data)
        # NOW that data has been transferred we can set the beginning index
        # to the beginning of the array
        self._front = 0

    def enqueue(self, elem):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))

        next_available_index = self._front + len(self._data) % len(self._data)
        self._data[next_available_index] = elem
        self._size += 1




