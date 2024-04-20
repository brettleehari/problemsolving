"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        lst = []

        i = 0
        for fl in s:
            j = 0
            for sl in s[i+1:len(s):1]:
                if fl == sl:
                    lst.append(fl)
                    j += 1
                    break
            if j == 0 and fl not in lst:
                return i
                     

            i += 1


        return -1
        
