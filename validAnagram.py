# create a dictionary
# store each character in both strings in two different dictionaries
# compare both dictionaries with each other
# if similar, return True
# else, return False
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        freq_ = {}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for n in t:
            if n in freq_:
                freq_[n] += 1
            else:
                freq_[n] = 1 
        return freq == freq_


# Time complexity: O(n + m), n is len(s), m is len(t)
# Space complexity: O(1), since there are only 26 characters in the alphabet

