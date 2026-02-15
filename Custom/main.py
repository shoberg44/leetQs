from LL import LList
from Med.LRU import LRUCache
hello = LList()
hello.push(1)

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