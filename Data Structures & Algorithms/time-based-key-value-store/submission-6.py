class TimeMap:

    def __init__(self):
        self.hmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key].append((value, timestamp))
    # "test": [one, 10 | two, 20 | three, 30]
    def get(self, key: str, timestamp: int) -> str:
        values = self.hmap[key]
        l, r = 0, len(values)

        while l < r:
            mid = l + (r - l) // 2
            # mid = r - (r - l) // 2

            if not (values[mid][1] <= timestamp):
                r = mid
            else:
                l = mid + 1
        
        return values[r - 1][0] if 0 <= r - 1 < len(values) and values[r - 1][1] <= timestamp else ""

