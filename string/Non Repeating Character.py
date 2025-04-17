'''
Given a string s consisting of lowercase English Letters. Return the first non-repeating character in s.
If there is no non-repeating character, return '$'.
Note: When you return '$' driver code will output -1.

Examples:

Input: s = "geeksforgeeks"
Output: 'f'
Explanation: In the given string, 'f' is the first character in the string which does not repeat.
Input: s = "racecar"
Output: 'e'
Explanation: In the given string, 'e' is the only character in the string which does not repeat.
Input: s = "aabbccc"
Output: -1
Explanation: All the characters in the given string are repeating.
Constraints:
1 ≤ s.size() ≤ 105
'''

class Solution:
    max_char = 26
    def nonRepeatingChar(self,s):
        #code here
        vis = [-1] * self.max_char
        
        for i in range(len(s)):
            if vis[ord(s[i]) - ord('a')] == -1:
                vis[ord(s[i]) - ord('a')] = i
                
            else:
                vis[ord(s[i]) - ord('a')] = -2
                
                
        idx = float('inf')
        
        for i in range(self.max_char):
            if vis[i] >=0:
                idx = min(idx,vis[i])
                
        return '$' if idx == float('inf') else s[idx]
        
    
