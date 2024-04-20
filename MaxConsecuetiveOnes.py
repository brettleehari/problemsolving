"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""

class Solution():
    def findMaxConsecutiveOnes(self, nums):
        #constraints
        bi = [2,3,4,5,6,7,8,9]
        if len(nums) < 1 or len(nums) > 10**5:
            #return ("Hey this is a constraint")
            return 0
        if any(item in bi for item in nums):
            return 0
            #return ("Not a binary list")
        else:
            #print("Valid number")
            max_v = 0
            max_lst = []
            i = 1
            for element in nums:

                if element==1:
                    max_v += 1
                else:
                    max_lst.append(max_v)
                    max_v = 0
                #if the last number is 1
                if i == len(nums):
                    max_lst.append(max_v)

                i += 1
            
            return max(max_lst)



nums = [1,0,1,1,1]
obj = Solution()
print(obj.findMaxConsecutiveOnes(nums))
