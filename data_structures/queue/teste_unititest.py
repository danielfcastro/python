import unittest

from data_structures.queue.deque import Deque
from data_structures.queue.queue import Queue

queue = Queue()
deque = Deque()


# A classe abaixo herda de TestCase
class TesQueueMethods(unittest.TestCase):
    def testPush(self):
        global linked_list
        queue.clear()
        queue.push(10)
        self.assertEquals(1, queue.size())

    def testPop(self):
        global linked_list
        queue.clear()
        queue.push(10)
        queue.push(5)
        queue.push(8)
        elemento = queue.pop()
        print(elemento)
        self.assertEquals(10, elemento)

    def testPopEmpty(self):
        global linked_list
        queue.clear()
        elemento = queue.pop()
        print(elemento)
        self.assertEquals(None, elemento)

    def testSize(self):
        global linked_list
        queue.clear()
        queue.push(10)
        queue.push(8)
        self.assertEquals(2, queue.size())

    def testSizeFalse(self):
        global linked_list
        queue.clear()
        queue.push(10)
        self.assertEquals(False, queue.empty())

    def testEmptyTrue(self):
        global linked_list
        queue.clear()
        self.assertEquals(True, queue.empty())

    def testFirst(self):
        global linked_list
        queue.clear()
        queue.push(10)
        self.assertEquals(10, queue.first())

    def testFirstNone(self):
        global linked_list
        queue.clear()
        self.assertEquals(None, queue.first())


# A classe abaixo herda de TestCase
class TesDequeMethods(unittest.TestCase):
    def testPushFront(self):
        global deque
        deque.push_back(10)
        deque.push_back(20)
        deque.push_back(30)
        deque.push_back(40)
        deque.push_back(50)
        deque.push_back(60)
        deque.push_back(70)
        deque.push_back(80)
        deque.push_front(-10)
        self.assertEquals(-10, deque.first())

    def testPushBack(self):
        global deque
        deque.push_back(10)
        deque.push_back(20)
        deque.push_back(30)
        deque.push_back(40)
        deque.push_back(50)
        deque.push_back(60)
        deque.push_back(70)
        deque.push_back(80)
        deque.push_back(1000)
        self.assertEquals(1000, deque.last())

    def testPopFront(self):
        global deque
        deque.push_back(10)
        deque.push_back(20)
        deque.push_back(30)
        deque.push_back(40)
        deque.push_back(50)
        deque.push_back(60)
        deque.push_back(70)
        deque.push_back(80)
        elemento = deque.pop_front()
        print(elemento)
        self.assertEquals(10, elemento)

    def testPopFrontEmpty(self):
        global deque
        deque.push_back(10)
        deque.push_back(20)
        deque.push_back(30)
        deque.push_back(40)
        deque.push_back(50)
        deque.push_back(60)
        deque.push_back(70)
        deque.push_back(80)
        deque.clear()
        elemento = deque.pop_front()
        print(elemento)
        self.assertEquals(None, elemento)

    def testPopBack(self):
        global deque
        deque.push_back(10)
        deque.push_back(20)
        deque.push_back(30)
        deque.push_back(40)
        deque.push_back(50)
        deque.push_back(60)
        deque.push_back(70)
        deque.push_back(80)
        elemento = deque.pop_back()
        print(elemento)
        self.assertEquals(80, elemento)

    def testPopBackEmpty(self):
        global deque
        deque.push_back(10)
        deque.push_back(20)
        deque.push_back(30)
        deque.push_back(40)
        deque.push_back(50)
        deque.push_back(60)
        deque.push_back(70)
        deque.push_back(80)
        deque.clear()
        elemento = deque.pop_back()
        print(elemento)
        self.assertEquals(None, elemento)

    def testSize(self):
        global deque
        deque.push_back(10)
        deque.push_back(20)
        deque.push_back(30)
        deque.push_back(40)
        deque.push_back(50)
        deque.push_back(60)
        deque.push_back(70)
        deque.push_back(80)
        self.assertEquals(8, deque.size())

    def testSize(self):
        global deque
        deque.push_back(10)
        deque.push_back(20)
        deque.push_back(30)
        deque.push_back(40)
        deque.push_back(50)
        deque.push_back(60)
        deque.push_back(70)
        deque.push_back(80)
        deque.clear()
        self.assertEquals(0, deque.size())

    def testFirst(self):
        global deque
        deque.push_back(10)
        deque.push_back(20)
        deque.push_back(30)
        deque.push_back(40)
        deque.push_back(50)
        deque.push_back(60)
        deque.push_back(70)
        deque.push_back(80)
        self.assertEquals(10, deque.first())

    def testFirstNone(self):
        global deque
        deque.push_back(10)
        deque.push_back(20)
        deque.push_back(30)
        deque.push_back(40)
        deque.push_back(50)
        deque.push_back(60)
        deque.push_back(70)
        deque.push_back(80)
        deque.clear()
        self.assertEquals(None, deque.first())

    def testLast(self):
        global deque
        deque.push_back(10)
        deque.push_back(20)
        deque.push_back(30)
        deque.push_back(40)
        deque.push_back(50)
        deque.push_back(60)
        deque.push_back(70)
        deque.push_back(80)
        self.assertEquals(80, deque.last())

    def testFirstNone(self):
        global deque
        deque.push_back(10)
        deque.push_back(20)
        deque.push_back(30)
        deque.push_back(40)
        deque.push_back(50)
        deque.push_back(60)
        deque.push_back(70)
        deque.push_back(80)
        deque.clear()
        self.assertEquals(None, deque.last())


unittest.main
