'''
INTERSECTION OF 2 ARRAYS
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
'''
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Create a set from nums1 to eliminate duplicates and enable O(1) lookup
        set1 = set(nums1)
        
        # Create result set to store intersection
        result = set()
        
        # Check each number in nums2
        for num in nums2:
            # If number exists in set1, add to result
            if num in set1:
                result.add(num)
                
        return list(result)