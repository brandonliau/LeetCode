class TimeMap:
    def __init__(self):
        self.ds = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.ds:
            self.ds[key] = []
        self.ds[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values, ans = self.ds.get(key, []), ""
        low, high = 0, len(values) - 1
        
        while low <= high:
            mid = (high + low) // 2
            if values[mid][1] <= timestamp:
                ans = values[mid][0]
                low = mid + 1
            else:
                high = mid - 1
        return ans
