class ListNode:
    def __init__(self, key=-1, val = -1):
        self.key = key
        self.val = val
        self.next = self.prev = None

class DLL:
    def __init__(self):
        self.head, self.tail = ListNode(), ListNode()
        self.head.next, self.tail.prev = self.tail, self.head
    
    def append(self, key, val):
        new_node = ListNode(key, val)
        pre = self.tail.prev
        pre.next = self.tail.prev = new_node
        new_node.prev, new_node.next = pre, self.tail
        return new_node
    
    def popleft(self):
        tmp = self.head.next
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        return tmp
    
    def remove(self, node):
        pre, nxt = node.prev, node.next
        pre.next, nxt.prev = nxt, pre

class LRUCache:
    def __init__(self, capacity: int):
        self.map, self.dll, self.capacity = {}, DLL(), capacity

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.dll.remove(node)
            self.map[key] = self.dll.append(key, node.val)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.dll.remove(self.map[key])
            self.map[key] = self.dll.append(key, value)
            return
        
        if len(self.map) == self.capacity:
            tmp = self.dll.popleft()
            del self.map[tmp.key]
        
        node = self.dll.append(key, value)
        self.map[key] = node
