from typing import Any, Generator


class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, elem):
        self._data.append(elem)

    def top(self):
        if len(self._data) == 0:
            raise IndexError('Calling top on an empty stack')
        return self._data[-1]

    def pop(self):
        if len(self._data) == 0:
            raise IndexError('Calling pop on an empty stack')

        return self._data.pop()


def reverse(l: list[Any]) -> Generator:
    store = ArrayStack()
    [store.push(e) for e in l]

    while not store.is_empty():
        yield store.pop()



def parenthesis_match(s: str) -> bool:
    opening = "([{"
    closing = ")]}"

    store = ArrayStack()

    for ch in s:
        if ch in opening:
            store.push(ch)
        elif ch in closing:
            if store.is_empty():
                return False
            # If we are closing, we must be closing the last opened one
            # round, square and braces have the SAME ORDER on both opening and closing
            if closing.index(ch) != opening.index(store.pop()):
                return False
    return store.is_empty()





li = [1, 2, 3]

rev = reverse(li)
for elem in rev:
    print(elem)

match = "((([[{}]])))"
print(f'{match} -> {parenthesis_match(match)}')

no_match = "((([[{}]]))))"
print(f'{no_match} -> {parenthesis_match(no_match)}')