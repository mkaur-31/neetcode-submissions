import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.size = k
        self.data = []
        for num in nums:
            self.add(num)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.data, val)
        if len(self.data) > self.size:
            heapq.heappop(self.data)
        
        return self.data[0]
            
        
