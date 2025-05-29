'''
146. LRU Cache
Solved
Medium
Topics
conpanies icon
Companies
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.

'''
import heapq

class LRUEntry:

    def __init__(self, key: int, val: int, t: int):
        self.key = key
        self.val = val
        self.t = t

    def __lt__(self, other):
        return self.t < other.t


class LRUCache:

    def __init__(self, capacity: int):
        self.vals = {}
        self.capacity = capacity
        self.used_keys = []
        self.timestamp = 0

    def get_timestamp(self) -> int:
        res = self.timestamp
        self.timestamp += 1
        return res

    def get(self, key: int) -> int:
        res = self.vals.get(key, -1)
        if res != -1:
            self.vals[key].t = self.get_timestamp()
            return res.val

        else:

            return res 

    def put(self, key: int, value: int) -> None:
        if key in self.vals:
            self.vals[key].key = key
            self.vals[key].val = value
                
        else:
            if self.capacity == 0:
                heapq.heapify(self.used_keys)
                least_key = heapq.heappop(self.used_keys)
                del self.vals[least_key.key]
                self.vals[key] = LRUEntry(key, value, 0)
                #heapq.heappush(self.used_keys, self.vals[key])
                self.used_keys.append(self.vals[key])
            else:
                self.capacity -= 1
                self.vals[key] = LRUEntry(key, value, 0)
                #heapq.heappush(self.used_keys, self.vals[key])
                self.used_keys.append(self.vals[key])

        self.vals[key].t = self.get_timestamp()
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)