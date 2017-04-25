import unittest

from data_structures.list.double_linked_list import DoubleLinkedList
from data_structures.list.single_linked_list import LinkedList

linked_list = LinkedList()
double_linked_list = DoubleLinkedList()


# A classe abaixo herda de TestCase
class TestSingleListMethods(unittest.TestCase):
    def testAdd(self):
        global linked_list
        linked_list.clear()
        linked_list.add(10)
        linked_list.print()
        self.assertEquals(10, linked_list.get(0)._value)

    def testAddAfter(self):
        global linked_list
        linked_list.clear()
        linked_list.add(10)
        linked_list.add(20)
        linked_list.add(30)
        linked_list.addAt(15, 1)
        linked_list.print()
        self.assertEquals(15, linked_list.get(1)._value)

    def testAddAfterNull(self):
        global linked_list
        linked_list.clear()
        linked_list.print()
        with self.assertRaises(IndexError):
            linked_list.addAt(10, 2)

    def testAddAfterNullBiggerThenSize(self):
        global linked_list
        linked_list.clear()
        linked_list.print()
        with self.assertRaises(IndexError):
            linked_list.addAt(10, 20)

    def testAddAfterBiggerThenSize(self):
        global linked_list
        linked_list.clear()
        linked_list.add(10)
        linked_list.add(20)
        linked_list.add(30)
        linked_list.print()
        with self.assertRaises(IndexError):
            linked_list.addAt(15, 50)

    def testDeleteEnd(self):
        global linked_list
        linked_list.clear()
        linked_list.add(10)
        linked_list.add(20)
        linked_list.add(30)
        linked_list.delete(2)
        linked_list.print()
        self.assertEquals(2, linked_list.length())

    def testDeleteBegin(self):
        global linked_list
        linked_list.clear()
        linked_list.add(10)
        linked_list.add(20)
        linked_list.add(30)
        linked_list.delete(0)
        linked_list.print()
        self.assertEquals(2, linked_list.length())

    def testDeleteBetween(self):
        global linked_list
        linked_list.clear()
        linked_list.add(10)
        linked_list.add(20)
        linked_list.add(30)
        linked_list.delete(1)
        linked_list.print()
        self.assertEquals(2, linked_list.length())

    def testDeleteNegative(self):
        global linked_list
        linked_list.clear()
        linked_list.add(10)
        linked_list.add(20)
        linked_list.add(30)
        linked_list.print()
        with self.assertRaises(IndexError):
            linked_list.delete(-10)


class TestDoubleListMethods(unittest.TestCase):
    def testAdd(self):
        global double_linked_list
        double_linked_list.clear()
        double_linked_list.add(10)
        double_linked_list.print()
        self.assertEquals(10, double_linked_list.get(0)._value)

    def testAddAfter(self):
        global double_linked_list
        double_linked_list.clear()
        double_linked_list.add(10)
        double_linked_list.add(20)
        double_linked_list.add(30)
        double_linked_list.addAt(15, 1)
        double_linked_list.print()
        self.assertEquals(15, double_linked_list.get(1)._value)

    def testAddAfterNull(self):
        global double_linked_list
        double_linked_list.clear()
        double_linked_list.print()
        with self.assertRaises(IndexError):
            double_linked_list.addAt(10, 2)

    def testAddAfterNullBiggerThenSize(self):
        global double_linked_list
        double_linked_list.clear()
        double_linked_list.print()
        with self.assertRaises(IndexError):
            double_linked_list.addAt(10, 20)

    def testAddAfterBiggerThenSize(self):
        global double_linked_list
        double_linked_list.clear()
        double_linked_list.add(10)
        double_linked_list.add(20)
        double_linked_list.add(30)
        double_linked_list.print()
        with self.assertRaises(IndexError):
            linked_list.addAt(15, 50)

    def testDeleteEnd(self):
        global double_linked_list
        double_linked_list.clear()
        double_linked_list.add(10)
        double_linked_list.add(20)
        double_linked_list.add(30)
        double_linked_list.delete(2)
        double_linked_list.print()
        self.assertEquals(2, double_linked_list.length())

    def testDeleteBegin(self):
        global double_linked_list
        double_linked_list.clear()
        double_linked_list.add(10)
        double_linked_list.add(20)
        double_linked_list.add(30)
        double_linked_list.delete(0)
        double_linked_list.print()
        self.assertEquals(2, double_linked_list.length())

    def testDeleteBetween(self):
        global double_linked_list
        double_linked_list.clear()
        double_linked_list.add(10)
        double_linked_list.add(20)
        double_linked_list.add(30)
        double_linked_list.delete(1)
        double_linked_list.print()
        self.assertEquals(2, double_linked_list.length())

    def testDeleteNegative(self):
        global double_linked_list
        double_linked_list.clear()
        double_linked_list.add(10)
        double_linked_list.add(20)
        double_linked_list.add(30)
        double_linked_list.print()
        with self.assertRaises(IndexError):
            linked_list.delete(-10)


unittest.main
