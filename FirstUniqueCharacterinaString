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
        #a list to keep track of repeated characters
        lst = []
        #iterative value keeper for outer loop 
        i = 0
        for fl in s:
            j = 0 # to keep track repeaters
            for sl in s[i+1:len(s):1]: #inner loop to start from next char and run through the lenght of the string
                if fl == sl: #if character repeats
                    lst.append(fl) #append to the list created in line 4
                    j += 1
                    break # no point in iterating once it repeats
            if j == 0 and fl not in lst: #critical decision maker where j will be 0 for no repeat chars as well as j could be zero if the repeat value has occured earlier
                return i
            i += 1 # increment to move to next char
        return -1 #if nothing clicks return -1
        
