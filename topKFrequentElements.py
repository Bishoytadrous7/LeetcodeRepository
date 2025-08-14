                    #Apprach 1: Bucket Sort            
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if not num in count:
                count[num] = 0
            count[num] += 1

        freq = [[] for i in range(len(nums)+1)]
        for num, c in count.items():
            freq[c].append(num)
        result = []
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result

# Time complexity: O(n)
# Space complexity: O(n)


                    #Approach 2: Sorting: 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
# Time complexity: O(nlogn)
# Space complexity: O(n)

                   #Approach 3: Min Heap
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
# Time complexity: O(nlogk)
# Space complexity: O(n+k)