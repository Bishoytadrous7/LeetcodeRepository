class Solution:
  def minWindow(self, s: str, t: str) -> str:
      '''
          Q: case-sensitive?

          Sliding Window:
          - two dicts for char counts of s and t
          - two variables need, have to check for validity of window
          - move r until window has all desirable characters (need == have) (valid)
          - move l until window doesn't have all desirable chars (need != have) (not valid), 
            taking into account length of window every time

          '''
      if t == "":
          return ""
      countT={}
      window= {}
      for c in t:
          countT[c] = countT.get(c, 0) +1
      l = 0
      have = 0
      need = len(countT)
      res = [-1, -1]
      resLen = float("infinity")
      for r in range(len(s)):
          c = s[r]
          window[c] = 1 + window.get(c, 0)
          if c in countT and window[c] == countT[c]:
              have +=1
          while have == need:
              if (r-l+1) < resLen:
                  resLen = r-l+1
                  res = [l, r]
              window[s[l]] -=1
              if s[l] in countT and window[s[l]] < countT[s[l]]:
                  have -=1
              l +=1
      l, r = res
      return s[l: r+1] if resLen != float("infinity") else ""
#Time complexity: O(n*m)
#Space Complexity: O(m)
#n is the length of the string and m is the total number of unique characters in the strings 


