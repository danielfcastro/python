from data_structures.queue.basequeue import BaseQueue


class Queue(BaseQueue):
    def __init__(self):
        BaseQueue.__init__(self)

    def push(self, element):
        self._queue.append(element)
        self._length += 1

    def pop(self):
        element = None
        if not self.empty():
            element = self._queue.pop(0)
            self._length -= 1
        return element
