import unittest

from Custom.LL import DoubleLinkedList
from Med.LRU_lib import LRUCache
from Custom.Tree import Tree, Node, AVLTree, RBTree

class TestLRU(unittest.TestCase):
    def testLRU(self):
        c = LRUCache(2)
        self.assertEqual(len(c), 0)
        c.put(1, 1)  # cache is {1=1}
        self.assertEqual(c[1],1)
        self.assertEqual(len(c),1)
        c.put(2, 2)  # cache is {1=1, 2=2}
        self.assertEqual(c[1], 1)
        self.assertEqual(c[2], 2)
        self.assertEqual(len(c), 2)
        self.assertEqual(c.get(1),1)  # return 1
        self.assertFalse(c.get(0))
        c.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
        self.assertEqual(c.get(2),-1)  # returns -1 (not found)
        c.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
        self.assertEqual(c.get(1),-1) # return -1 (not found)
        self.assertEqual(c.get(3),3)  # return 3
        self.assertEqual(c.get(4),4)  # return 4

class TestLL(unittest.TestCase):
    def testSingleLinkedList(self):
        l = DoubleLinkedList()
        self.assertEqual(l._head, None)
        self.assertEqual(l._tail, None)
        self.assertEqual(len(l), 0)
        l.push(1)
        self.assertEqual(l._head.data, 1)
        self.assertEqual(l._tail.data, 1)
        self.assertEqual(len(l), 1)
        l.push(2)
        self.assertEqual(l._head.data, 1)
        self.assertEqual(l._tail.data, 2)
        self.assertEqual(len(l), 2)
        self.assertEqual(l.__str__(),'1 -> 2')
        l.push(4)
        self.assertEqual(l._head.data, 1)
        self.assertEqual(l._head.next.data, 2)
        self.assertEqual(l._tail, l._head.next.next)
        self.assertEqual(l._tail.data, 4)
        self.assertEqual(len(l), 3)
        l.pop()
        self.assertEqual(len(l), 2)
        self.assertEqual(l._head.data, 1)
        self.assertEqual(l._head.next.data, 2)
        self.assertEqual(l._tail, l._head.next)
        self.assertEqual(l._tail.data, 2)
        l.push(-1) # 1,2,4,-1
        self.assertEqual(len(l), 3)
    def testDoubleLinkedList(self):
        l = DoubleLinkedList()
        self.assertEqual(len(l),0)
        self.assertEqual(l.getEnd(),None)
    def testNoPop(self):
        l = DoubleLinkedList()
        try:
            l.pop()
        except IndexError as e:
            print(e)
            print(e.__notes__)
        except:
            print("something went wrong:",l)
        finally:
            print('done handling error')


class TestTree(unittest.TestCase):
    def testAVL(self):
        #simple tree
        #     5
        #   3   7
        #  1 4 6 8
        # 0
        tree = AVLTree([5, 3, 7, 1, 4, 6, 8, 0])
        print(tree,end="\n---------------------\n")
        print(tree._balance(tree.root),'\n',"-------\n")

        # 1
        #   2
        #    3
        #     ...8
        tree2 = AVLTree([2, 3, 4, 5, 6, 7, 8])
        print(tree2, end="\n---------------------\n")
        print(tree2._balance(tree2.root), '\n', "-------\n")