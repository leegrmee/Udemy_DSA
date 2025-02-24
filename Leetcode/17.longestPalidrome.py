"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest
palindrome
 that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.
"""

from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:

        h = defaultdict(int)
        result = 0

        for char in s:
            h[char] += 1
            if h[char] % 2 == 0:
                result += 2
        for v in h.values():
            if v % 2 == 1:
                result += 1
                break
        return result


"""
# 두 표현은 동일하게 작동/ v % 2 이 0이면 , 0은 False로 평가되기 때문에. 
if v % 2:
    print("홀수입니다")

if v % 2 == 1:
    print("홀수입니다")

"""


class Solution:
    def longestPalindrome(self, s: str) -> int:

        seen = set()
        result = 0

        for c in s:
            if c in seen:
                seen.remove(c)
                result += 2
            else:
                seen.add(c)

        if seen:
            result += 1

        return result
