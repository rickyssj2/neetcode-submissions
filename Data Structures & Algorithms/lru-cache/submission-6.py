class ListNode:
    def __init__(self, key=-1, val = -1):
        self.key = key
        self.val = val
        self.next = self.prev = None

class DLL:
    def __init__(self):
        self.head, self.tail = ListNode(), ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def append(self, key, val):
        new_node = ListNode(key, val)
        pre = self.tail.prev
        pre.next = new_node
        new_node.prev = pre
        new_node.next = self.tail
        self.tail.prev = new_node
        return new_node
    
    def popleft(self):
        node = self.head.next
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        return node
    
    def remove(self, node):
        pre, nxt = node.prev, node.next
        pre.next = nxt
        nxt.prev = pre

class LRUCache:
    def __init__(self, capacity: int):
        self.map = {}
        self.dll = DLL()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.dll.remove(node)
            self.map[key] = self.dll.append(key, node.val)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            self.dll.remove(node)
            self.map[key] = self.dll.append(key, value)
            return
        
        if len(self.map) == self.capacity:
            node = self.dll.popleft()
            del self.map[node.key]
        
        node = self.dll.append(key, value)
        self.map[key] = node
