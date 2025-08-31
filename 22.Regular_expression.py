class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Create a DP table with dimensions (len(s) + 1) x (len(p) + 1)
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Empty pattern matches empty string
        dp[0][0] = True
        
        # Handle patterns starting with '*'
        for j in range(1, len(p) + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        
        # Fill DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] == '*':
                    # Zero occurrences: skip the char and '*'
                    dp[i][j] |= dp[i][j-2]
                    # One or more occurrences: if current char matches preceding char or '.'
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        dp[i][j] |= dp[i-1][j]
                else:
                    # Current chars match or pattern has '.'
                    if p[j-1] == s[i-1] or p[j-1] == '.':
                        dp[i][j] = dp[i-1][j-1]
        
        return dp[len(s)][len(p)]
        