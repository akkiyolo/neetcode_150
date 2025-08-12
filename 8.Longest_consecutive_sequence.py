'''
LONGEST CONSECUTIVE SEQUENCE
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3
'''
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Convert nums to a set for O(1) lookups
        num_set = set(nums)
        longest = 0
        
        # Iterate through each number
        for num in num_set:
            # Only start checking sequences from the smallest number in the sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # Check for consecutive numbers
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                # Update longest streak if current is larger
                longest = max(longest, current_streak)
        
        return longest