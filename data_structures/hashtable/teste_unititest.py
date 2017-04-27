import unittest

from data_structures.hashtable.Hashtable import Hashtable

hash_table = Hashtable(10)
hash_table.insert(19)
hash_table.insert(28)
hash_table.insert(20)
hash_table.insert(5)
hash_table.insert(33)


# A classe abaixo herda de TestCase
class TestHashTableMethods(unittest.TestCase):
    def testAdd(self):
        global hash_table
        hash_table.show()
        print(' Adding...')
        hash_table.insert(15)
        print(' Added...')
        hash_table.show()

    def testRemove(self):
        global binary_search_tree
        hash_table.show()
        print(' Removing...')
        hash_table.remove(15)
        hash_table.remove(20)
        print(' Removed...')
        hash_table.show()




unittest.main
