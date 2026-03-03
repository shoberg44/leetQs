class DoubleLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    def __len__(self):
        return self._size
    def push(self, data):
        data_node = self.Node(data)
        if not self._tail:
            # no nodes
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
        self._size += 1

    '''
    removes and then returns the value at the endpoint of the LL
    
    @param front bool; whether to remove from the head of the LL (replicating a queue) when true, or from the tail (a stack). Defaults to False
    '''
    def pop(self, front=False):
        # if empty
        if not self._head or not self._tail:
            # Create the exception
            err = IndexError('popping from empty or malformed list')

            # Add the note (modifies 'err' in place)
            err.add_note(f'H/T: {self._head} / {self._tail}')

            # Raise the modified exception
            raise err

        # reassign tail to tails prev
        target = self._tail
        self._tail = target.prev
        # remove links
        target.prev.next = None
        self._size -= 1
        return target.data

    '''
    Gets an endpoint of the list (front or back)
    @param from_back bool; if true, returns the data at the tail of the LL. Default is False
    '''
    def getEnd(self, from_back=False):
        if from_back:
            return self._tail.data
        else:
            return self._head.data

    def __str__(self):
        current_node = self._head
        if current_node is None:
            return '<Empty Linked List>'
        ret = []
        while current_node.next:
            ret.append(str(current_node.data))
            current_node = current_node.next
        ret.append(str(current_node.data))
        return ' -> '.join(ret)




    '''
    A class to track objects in the Linked List
    '''
    class __Node:
        next = None
        prev = None
        data = None

        def __init__(self, data):
            self.data = data