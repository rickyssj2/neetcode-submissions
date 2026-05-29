class TimeMap:

    def __init__(self):
        self.hmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key].append((value, timestamp))
    # "test": [one, 10 | two, 20 | three, 30]
    def get(self, key: str, timestamp: int) -> str:
        values = self.hmap[key]
        l, r = 0, len(values) - 1

        while l < r:
            # mid = l + (r - l) // 2
            mid = r - (r - l) // 2

            if values[mid][1] <= timestamp:
                l = mid
            else:
                r = mid - 1
        
        return values[r][0] if 0 <= r < len(values) and values[r][1] <= timestamp else ""

