import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1: return stones[0]
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        while len(heap) > 1:

            x , y = -heapq.heappop(heap), -heapq.heappop(heap)
            
            if x > y:
                heapq.heappush(heap, -(x-y))
            elif x < y:
                heapq.heappush(heap, -(y-x))
            else:
                heapq.heappush(heap,0)

        return -heap[0]
        
                





        