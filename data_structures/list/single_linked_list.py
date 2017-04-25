class Node:
    def __init__(self, value, next_node):
        self._value = value
        self._next = next_node

    def has_next(self):
        if self._next is not None:
            return True
        return False


class LinkedList:
    def __init__(self, root=None):
        self._root = root
        if root is not None:
            self._size = 1
        else:
            self._size = 0

    def add(self, valor):
        _new_node = Node(valor, None)
        # add root node
        if self._size == 0:
            self._root = _new_node
        else:
            # get the old node
            _old = self.get(self._size - 1)
            # set to None because it will be added at the end
            _new_node._next = None
            # points the next node of the old last node to new_node
            _old._next = _new_node
        self._size += 1

    def addAt(self, valor, index):
        # raises exception if index is out of bounds
        if index < 0 or index > self._size:
            raise IndexError(' index is out of range')
        _new_node = Node(valor, None)

        if index == 0:
            # get the old node
            _old = self.get(0)
            # points the next node of the new node to the old node
            _new_node._next = _old
            # points the root to the new node
            self._root = _new_node
        else:
            # get the previous node
            _previous = self.get(index - 1)
            # sets the next node of the new node to be the same as the previous node's next node
            _new_node._next = _previous._next
            # sets the next node of the previous one to be the new node
            _previous._next = _new_node
        self._size += 1

    def delete(self, index):
        if index < 0 or index > self._size:
            raise IndexError(' index is out of range')
        _node = None
        if index == 0:
            if self._size == 1:
                self._root = None
            else:
                self._root = self._root._next
        elif index == self._size - 1:
            _previous = self.trasverse(index - 1)
            _previous._next = None
        else:
            _previous = self.trasverse(index - 1)
            _previous._next = _previous._next._next
        self._size -= 1

    def trasverse(self, length):
        if length > self._size:
            return None
        if length == 0:
            return self._root
        if length < 0:
            length = self._size
        _counter = 0
        _current = self._root
        while _current is not None:
            _current = _current._next
            _counter += 1
            if _counter == length:
                break
        return _current

    def clear(self):
        self._root = None
        self._size = 0

    def length(self):
        return self._size

    def empty(self):
        if self._size == 0:
            return True
        return False

    def get(self, index):
        if index > self._size:
            return None
        elif index < 0:
            index = self._size - 1
        counter = 0
        node = self._root

        if index == 0:
            return node

        while counter < index:
            node = node._next
            counter += 1
        return node

    def print(self):
        _current = self._root
        print("[", end='')
        while _current is not None:
            print(_current._value, end='')
            if _current._next is not None:
                print(" ,", end='')
            _current = _current._next
        print("]", end='')
