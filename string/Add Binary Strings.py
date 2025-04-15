'''
Given two binary strings s1 and s2 consisting of only 0s and 1s. Find the resultant string after adding the two Binary Strings.
Note: The input strings may contain leading zeros but the output string should not have any leading zeros.

Input: s1 = "1101", s2 = "111"
Output: 10100
Explanation:
 1101
+ 111
10100
Input: s1 = "00100", s2 = "010"
Output: 110
Explanation: 
  100
+  10
  110
Constraints:
1 ≤s1.size(), s2.size()≤ 106
'''
def trimleadingzeros(s):
    
    firstone = s.find('1')
    return s[firstone:] if firstone != -1 else '0'

class Solution:
	def addBinary(self, s1, s2):
		# code here
		s1 = trimleadingzeros(s1)
		s2 = trimleadingzeros(s2)
		
		n = len(s1)
		m = len(s2)
		
		if n < m :
		    s1,s2 = s2,s1
		    n,m=m,n
		    
        j = m - 1
        carry = 0
        result = []
        
        
        for i in range(n - 1,-1,-1):
            
            bit1 = int(s1[i])
            bitsum = bit1 + carry
            
            
            
            if j >= 0:
                bit2 = int(s2[j])
                bitsum += bit2
                j-=1
                
            bit = bitsum % 2
            carry = bitsum // 2
            
            result.append(str(bit))
            
        if carry > 0:
            result.append('1')
        return ''.join(result[::-1])
