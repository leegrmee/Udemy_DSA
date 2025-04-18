"""
Given a string s, return true if it is a palindrome, otherwise return false.
A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

ignore case, case-insensitive => lower()
ignore non-alphanumeric characters => isalnum()
"""


# first approach
class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1, p2 = 0, len(s) - 1

        while s[p1].lower() == s[p2].lower():
            p1 += 1
            p2 -= 1
            if p1 == mid and p2 == mid:
                return True

        return False


"""
problem
1.알파벳과 숫자가 아닌 문자 처리 누락
2.인덱스 검사 누락:
while s[p1].lower() == s[p2].lower()에서 p1과 p2가 문자열 범위를 벗어나는 경우
3.if p1 == mid and p2 == mid:는 홀수 길이의 문자열에서만 작동. 짝수 길이의 문자열에서는 p1과 p2가 서로 교차
"""


# second approach
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for c in s:
            if c.isalnum():
                new_str += c.lower()

        return new_str == new_str[::-1]


"""
time complexity: O(n)
space complexity: O(n)
"""


# third approach
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.is_alphanumeric(s[l]):
                l += 1
            while l < r and not self.is_alphanumeric(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

    def is_alphanumeric(self, c: str) -> bool:
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )


"""
time complexity: O(n)
space complexity: O(1)
"""
