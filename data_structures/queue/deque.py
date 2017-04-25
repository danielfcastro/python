from data_structures.queue.basequeue import BaseQueue


# Double Ended Queue
class Deque(BaseQueue):
    def __init__(self):
        BaseQueue.__init__(self)

    def push_front(self, elemento):
        self._queue.insert(0, elemento)
        self._length += 1

    def pop_front(self):
        elemento = None
        if not self.empty():
            elemento = self._queue.pop(0)
            self._length -= 1
        return elemento

    def push_back(self, elemento):
        if not self.empty():
            self._queue.insert(self.size(), elemento)
        else:
            self._queue.insert(0, elemento)
        self._length += 1

    def pop_back(self):
        elemento = None
        if not self.empty():
            elemento = self._queue.pop(self._length - 1)
            self._length -= 1
        return elemento
