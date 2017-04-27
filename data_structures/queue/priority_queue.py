from data_structures.queue.basequeue import BaseQueue

class Node:

    def __init__(self, value=None, priority = 0):
        self.__value = value
        self.__priority = priority


    def getValue(self):
        return self.__value


    def setValue(self, value):
        self.__value = value

    def getPriority(self):
        return self.__priority


    def setPriority(self, value):
        self.__priority = value

    def equals(self, other):
        if self.getValue() == other.getValue() and self.getPriority() == other.getPriority():
            return True
        return False


class PriorityQueue(BaseQueue):

    def __init__(self):
        BaseQueue.__init__(self)

    def push(self, element):
        if self.empty():
            self._queue.append(element)
        else:
            for i in range(self.size()):
                if self._queue[i].getPriority() < element.getPriority():
                    self._queue.insert(i, element)
                    flag_push = True
                    break
            if not flag_push:
                self._queue.insert(self.size(), element)

        self._length += 1

    def pop(self):
        element = None
        if not self.empty():
            element = self._queue.pop(0)
            self._length -= 1
        return element

    def show(self):
        for p in self._queue:
            print('Value: %s' % p.getValue())
            print('Priority: %d\n' % p.getPriority())