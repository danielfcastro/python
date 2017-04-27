import unittest

from data_structures.graphs.graph import Graph

graph = Graph(5)

graph.add_edge(1, 2)
graph.add_edge(4, 1)
graph.add_edge(2, 3)
graph.add_edge(2, 5)
graph.add_edge(5, 3)

# A classe abaixo herda de TestCase
class TestGraphMethods(unittest.TestCase):
    def testAddEdge(self):
        global graph
        graph.add_edge(5, 3)

        graph.depth_first_search(1)
        graph.breadth_first_search(1)
        #self.assertEquals(20, graph.getRoot().getRight().getRight().getRight().getValue())



unittest.main
