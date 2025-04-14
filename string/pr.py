# this is a comment
print("Hello world")

class Solution:
    def reverseString(self, s: list[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

s = ['a', 'b', 'h', 'a', 'y']
Solution().reverseString(s)
print(s)  # Output: ['y', 'a', 'h', 'b', 'a']

print("Hello world") # 2nd time!
