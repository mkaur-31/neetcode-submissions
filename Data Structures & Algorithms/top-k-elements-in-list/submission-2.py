class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        count = collections.defaultdict(int)
        for i in nums:
            count[i] += 1
        
        
        countl = [(-val,key) for key,val in count.items()]
        heapq.heapify(countl)
    
        res = []
        for i in range(k):

            x = heapq.heappop(countl)
            res.append(x[1])
        return res


        