class LList:
    def __init__(self):
        self._head = None
        self._tail = None
    def push(self, data):
        data_node = self.Node(data)
        if not self._tail:
            self._tail = data_node
        else:
            # update tail
            prev = self._tail
            self._tail = data_node

            # link prev node
            prev.next = data_node
            data_node.prev = prev
        if not self._head:
            self._head = data_node


    def pop(self, front=False):
        # if empty
        if not self._head:
            return None

        # reassign tail to tails prev
        target = self._tail
        self._tail = target.prev
        # remove links
        target.prev.next = None
        return target.data
    def __str__(self):
        current_node = self._head
        ret = []
        while current_node.next:
            ret.append(str(current_node.data))
            current_node = current_node.next
        ret.append(str(current_node.data))
        return ' -> '.join(ret)




    '''
    A class to track objects in the Linked List
    '''

    class Node:
        next = None
        prev = None
        data = None

        def __init__(self, data):
            self.data = data