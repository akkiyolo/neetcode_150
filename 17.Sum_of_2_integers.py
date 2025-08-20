'''
SUM OF 2 INTEGERS
Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = 2, b = 3
Output: 5
'''
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        for i in range(1,abs(b)+1):
            if b>=0:
                a+=1
            else:
                a-=1
        return a