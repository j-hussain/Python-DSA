# Queue implementation

from typing import Union, List

class Queue:

    """

        Queue ADT defines collection that keeps objects sequentially.
        Access is on a FIFO basis.

        Methods:
            - enqueue() : add element to back of queue
            - dequeue() : remove and return first element of queue
            - first() : reference to element at front of Q without removal

    """
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * Queue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def _resize(self, new_tail: int) -> None:
        prev_data = self._data
        self._data = [None] * new_tail
        walk = self._front
        for k in range(self._size):
            self._data[k] = prev_data[walk]
            walk = (1 + walk) % len(prev_data)
        self._front = 0

    def enqueue(self, e: Union[str, int]) -> None:
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1


    def dequeue(self) -> Union[int, str]:
        if self.is_empty():
            raise Empty("Queue is empty.")
        e = self._data[self._front]
        # assist garbage collection
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return e

    def first(self) -> Union[str, int]:
        if self.is_empty():
            raise Empty("Queue is empty.")
        return self._data[self._front]

    

    