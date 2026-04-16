class TimeMap:

    def __init__(self):
        self.redis = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.redis:
            self.redis[key] = []
        
        self.redis[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.redis:
            return ""
        left, right = 0, len(self.redis[key]) - 1

        best = ""
        while left <= right:
            mid = (left + right) // 2
            value, time = self.redis[key][mid]
            if time == timestamp:
                return value
                
            elif time <= timestamp:
                best = value
                left = mid + 1
            else:
                right = mid - 1
                
        return best


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)