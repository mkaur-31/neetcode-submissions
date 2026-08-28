class TimeMap:
    from collections import defaultdict, deque

    def __init__(self):
        self.ds = defaultdict(list)
        self.vals = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ds[key].append(timestamp)
        self.vals[(key,timestamp)] = value
        
        

    def get(self, key: str, timestamp: int) -> str:
        times = self.ds[key]
        l, r = 0, len(times)-1
        res = ""
        if not times or times[0] > timestamp : return res
        while l <= r:
            mid = (l+r)//2
            if timestamp == times[mid]:
                res = self.vals[(key,times[mid])]
                return res
            elif timestamp < times[mid]:
                r = mid-1
            else:
                l = mid + 1
        return self.vals[(key,times[r])]