from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.od = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.od: return -1
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            self.od[key] = value
            return
        if len(self.od) == self.capacity: self.od.popitem(last=False)
        self.od[key] = value
