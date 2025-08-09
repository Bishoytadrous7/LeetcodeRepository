
# Create an empty dictionary 
# Loop through each number in nums.
# If the number is already in the dictionary, return True (duplicate found). 
# Otherwise, add it to the dictionary. 
# return False.
class Solution:
  def containsDuplicate(self, nums: list[int]) -> bool:
      freq = {}
      for i in nums:
          if i in freq:
              return True
          freq[i] = 1
      return False

# Time Complexity: O(n) 
# Space Complexity: O(n) — In the worst case, all elements are stored in the dictionary


# Another Approach (HashSet)
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)
#         return False

# Time Complexity: O(n) — We iterate through the list once.
# Space Complexity: O(n) — In the worst case, we store all n elements in the set.
