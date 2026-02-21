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
    def __init__(self):
        # simple tree
        tree = AVLTree()
    def __init__(self, nodes_list):
        nodes_list.reverse()
        self.root = Node(nodes_list.pop(len(nodes_list)-1))
        while nodes_list:
            num = nodes_list.pop(len(nodes_list)-1)
            Node(num).insert(self.root)

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
        # need to find the height of the l & r subtrees
        left_h = 0
        if node.left:
            left_h = self._height(node.left)
        right_h = 0
        if node.right:
            right_h = self._height(node.right)

        balance = left_h - right_h
        if  balance > 1:
            pass

        if balance < -1:
            self._Lrot(node)
        elif balance > 1:
            self._Rrot(node)

        return balance




    def _height(self, node):
        if node is None:
            return -1


        left_height = 0
        if node.left:
            left_height = self._height(node.left)
        else:
            left_height = -1 # BOTTOMED OUT LEFT TREE

        right_height = 0
        if node.right:
            right_height = self._height(node.right)
        else:
            right_height = -1

        if left_height == -1 and right_height == -1:
            return 0 # base case (no children start counting up)

        if left_height < right_height:
            return right_height + 1
        return left_height + 1




