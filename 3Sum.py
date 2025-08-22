class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
      res = []
      nums.sort()

      for i, a in enumerate(nums):
          if a == nums[i-1] and i>0:
              continue

          left = i+1
          right = len(nums)-1
          while left < right:
              threeSum = a + nums[left] + nums[right]
              if threeSum > 0:
                  right -=1
              elif threeSum < 0:
                  left += 1
              else:
                  res.append([a, nums[left], nums[right]])
                  left += 1
                  right -= 1
                  while nums[left] == nums[left-1] and left < right:
                      left += 1
      return res
#Time complexity: O(n^2) 
#Space complexity: O(1) or O(n) O(n) extra space depending on the sorting algorithm.