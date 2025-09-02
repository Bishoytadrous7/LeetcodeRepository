class Solution:
  def search(self, nums: List[int], target: int) -> int:
      '''
      discrete cases; know if mid is in left or right sorted portions
      then know where to search based on which portion is it in
      '''
      l, r = 0, len(nums) - 1
      while l <= r:
          mid = (l + r) // 2
          if nums[mid] == target:
              return mid

          # left sorted portion
          if nums[mid] >= nums[l]:
              if target < nums[mid] and target >= nums[l]:
                  r = mid - 1
              else:
                  l = mid + 1

         # right sorted portion 
          else:
              if target > nums[mid] and target < nums[l]:
                  l = mid + 1
              else:
                  r = mid - 1
      return -1
      # O(log n)
      # O(1)