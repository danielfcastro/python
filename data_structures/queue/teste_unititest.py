import unittest

from data_structures.queue.deque import Deque
from data_structures.queue.queue import Queue
from data_structures.queue.priority_queue import PriorityQueue
from data_structures.queue.priority_queue import Node

queue = Queue()
deque = Deque()
priority_queue = PriorityQueue()

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
        self.assertEquals(10, elemento)

    def testPopEmpty(self):
        global linked_list
        queue.clear()
        elemento = queue.pop()
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

class TesPriorityQueueMethods(unittest.TestCase):
    def testPush(self):
        global priority_queue
        n = Node('Daniel', 10)
        priority_queue.clear()
        priority_queue.push(n)
        self.assertEquals(1, priority_queue.size())

    def testPop(self):
        global priority_queue
        priority_queue.clear()
        n1 = Node('Daniel', 10)
        n2 = Node('Jane', 20)
        n3 = Node('Arthur', 30)
        n4 = Node('David', 40)
        priority_queue.push(n1)
        priority_queue.push(n2)
        priority_queue.push(n3)
        priority_queue.push(n4)

        elemento = priority_queue.pop()
        self.assertEquals('David', elemento.getValue())

    def testPopEmpty(self):
        global priority_queue
        priority_queue.clear()
        elemento = priority_queue.pop()
        self.assertEquals(None, elemento)

    def testSize(self):
        global priority_queue
        priority_queue.clear()
        n1 = Node('Daniel', 10)
        n2 = Node('Jane', 20)
        n3 = Node('Arthur', 30)
        n4 = Node('David', 40)
        priority_queue.push(n1)
        priority_queue.push(n2)
        priority_queue.push(n3)
        priority_queue.push(n4)
        self.assertEquals(4, priority_queue.size())

    def testSizeFalse(self):
        global priority_queue
        priority_queue.clear()
        priority_queue.push(10)
        self.assertEquals(False, priority_queue.empty())

    def testEmptyTrue(self):
        global priority_queue
        priority_queue.clear()
        self.assertEquals(True, priority_queue.empty())

    def testFirst(self):
        global priority_queue
        priority_queue.clear()
        n = Node('Daniel', 10)
        priority_queue.push(n)
        self.assertEquals(True, priority_queue.first().equals(n))

    def testFirstNone(self):
        global priority_queue
        priority_queue.clear()
        self.assertEquals(None, priority_queue.first())

    def testShow(self):
        global priority_queue
        priority_queue.clear()
        n1 = Node('Daniel', 10)
        n2 = Node('Jane', 20)
        n3 = Node('Arthur', 30)
        n4 = Node('David', 40)
        priority_queue.push(n1)
        priority_queue.push(n2)
        priority_queue.push(n3)
        priority_queue.push(n4)
        priority_queue.show()
unittest.main
