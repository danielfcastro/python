from data_structures.binary_search_tree.bynary_search_tree import Node
from data_structures.binary_search_tree.bynary_search_tree import BinarySearchTree

import math

class FatherLinkedNode(Node):
    def __init__(self, value, left_node=None, right_node=None, father_node=None):
        Node.__init__(self, value, left_node, right_node)
        self.__father = father_node

    def getFather(self):
        return self.__father

    def setFather(self, father_node):
        self.__father = father_node


class BalancedBinarySearchTree(BinarySearchTree):

    def BalancedBinarySearchTree(self, root=None):
        BinarySearchTree.__init__(self, root)

    def insert(self, root_node, value):
        new_node = FatherLinkedNode(value)
        # If the tree is empty, add it as the new root
        if root_node is None:
            self.setRoot(new_node)
            return

        # Otherwise checks if the current value is smaller than value of relative root
        # if that is the case then the new node must lies at left of its root
        elif value < root_node.getValue():
            #if the left node is None then we have found the spot to add the new node
            if root_node.getLeft() is None:
                root_node.setLeft(new_node)
                new_node.setFather(root_node)
                #self.balanceTree()
            # recursive call
            else:
                self.insert(root_node.getLeft(),value)
                return
        # Else it understands that the current value is bigger than value of relative root
        # if that is the case then the new node must lies at right of its root
        elif value > root_node.getValue():
            # if the right node is None then we have found the spot to add the new node
            if root_node.getRight() is None:
                root_node.setRight(new_node)
                new_node.setFather(root_node)
                # self.balanceTree()
            else:
                self.insert(root_node.getRight(),value)
                return
        else:
            raise RuntimeError('Element already exists')

    def treeAsList(self, curr_node, list = []):

        if curr_node is not None:
            list.append(curr_node.getValue())
            self.treeAsList(curr_node.getLeft(), list)
            self.treeAsList(curr_node.getRight(), list)
            list.sort()

    def __balance(self, list):
        if list is None:
            raise RuntimeError('Can not balance empty list')

        # divide the list in two parts
        first_lenght = math.ceil(len(list)/2)
        first_half = list[:first_lenght]
        second_half = list[first_lenght:]
        if len(first_half) > 0:
            mid_node = first_half.pop()
            self.insert(self.getRoot(), mid_node)
            self.__balance(first_half)

        if len(second_half) > 0:
            self.__balance(second_half)

    def balanceTree(self):
        list = []
        self.treeAsList(self.getRoot(), list)
        self.setRoot(None)

        # divide the list in two parts
        first_lenght = math.ceil(len(list)/2)
        first_half = list[:first_lenght]
        second_half = list[first_lenght:]
        mid_node = first_half.pop()
        self.insert(self.getRoot(), mid_node)
        self.__balance(first_half)
        self.__balance(second_half)