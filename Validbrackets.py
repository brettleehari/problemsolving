"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
#crude quick solution
class Solution:
    def isValid(self, s: str) -> bool:

        pairs = { "}" : "{",
                 "]"  : "[",
                 ")": "("}
        lst = []
        for brace in s:
            if brace in list(pairs.keys()) and len(lst) < 1:
                return False
            if brace not in list(pairs.keys()):
                lst.append(brace)
            else:
                if pairs[brace] != lst[-1]:
                    return False
                elif pairs[brace] == lst[-1]:
                    lst.pop()
        if len(lst) > 0:
            return False
        else:
            return True
