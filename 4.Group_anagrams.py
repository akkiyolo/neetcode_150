'''
GROUP ANAGRAMS
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Dictionary to group anagrams
        groups = {}
        
        # For each string, sort it and use as key
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in groups:
                groups[sorted_s] = []
            groups[sorted_s].append(s)
        
        # Return all groups
        return list(groups.values())