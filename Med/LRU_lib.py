import collections

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._capacity = capacity
        self._stack = collections.OrderedDict()

    def __len__(self):
        return len(self._stack)

    def __getitem__(self, item):
        return self._stack[item]
    def __setitem__(self, key, value):
        self._stack[key] = value
    def __delitem__(self, key):
        del self._stack[key]

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        res = self._stack.get(key, -1)
        if not res == -1:
            self._stack.move_to_end(key)
        return res

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if not key in self._stack:
            # need to insert
            if len(self._stack) >= self._capacity:
                # at capacity
                self._stack.popitem(False)
            self._stack[key] = value
        else:
            self._stack.move_to_end(key)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)