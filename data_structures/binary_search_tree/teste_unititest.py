import unittest

from data_structures.binary_search_tree.bynary_search_tree import BinarySearchTree
from data_structures.binary_search_tree.balanced_binary_search_tree import BalancedBinarySearchTree

binary_search_tree = BinarySearchTree()

binary_search_tree.insert(binary_search_tree.getRoot(), 8)
binary_search_tree.insert(binary_search_tree.getRoot(), 3)
binary_search_tree.insert(binary_search_tree.getRoot(), 1)
binary_search_tree.insert(binary_search_tree.getRoot(), 6)
binary_search_tree.insert(binary_search_tree.getRoot(), 4)
binary_search_tree.insert(binary_search_tree.getRoot(), 7)
binary_search_tree.insert(binary_search_tree.getRoot(), 10)
binary_search_tree.insert(binary_search_tree.getRoot(), 14)
binary_search_tree.insert(binary_search_tree.getRoot(), 13)
binary_search_tree.show_pre_order(binary_search_tree.getRoot())


balanced_binary_search_tree = BalancedBinarySearchTree()
balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 8)
balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 3)
balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 1)
balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 6)
balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 4)
balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 7)
balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 10)
balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 14)
balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 13)
balanced_binary_search_tree.show_pre_order(balanced_binary_search_tree.getRoot())


# A classe abaixo herda de TestCase
class TestBinarySearchTreeMethods(unittest.TestCase):
    def testAdd(self):
        global binary_search_tree
        binary_search_tree.insert(binary_search_tree.getRoot(), 20)
        self.assertEquals(20, binary_search_tree.getRoot().getRight().getRight().getRight().getValue())

    def testRemoveLeaf(self):
        global binary_search_tree
        binary_search_tree.clear()
        binary_search_tree.insert(binary_search_tree.getRoot(), 8)
        binary_search_tree.insert(binary_search_tree.getRoot(), 3)
        binary_search_tree.insert(binary_search_tree.getRoot(), 1)
        binary_search_tree.insert(binary_search_tree.getRoot(), 6)
        binary_search_tree.insert(binary_search_tree.getRoot(), 4)
        binary_search_tree.insert(binary_search_tree.getRoot(), 7)
        binary_search_tree.insert(binary_search_tree.getRoot(), 10)
        binary_search_tree.insert(binary_search_tree.getRoot(), 14)
        binary_search_tree.insert(binary_search_tree.getRoot(), 13)
        binary_search_tree.insert(binary_search_tree.getRoot(), 20)
        binary_search_tree.remove(binary_search_tree.getRoot(), 20)
        #binary_search_tree.show_pre_order(binary_search_tree.getRoot())
        binary_search_tree.show_pre_order(binary_search_tree.getRoot())
        #self.assertEquals(13, binary_search_tree.getRoot().getRight().getRight().getLeft().getValue())

    def testRemoveFatherOneSon(self):
        global binary_search_tree
        binary_search_tree.clear()
        binary_search_tree.insert(binary_search_tree.getRoot(), 8)
        binary_search_tree.insert(binary_search_tree.getRoot(), 3)
        binary_search_tree.insert(binary_search_tree.getRoot(), 1)
        binary_search_tree.insert(binary_search_tree.getRoot(), 6)
        binary_search_tree.insert(binary_search_tree.getRoot(), 4)
        binary_search_tree.insert(binary_search_tree.getRoot(), 7)
        binary_search_tree.insert(binary_search_tree.getRoot(), 10)
        binary_search_tree.insert(binary_search_tree.getRoot(), 14)
        binary_search_tree.insert(binary_search_tree.getRoot(), 13)
        binary_search_tree.remove(binary_search_tree.getRoot(), 14)
        #binary_search_tree.show_pre_order(binary_search_tree.getRoot())
        binary_search_tree.show_pre_order(binary_search_tree.getRoot())
        #self.assertEquals(13, binary_search_tree.getRoot().getRight().getRight().getValue())

    def testRemoveFatherTwoSon(self):
        global binary_search_tree
        binary_search_tree.clear()
        binary_search_tree.insert(binary_search_tree.getRoot(), 8)
        binary_search_tree.insert(binary_search_tree.getRoot(), 3)
        binary_search_tree.insert(binary_search_tree.getRoot(), 1)
        binary_search_tree.insert(binary_search_tree.getRoot(), 6)
        binary_search_tree.insert(binary_search_tree.getRoot(), 4)
        binary_search_tree.insert(binary_search_tree.getRoot(), 7)
        binary_search_tree.insert(binary_search_tree.getRoot(), 10)
        binary_search_tree.insert(binary_search_tree.getRoot(), 14)
        binary_search_tree.insert(binary_search_tree.getRoot(), 13)
        binary_search_tree.remove(binary_search_tree.getRoot(), 6)
        #binary_search_tree.show_pre_order(binary_search_tree.getRoot())
        binary_search_tree.show_pre_order(binary_search_tree.getRoot())
        #self.assertEquals(13, binary_search_tree.getRoot().getRight().getRight().getValue())


