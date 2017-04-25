class BaseQueue:
    def __init__(self):
        self._queue = []
        self._length = 0

    def empty(self):
        if self._length == 0:
            return True
        return False

    def size(self):
        return self._length

    def first(self):
        if not self.empty():
            return self._queue[0]
        return None

    def last(self):
        if not self.empty():
            return self._queue[-1]
        return None

    def clear(self):
        if not self.empty():
            self._queue.clear()
            self._length = 0

    def show(self):
        for i in self._queue:
            print(i, end=' ')
