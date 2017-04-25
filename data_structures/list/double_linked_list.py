from data_structures.list.single_linked_list import Node, LinkedList


class DoubleLinkedNode(Node):
    def __init__(self, value, next_node, previous_node):
        Node.__init__(self, value, next_node)
        self._previous = previous_node


class DoubleLinkedList(LinkedList):
    def __init__(self, root=None):
        LinkedList.__init__(self, root)

    def add(self, valor):
        _new_node = DoubleLinkedNode(valor, None, None)
        # add root node
        if self._size == 0:
            self._root = _new_node
        else:
            # get the old node
            _old = self.get(self._size - 1)
            # set to None because it will be added at the end
            _new_node._next = None
            # set the previous node of the new node to be the old node
            _new_node.__previous = _old
            # points the next node of the old last node to new_node
            _old._next = _new_node
        self._size += 1

    def addAt(self, valor, index):
        # raises exception if index is out of bounds
        if index < 0 or index > self._size:
            raise IndexError(' index is out of range')
        _new_node = DoubleLinkedNode(valor, None, None)

        if index == 0:
            # get the old node
            _old = self.get(0)
            # points the next node of the new node to the old node
            _new_node._next = _old
            # set the previous node of the new node to be the old node
            _new_node.__previous = _old
            # points the root to the new node
            self._root = _new_node
        else:
            # get the previous node
            _previous = self.get(index - 1)
            # sets the next node of the new node to be the same as the previous node's next node
            _new_node._next = _previous._next
            # sets the previous node of the new node to be previous node
            _new_node.__previous = _previous
            # sets the next node of the previous one to be the new node
            _previous._next._previous = _new_node
            # sets the next node of the previous node to be new noe
            _previous._next = _new_node
        self._size += 1

    def delete(self, index):
        if index < 0 or index > self._size:
            raise IndexError(' index is out of range')
        # delete the root node
        if index == 0:
            # if the list is unitary
            if self._size == 1:
                self._root = None
            else:
                # sets the previous of the next node of the root to be None
                self._root._next._previous = None
                # sets the new root to be the next one of the old root
                self._root = self._root._next
        # deletes at the end
        elif index == self._size - 1:
            _previous = self.trasverse(index - 1)
            # this one is just to make sure the memory will be collected
            _previous._next._previous = None
            _previous._next = None
        # deletes along the list, not extremes
        else:
            # get the previous node of the to be deleted node
            _previous = self.trasverse(index - 1)
            # get the next node of the to be deleted node
            _next = _previous._next._next
            # sets the successor of the previous node to be the successor of the deleted node
            _previous._next = _next
            # sets the predecessor of the successor node of the deleted node to be the previous node of the deleted node
            _next._previous = _previous
        self._size -= 1
