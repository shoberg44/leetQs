from LL import LList
from Med.LRU import LRUCache
from Tree import Tree, Node, AVLTree, RBTree

def testLinkedList():
    hello = LList()
    hello.push(1)
    hello.push(2)
    print(hello)
    hello.push(4)
    print(hello.pop())
    hello.push(-1) # 1,2,4,-1
    print(hello)

def testLRU():
    lRUCache = LRUCache(2)
    print(lRUCache.put(1, 1)) # cache is {1=1}
    print(lRUCache.put(2, 2)) # cache is {1=1, 2=2}
    print(lRUCache.get(1))    # return 1
    print(lRUCache.put(3, 3)) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    print(lRUCache.get(2))    # returns -1 (not found)
    print(lRUCache.put(4, 4)) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    print(lRUCache.get(1))   # return -1 (not found)
    print(lRUCache.get(3))    # return 3
    print(lRUCache.get(4))    # return 4

def testTree():
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




testTree()