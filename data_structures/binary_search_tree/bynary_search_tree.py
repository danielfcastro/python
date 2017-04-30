class Node:
    def __init__(self, value, left_node=None, right_node=None):
        self.__left_node = left_node
        self.__right_node = right_node
        self.__value = value

    def getValue(self):
        return self.__value

    def setValue(self, value):
        self.__value = value

    def getLeft(self):
        return self.__left_node

    def setLeft(self, left_node):
        self.__left_node = left_node

    def getRight(self):
        return self.__right_node

    def setRight(self, right_node):
        self.__right_node = right_node

class BinarySearchTree:

    def __init__(self, root=None):
        self.__root = root

    def getRoot(self):
        return self.__root

    def setRoot(self, root):
        self.__root = root

    def empty(self):
        if self.__root is not None:
            return False
        return True

    def clear(self):
        self.__root = None

    def insert(self, root_node, value):

        # If the tree is empty, add it as the new root
        if root_node is None:
            new_node = Node(value)
            self.__root = new_node
            return

        # Otherwise checks if the current value is smaller than value of relative root
        # if that is the case then the new node must lies at left of its root
        elif value < root_node.getValue():
            #if the left node is None then we have found the spot to add the new node
            if root_node.getLeft() is None:
                root_node.setLeft(Node(value))
            # recursive call
            else:
                self.insert(root_node.getLeft(),value)
                return
        # Else it understands that the current value is bigger than value of relative root
        # if that is the case then the new node must lies at right of its root
        elif value > root_node.getValue():
            # if the right node is None then we have found the spot to add the new node
            if root_node.getRight() is None:
                root_node.setRight(Node(value))
            else:
                self.insert(root_node.getRight(),value)
                return
        else:
            raise RuntimeError('Element already exists')




    def remove(self, root, value):

        # Base Case
        if root is None:
            raise RuntimeError('Node not found')
        if self.getRoot() is None:
            raise RuntimeError('Empty Tree')

        # If the value to be deleted is smaller the root's value
        # then it lies in left subtree
        elif value < root.getValue():
            root.setLeft(self.remove(root.getLeft(), value))

        # If the kye to be delete is greater than the root's key
        # then it lies in right subtree
        elif value > root.getValue():
            root.setRight(self.remove(root.getRight(), value))

        # If key is same as root's key, then this is the node
        # to be deleted
        else:

            # Node with only one child or no child
            if root.getLeft() is None:
                temp = root.getRight()
                root = None
                return temp

            if root.getRight() is None:
                temp = root.getLeft()
                root = None
                return temp

            # Node with two children: Get the inorder successor
            # (smallest in the right subtree)
            temp = self.minValueNode(root.getRight())
            # Copy the inorder successor's content to this node
            root.setValue(temp.getValue())

            # Delete the inorder successor
            root.setRight(self.remove(root.getRight(), temp.getValue()))

        return root

    # Given a non-empty binary search tree, return the node
    # with minum key value found in that tree. Note that the
    # entire tree does not need to be searched
    def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while (current.getLeft() is not None):
            current = current.getLeft()

        return current

    def search(self, value, node):
        if node.getValue() == value:
            return True
        if(value < node.getLeft().getValue()):
            self.search(value, node.getLeft())
        else:
            self.search(value, node.getRight())

    # pre-order show (root-left-right)
    def show_pre_order(self, curr_node):

        if curr_node is not None:
            print('%d' % curr_node.getValue(), end=' ')
            self.show_pre_order(curr_node.getLeft())
            self.show_pre_order(curr_node.getRight())

    # post-order show (root-right-left)
    def show_post_order(self, curr_node):

        if curr_node is not None:
            print('%d' % curr_node.getValue(), end=' ')
            self.show_post_order(curr_node.getRight())
            self.show_post_order(curr_node.getLeft())

    # in-order show (root-right-left)
    def show_in_order(self, curr_node):

        if curr_node is not None:
            self.show_in_order(curr_node.getRight())
            print('%d' % curr_node.getValue(), end=' ')
            self.show_in_order(curr_node.getLeft())

