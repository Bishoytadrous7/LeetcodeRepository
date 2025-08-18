'''
Q: empty array?
Q: only numbers?
Q: duplicates?
Q: time/space constraints

Approach Brute Force: O(n^2); for every element (n); search (n) for every consecutive numbers 
(n at worst);

Approach 1: sort O(n log n)

Approach 2: Think of Sequences O(n) O(n)

put elements in set for faster lookup
in array, check if element is a start of sequence; if yes, use set to look up its neighbors and count the subsequence lenght
keep track of max subsequence
We check every element at most twice so O(n)
'''
class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
      numSet = set(nums)
      longest = 0
      for i in numSet:
          if i-1  not in numSet:
              length = 0
              while i+length in numSet:
                  length+= 1
              longest = max(length,longest)
      return longest
#Time complexity: O(n)
#Space complexity: O(n)