class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Q: empty string?
        Q: time/space constraints?

        # Approach 1: Brute Force O(n^2)
        check every possible substring

        # Approach 2: Sliding Window O(n)
        validation criteria: length of substring - max char frequency <= k
        move right pointer until validation criteria is not met
        move left pointer until validation criteria is met
        keep track of alphabets count in a dictionary
        '''
        l = 0
        res = 0
        counts = {}
        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            while (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
        return res
#Time: O(26 *n) = O(n)
#Space:O(1)

#Better Approach
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res = 0
        maxf=0

        for r in range(len(s)):
            count[s[r]] = 1+ count.get(s[r], 0)

            maxf = max(maxf, count[s[r]])

            while (r-l+1) - maxf > k:
                count[s[l]] -= 1
                l+=1
            res = max(res, r-l+1)
        return res

#Time complexity: O(n)
#Space Complexity: O(n)

