class DoubleLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    def __len__(self):
        return self._size
    '''
    Appends or prepends to the linked list
    
    @param data; the data to add store in the new appended entry
    @param front bool; to append the new entry to the front/head of the linked list. Default False, appends to back.tail of LL
    '''
    def push(self, data, front=False):
        data_node = self.__Node(data)
        if not self._tail or not self._head:
            if self._size != 0 or not (self._head is None and self._tail is None): raise IndexError('pushing on malformed linkedlist')
            # no nodes
            self._tail = data_node
            self._head = data_node
        else:
            if front:
                # update new leading/front node
                prevLead = self._head
                self._head = data_node

                # link the new node to neighbors
                prevLead.prev = data_node
                data_node.next = prevLead
            else:
                # same as front push but on the back/tail
                prevLead = self._tail
                self._tail = data_node

                prevLead.next = data_node
                data_node.prev = prevLead
        self._size += 1

    '''
    removes and then returns the value at the endpoint of the LL
    
    @param front bool; whether to remove from the head of the LL (replicating a queue) when true, or from the tail (a stack). Defaults to False
    '''
    def pop(self, front=False):
        self.has_content()
        # on front
        if front:
            # reassign tail to tails prev
            target = self._head
            self._head = target.next
            # remove links
            target.next.prev = None
        else:
            # reassign tail to tails prev
            target = self._tail
            self._tail = target.prev
            # remove links
            target.prev.next = None

        self._size -= 1
        return target.data

    '''
    A function that raises an exception when trying to access data from an empty LL
    '''
    def has_content(self):
        # if empty
        if not len(self):
            # Create the exception
            err = IndexError('Popping from empty or malformed list')
            # Add the note (modifies 'err' in place)
            err.add_note(f'H/T: {self._head} / {self._tail}')
            raise err
        return True

    '''
    Gets an endpoint of the list (front or back)
    @param from_back bool; if true, returns the data at the tail of the LL. Default is False
    '''
    def get_end(self, from_front=False):
        self.has_content()
        if not from_front:
            return self._tail.data
        else:
            return self._head.data

    def __str__(self):
        str_rep = ' -> '.join(self.__repr__())
        if not str_rep:
            str_rep = '<Empty Linked List>'
        return str_rep

    def __repr__(self):
        # use different print for empty lists
        try:
            self.has_content()
        except IndexError:
            return list()

        ret = []
        current_node = self._head
        while True:
            ret.append(str(current_node.data))
            current_node = current_node.next

            # exit if no next node
            if not current_node:
                break
        return ret



    '''
    A class to track objects in the Linked List
    '''
    class __Node:
        next = None
        prev = None
        data = None

        def __init__(self, data):
            self.data = data