# A classe abaixo herda de TestCase
class TestBalancedBinarySearchTreeMethods(unittest.TestCase):
    def testAdd(self):
        global balanced_binary_search_tree
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 20)
        balanced_binary_search_tree.show_pre_order(balanced_binary_search_tree.getRoot())
        #self.assertEquals(20, balanced_binary_search_tree.getRoot().getRight().getRight().getRight().getValue())

    def testRemoveLeaf(self):
        global balanced_binary_search_tree
        balanced_binary_search_tree.clear()
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 8)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 3)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 1)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 6)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 4)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 7)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 10)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 14)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 13)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 20)
        balanced_binary_search_tree.remove(balanced_binary_search_tree.getRoot(), 20)
        #balanced_binary_search_tree.show_pre_order(balanced_binary_search_tree.getRoot())
        balanced_binary_search_tree.show_pre_order(balanced_binary_search_tree.getRoot())
        #self.assertEquals(13, balanced_binary_search_tree.getRoot().getRight().getRight().getLeft().getValue())

    def testRemoveAbsentNode(self):
        global balanced_binary_search_tree
        balanced_binary_search_tree.clear()
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 8)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 3)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 1)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 6)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 4)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 7)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 10)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 14)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 13)
        with self.assertRaises(RuntimeError):
            balanced_binary_search_tree.remove(balanced_binary_search_tree.getRoot(), 15)
        #balanced_binary_search_tree.show_pre_order(balanced_binary_search_tree.getRoot())
        balanced_binary_search_tree.show_pre_order(balanced_binary_search_tree.getRoot())

    def testRemoveFatherOneSon(self):
        global balanced_binary_search_tree
        balanced_binary_search_tree.clear()
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 8)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 3)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 1)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 6)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 4)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 7)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 10)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 14)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 13)
        balanced_binary_search_tree.remove(balanced_binary_search_tree.getRoot(), 14)
        #balanced_binary_search_tree.show_pre_order(balanced_binary_search_tree.getRoot())
        balanced_binary_search_tree.show_pre_order(balanced_binary_search_tree.getRoot())
        #self.assertEquals(13, balanced_binary_search_tree.getRoot().getRight().getRight().getValue())

    def testRemoveFatherTwoSon(self):
        global balanced_binary_search_tree
        balanced_binary_search_tree.clear()
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 8)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 3)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 1)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 6)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 4)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 7)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 10)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 14)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 13)
        balanced_binary_search_tree.remove(balanced_binary_search_tree.getRoot(), 6)
        #balanced_binary_search_tree.show_pre_order(balanced_binary_search_tree.getRoot())
        balanced_binary_search_tree.show_pre_order(balanced_binary_search_tree.getRoot())
        #self.assertEquals(13, balanced_binary_search_tree.getRoot().getRight().getRight().getValue())

    def testBalance(self):
        global balanced_binary_search_tree
        balanced_binary_search_tree.clear()
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 8)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 3)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 1)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 6)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 4)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 7)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 10)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 14)
        balanced_binary_search_tree.insert(balanced_binary_search_tree.getRoot(), 13)
        balanced_binary_search_tree.remove(balanced_binary_search_tree.getRoot(), 6)
        #balanced_binary_search_tree.show_pre_order(balanced_binary_search_tree.getRoot())
        print('Unbalanced Tree - ', end=' ')
        balanced_binary_search_tree.show_pre_order(balanced_binary_search_tree.getRoot())
        print(' ')
        print('Balanced Tree - ', end=' ')
        balanced_binary_search_tree.balanceTree()
        balanced_binary_search_tree.show_pre_order(balanced_binary_search_tree.getRoot())
        #self.assertEquals(13, balanced_binary_search_tree.getRoot().getRight().getRight().getValue())

unittest.main
