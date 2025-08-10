# Iterate over each index as the first number
# For each first index, iterate over all following indexes
# Compare the sum of the two numbers to the target
# If a matching pair is found, return their indexes in a list
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for first in range(len(nums)):
            for i in range(first + 1, len(nums)):
                if nums[first] + nums[i] == target: 
                    return [first, i]
# Time complexity: O(n^2), two nested loops 
# Space complexity: O(1),  only a list is created

#Another Approach, (a better one for time complexity)

# Create a dictionary
# Loop through each index and value in nums
# Calculate the complement needed to reach the target
# If the complement is already in the dictionary, return its index and the current index
# Otherwise, store the current value and its index in the dictionary
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i
            
# Time complexity: O(n) 
# Space complexity: O(n), dictionary stores up to n elements in the worst case
