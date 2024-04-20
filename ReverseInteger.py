"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
"""


class Solution:
    def reverse(self, x):
        new_x = 0
        x_sign = "positive"
        if x < 0:
            x = abs(x)
            x_sign = "negative"
        while x != 0.0 :
            new_x = (new_x * 10) + (x % 10)
            x = (x  - x % 10) / 10
        if x_sign=="negative":
            new_x = new_x - (2*new_x)  
        if abs(new_x) < 2**31 and new_x != 2**31 - 1:  
            return int(new_x)
        else:
            return 0
x = 123

boj = Solution()
print(boj.reverse(x))
