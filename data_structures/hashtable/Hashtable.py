import sys

class Hashtable:

    def __init__(self, size):

        if size < 1:
            raise RuntimeError('Table Size must be positive')
        self._size = size
        self._table = [[] for i in range (size)]

    def hash(self, key):
        return key % self._size

    def insert (self, key):
        self._table[self.hash(key)].append(key)

    def show(self):

        for ll in self._table:
            if ll:
                for key in ll:
                    print('%d' % key, end=' ')
                print(' ')

    def search(self, key):
        if key in self._table[self.hash(key)]:
            return True
        return False

    def remove(self, key):
        hash_code = self.hash(key)
        if(self._table[hash_code] is not None):
            ll = self._table[hash_code]
            ll.remove(key)

