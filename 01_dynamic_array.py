import ctypes

class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._array = self._make_array(self._capacity)

    def append(self, element):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._array[self._n] = element
        self._n += 1

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def _resize(self, capacity):
        new = self._make_array(capacity)
        for i in range(len(self._array)):
            new[i] = self._array[i]
        self._array = new
        self._capacity = capacity

    def __len__(self):
        return self._n

    def __getitem__(self, idx):
        if not 0 < idx < self._n:
            raise IndexError("Invalid index")
        return self._array[idx]



def main():
    arr = DynamicArray()

    for i in range(50):
        arr.append(i)
        print(f'n_items: {arr._n}, capacity: {arr._capacity}')

    print(arr)



if __name__ == "__main__":
    main()
