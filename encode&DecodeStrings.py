'''
Q: empty string?
Q: what type of characters in these string?
Q: case-sensitivity?

store length of each string along with a delimiter like ‘#’ because the length isn’t 
always a single digit
'''
class Solution:
    
def encode(self, strs: List[str]) -> str:
    res = ""
    for s in strs:
        res += str(len(s)) + '#' + s
    return res

def decode(self, s: str) -> List[str]:
    res = []
    i = 0

    while i < len(s):
        j = i
        while s[j] != '#':
            j += 1
        length = int(s[i:j])
        res.append(s[j+1 : j+1+length])
        i = j+1+length
    return res

# Time Complexity: Encode: O(m) Decode: O(m) (where m is the total number of characters across all strings). 
# Space Complexity: O(m + n) for both encode() and decode() (where n is the number of strings and m is the total number of characters).
