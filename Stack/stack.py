# Stack implementation
from typing import Union, List

class Stack:

    def __init__(self) -> None:
        self._data = []

    def __len__(self) -> int:
        # returns length of stack
        return len(self._data)

    def is_empty(self) -> bool:
        # returns True if stack is empty
        return len(self._data) == 0

    def top(self) -> Union[int, str]:
        # return element on top of stack
        if self.is_empty():
            raise Empty("No elements in stack.")
        return self._data[-1]

    def pop(self) -> List:
        if self.is_empty():
            raise Empty("No elements in stack.")
        return self._data.pop()
