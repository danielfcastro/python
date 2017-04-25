import unittest

from data_structures.stack.stack import Stack


# A classe abaixo herda de TestCase
class TesStackMethods(unittest.TestCase):
    def testPush(self):
        s = Stack()
        s.push(10)
        self.assertEquals(1, s.length())

    def testPop(self):
        s = Stack()
        s.push(10)
        elemento = s.pop()
        print(elemento)
        self.assertEquals(10, elemento)

    def testPopEmpty(self):
        s = Stack()
        elemento = s.pop()
        print(elemento)
        self.assertEquals(False, elemento)

    def testLenght(self):
        s = Stack()
        s.push(10)
        s.push(8)
        self.assertEquals(2, s.length())

    def testEmptyFalse(self):
        s = Stack()
        s.push(10)
        self.assertEquals(False, s.empty())

    def testEmptyTrue(self):
        s = Stack()
        self.assertEquals(True, s.empty())

    def testTop(self):
        s = Stack()
        s.push(10)
        self.assertEquals(10, s.top())

    def testTopNone(self):
        s = Stack()
        self.assertEquals(None, s.top())


unittest.main
