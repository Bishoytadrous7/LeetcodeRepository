class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
      l_mult = 1
      r_mult = 1
      l_arr = [0] * len(nums)
      r_arr = [0] * len(nums)

      for i in range(len(nums)):
          j = -i -1
          l_arr[i] = l_mult
          r_arr[j] = r_mult
          l_mult *= nums[i]
          r_mult *= nums[j]

      return [l* r for l,r in zip(l_arr,r_arr)]
# Time complexity: O(n) (went through the array three times)
# Space complexity: O(n) (two extra arrays)

#Better approach for space complexity 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            res[i] = left
            left *= nums[i]
        right = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= right
            right *= nums[i]
        return res
# Time complexity: O(n)
# Space complexity: O(1) extra space