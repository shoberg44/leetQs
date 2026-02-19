import collections

# self balancing BSTs
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self._isRed = True
        self.data = data

    def delete(self, key):
        pass

    '''
    Inserts a Node onto a tree
    
    returns the parent of what was just inserted
    '''
    def insert(self, head):
        if not head:
            raise "cannot insert on None"

        can_next = head
        while True:
            if self.data < can_next.data:
                if can_next.left:
                    can_next = can_next.left
                else:
                    can_next.left = self
                    return can_next
            else:
                if can_next.right:
                    can_next = can_next.right
                else:
                    can_next.right = self
                    return can_next
    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self, root=Node(None)):
        self.root = root
    def __str__(self):
        ret = []
        queue = collections.deque()
        queue.append((self.root,0))

        prev_depth = 0
        while queue:
            current_tuple = queue.popleft()
            node = current_tuple[0]
            depth = current_tuple[1]

            if prev_depth != depth:
                ret.append('\n')
                prev_depth = depth

            ret.append(' ' * depth)
            ret.append(str(node.data))
            ret.append(' ' * depth)

            if node.left:
                queue.append((node.left,depth+1))
            if node.right:
                queue.append((node.right,depth+1))

        return ''.join(ret)

class RBTree (Tree):
    pass
class AVLTree(Tree):

    '''
    Right Rotates
    '''
    def _Rrot(self, node):
        pass
    '''
    Left Rotates
    '''
    def _Lrot(self, node):
        pass
    '''
    Balances a subtree
    '''
    def _balance(self, node):
        pass
