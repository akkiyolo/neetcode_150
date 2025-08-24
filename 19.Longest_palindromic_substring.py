'''
LONGEST PALINDROMIC SUBSTRING
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
    
        start = 0
        longest = 0
        
        for i in range(len(s)):
            # Check odd length palindrome (center at i)
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > longest:
                    start = left
                    longest = right - left + 1
                left -= 1
                right += 1
            
            # Check even length palindrome (center between i and i+1)
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > longest:
                    start = left
                    longest = right - left + 1
                left -= 1
                right += 1
        
        return s[start:start + longest]
            