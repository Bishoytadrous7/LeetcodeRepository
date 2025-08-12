class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      # Approach 1: Categorize by count
      '''
      use a 26-sized array that maps a-z to their count
      use dictionary {countarray -> list of anagrams}
      '''
      mappings = defaultdict(list)
      for s in strs:
          count = [0] * 26
          for ch in s:
              count[ord(ch) - ord('a')] += 1
          mappings[tuple(count)].append(s)
      return mappings.values()
      # m: length of array, n: avg length of strings
      # O(m * n * 26) -> O(m * n)
      # O(m * n)

      # Approach 2: Categorize by sorted string
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      '''
      traverse array sorting every element and adding to
      a dictionary {sorted -> list of anagrams}
      '''
      mappings = defaultdict(list)
      for s in strs:
          key = ''.join(sorted(s))
          mappings[key].append(s)
      return mappings.values()
      # O(m * n log n)
      # O(m * n)